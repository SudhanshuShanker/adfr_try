################################################################################
##
## This library is free software; you can redistribute it and/or
## modify it under the terms of the GNU Lesser General Public
## License as published by the Free Software Foundation; either
## version 2.1 of the License, or (at your option) any later version.
## 
## This library is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## Lesser General Public License for more details.
## 
## You should have received a copy of the GNU Lesser General Public
## License along with this library; if not, write to the Free Software
## Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
##
## (C) Copyrights Dr. Michel F. Sanner and TSRI 2016
##
################################################################################

#########################################################################
#
# Date: May 2003 Authors: Ruth Huey,  Michel Sanner
#
#    rhuey@scripps.edu
#    sanner@scripps.edu
#
# Copyright:  Michel Sanner, Ruth Huey, and TSRI
#
# revision: Guillaume Vareille
#
#########################################################################
#
# $Header: /mnt/raid/services/cvs/DejaVu2/Tests/test_ColorMapGUI.py,v 1.1.1.1.4.1 2017/07/13 22:24:00 annao Exp $
#
# $Id: test_ColorMapGUI.py,v 1.1.1.1.4.1 2017/07/13 22:24:00 annao Exp $
#



import sys, tkinter
import unittest
from mglutil.regression import testplus
from DejaVu2.colorTool import RGBRamp, RedWhiteBlueRamp, RedWhiteRamp, \
     WhiteBlueRamp
from DejaVu2.colorMap import ColorMap
from DejaVu2.ColormapGui import ColorMapGUI
from DejaVu2.Viewer import Viewer
from time import sleep


class ColorMapGUITest(unittest.TestCase):

    def setUp(self):
        self.root = tkinter.Tk()
        self.root.withdraw()

    def pause(self,sleepTime=0.2):
        self.root.update()
        sleep(sleepTime)

    def tearDown(self):
        self.root.destroy()

    def test_constructor(self):
        # test if we can display a very basic cmg
        cmap = ColorMap(name='test', ramp=RGBRamp())
        cmg = ColorMapGUI( cmap)
        self.pause()

        # Make sure that the Gui has been created properly.
        self.assertEqual(cmap.ramp, cmg.guiRamp)
        self.assertEqual(len(cmg.history), 1)
        self.assertEqual(cmg.cmapCurrent, True)
        

    def test_01_constructorWithViewer(self):
        # test building with a viewer
        cmap = ColorMap('test',ramp=RGBRamp())
        vi = Viewer(verbose=False)
        cmg = ColorMapGUI( cmap, viewer=vi)
        self.pause()
        self.assertTrue(cmg.ogl_cmw)
        vi.Exit()

    def test_constructorWidthOpt(self):
        # test setting canvas width
        cmap = ColorMap('test',ramp=RGBRamp())
        cmg = ColorMapGUI( cmap, width=300)
        self.pause()
        self.assertEqual(cmg.xrange, 275)


    def test_constructorXoffsetOpt(self):
        # test setting xoffset
        cmap = ColorMap('test',ramp=RGBRamp())
        cmg = ColorMapGUI( cmap, xoffset=5)
        self.pause()
        self.assertEqual( cmg.xrange, 195)


    def test_constructorHeightOpt(self):
        # test longer map
        cmap = ColorMap('test',ramp=RGBRamp(512))
        cmg = ColorMapGUI(cmap)
        self.pause()
        self.assertEqual(cmg.lengthRamp, 512)


    def test_Dismiss_cb(self):
        # test destruction of Toplevel
        cmap = ColorMap('test',ramp=RGBRamp(512))
        cmg = ColorMapGUI( cmap)
        self.pause()
        cmg.quit()
        assert cmg.master.winfo_exists()==0

    def test_Update(self):
        cmap = ColorMap(name='test', ramp=RGBRamp())
        cmg = ColorMapGUI(cmap, width=200)

        # update the ramp
        cmg.update(ramp=RedWhiteBlueRamp())
        self.assertEqual(cmg.lengthRamp, len(cmg.guiRamp))
        # the gui is not in a continuous mode....
        self.assertEqual(cmg.cmapCurrent, False)
        self.assertEqual(len(cmg.history), 1)
        
        # update with longer ramp
        cmg.update(ramp=RedWhiteBlueRamp(512))
        self.assertTrue(cmg.lengthRamp==len(cmg.guiRamp)==512)
        
        # update mini, maxi values...
        cmg.update(mini=1.0, maxi=7.0)
        self.assertEqual(cmg.guiMini, 1.0)
        self.assertEqual(cmg.guiMaxi, 7.0)

        # update and configure the ramp
        # The gui is not continuous
        cmg.update(cfgCmap=True)
        self.assertEqual(cmg.cmapCurrent, False)
        self.assertEqual(len(cmg.history),1)
        cmg.continuousUpdate.set(1)
        cmg.update(cfgCmap=True)
        self.assertEqual(cmg.cmapCurrent, True)
        self.assertEqual(len(cmg.history),2)
        
                                
    def test_stepBack_NoContinuous(self):
        cmap = ColorMap(name='test', ramp=RGBRamp())
        cmg = ColorMapGUI(cmap, width=200)
        self.assertEqual(len(cmg.history), 1)
        self.assertEqual(cmg.cmapCurrent, True)

        # Step back with only one entry in the history list.
        cmg.stepBack_cb()
        self.assertEqual(len(cmg.history), 1)
        self.assertEqual(cmg.cmapCurrent, True)
        cmg.apply_cb()
        self.assertEqual(len(cmg.history), 1)
        self.assertEqual(cmg.cmapCurrent, True)

        # Change the ramp without pushing it onto the history list
        # then stepBack_cb
        cmg.update(ramp=RedWhiteBlueRamp())
        self.assertEqual(len(cmg.history), 1)
        self.assertEqual(cmg.cmapCurrent, False)
        cmg.stepBack_cb()
        self.assertEqual(cmg.guiRamp, cmg.history[0])
        self.assertEqual(cmg.cmapCurrent, False)
        cmg.apply_cb()
        self.assertEqual(len(cmg.history), 1)
        self.assertEqual(cmg.cmapCurrent, True)
        self.assertEqual(cmg.guiRamp, cmap.ramp)
        
        # Change the ramp twice and push them onto the history list
        # then stepBack_cb until the beginning of the history list.
        cmg.update(ramp=RedWhiteBlueRamp())
        cmg.apply_cb()
        cmg.update(ramp=RedWhiteRamp())
        cmg.apply_cb()
        self.assertEqual(len(cmg.history), 3)
        cmg.stepBack_cb()
        cmg.stepBack_cb()
        cmg.apply_cb()
        self.assertEqual(len(cmg.history), 1)
        self.assertEqual(cmg.cmapCurrent, True)

        
        # Change the ramp three times and push them onto the history list
        # then stepBack_cb until the beginning of the history list.
        cmg.update(ramp=RedWhiteBlueRamp())
        cmg.apply_cb()
        cmg.update(ramp=RedWhiteRamp())
        cmg.apply_cb()
        self.assertEqual(len(cmg.history), 3)
        cmg.update(ramp=WhiteBlueRamp())
        cmg.apply_cb()
        self.assertEqual(len(cmg.history), 4)
        cmg.stepBack_cb()
        cmg.stepBack_cb()
        cmg.apply_cb()
        self.assertEqual(len(cmg.history), 2)
        self.assertEqual(cmg.cmapCurrent, True)
        
        
        
    def test_stepBack_Continuous(self):
        cmap = ColorMap('test', ramp=RGBRamp())
        cmg = ColorMapGUI(cmap, width=200, continuous=1)
        newRamp = RGBRamp()
        for x in range(5):
            cmg.update(ramp=newRamp)
        self.assertEqual(len(cmg.history),6)
        self.assertEqual(cmg.cmapCurrent, True)
        
        # step back with a continuous colorMapGUI.
        cmg.stepBack_cb()
        self.assertEqual(len(cmg.history),5)
        self.assertEqual(cmg.cmapCurrent, True)

        cmg.stepBack_cb()
        self.assertEqual(len(cmg.history),4)
        self.assertEqual(cmg.cmapCurrent, True)
        
        cmg.stepBack_cb()
        self.assertEqual(len(cmg.history),3)
        self.assertEqual(cmg.cmapCurrent, True)
        
        cmg.stepBack_cb()
        self.assertEqual(len(cmg.history),2)
        self.assertEqual(cmg.cmapCurrent, True)

        cmg.stepBack_cb()
        self.assertEqual(len(cmg.history),1)
        self.assertEqual(cmg.cmapCurrent, True)

        cmg.stepBack_cb()
        self.assertEqual(len(cmg.history),1)
        self.assertEqual(cmg.cmapCurrent, True)

    def test_resetComp(self):
        cmap = ColorMap('test', ramp=RGBRamp())
        cmg = ColorMapGUI(cmap, width=200, continuous=1)
        self.assertEqual(len(cmg.history), 1)

        ncm = ColorMap('rgb10', filename="Data/rgb10_map.py")
        rgb10 = ncm.ramp[:]
        ncm2 = ColorMap('rgb10T', filename='Data/rgb10_transparent_map.py')
        rgb10T = ncm2.ramp[:]

        cmg.update(ramp=rgb10T)
        self.assertEqual(len(cmg.history), 2)
        cmg.currentCanvasVar.set('Val')
        cmg.button_cb()
        # Reset the Opacity panel
        cmg.resetAll_cb #reset_cb()
        self.assertEqual(len(cmg.history), 2)

    def test_resetAll(self):
        cmap = ColorMap('test', ramp=RGBRamp())
        rgb = cmap.ramp
        cmg = ColorMapGUI(cmap, width=200, continuous=1)
        self.assertEqual(len(cmg.history), 1)
        cmg.update(ramp=RedWhiteRamp())
        cmg.update(ramp=RedWhiteBlueRamp())
        self.assertEqual(len(cmg.history),3)
        cmg.resetAll_cb()
        self.assertEqual(len(cmg.history),1)
        self.assertEqual(cmg.guiRamp, rgb)

        
if __name__ == '__main__':
    unittest.main()
##     testplus.chdir()
##     print harness
##     sys.exit( len( harness))
