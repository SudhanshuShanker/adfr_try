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
# Date: Aug 2003  Authors: Daniel Stoffler, Michel Sanner
#
#       stoffler@scripps.edu
#       sanner@scripps.edu
#
# Copyright: Daniel Stoffler, Michel Sanner, and TSRI
#
#########################################################################

import sys
ed = None

def setUp():
    global ed
    from Vision.VPE import VisualProgramingEnvironment
    ed = VisualProgramingEnvironment(name='Vision', withShell=0,)
    ed.root.update_idletasks()
    ed.configure(withThreads=0)


def tearDown():
    ed.exit_cb()
    import gc
    gc.collect()

##########################
## Helper methods
##########################

def pause(sleepTime=0.4):
    from time import sleep
    ed.master.update()
    sleep(sleepTime)

##########################
## Tests
##########################

def test_01_loadVizLib():
    from DejaVu.VisionInterface.DejaVuNodes import vizlib
    ed.addLibraryInstance(vizlib, 'DejaVu.VisionInterface.DejaVuNodes',
                          'vizlib')
    ed.root.update_idletasks()
    pause()

categories= ['Mapper', 'Geometry', 'Macro', 'Filter', 'Output', 'Input']

def categoryTest(cat):
    from DejaVu.VisionInterface.DejaVuNodes import vizlib
    ed.addLibraryInstance(vizlib, 'DejaVu.VisionInterface.DejaVuNodes',
                          'vizlib')
    ed.root.update_idletasks()
    pause()
    # test the vizlib nodes
    lib = '3D Visualization'
    libs = ed.libraries
    posx = 150
    posy = 150

    #ed.ModulePages.selectpage(lib)
    ed.root.update_idletasks()

    for node in libs[lib].libraryDescr[cat]['nodes']:
        klass = node.nodeClass
        kw = node.kw
        args = node.args
        netNode = klass(*args, **kw)
        print('testing: '+node.name) # begin node test
        #add node to canvas
        ed.currentNetwork.addNode(netNode,posx,posy)
        # show widget in node if available:
        widgetsInNode = netNode.getWidgetsForMaster('Node')
        if len( list(widgetsInNode.items()) ):
            if not netNode.isExpanded():
                netNode.toggleNodeExpand_cb()
                ed.root.update_idletasks()
            # and then hide it
            netNode.toggleNodeExpand_cb()
            ed.root.update_idletasks()

        # show widgets in param panel if available:
        widgetsInPanel = netNode.getWidgetsForMaster('ParamPanel')
        if len(list(widgetsInPanel.items())):
            netNode.paramPanel.show()
            ed.root.update_idletasks()
            #and then hide it
            netNode.paramPanel.hide()
            ed.root.update_idletasks()

        # and now delete the node
        ed.currentNetwork.deleteNodes([netNode])
        ed.root.update_idletasks()
        print('passed: '+node.name) # end node test


def test_02_MapperCategory():
    """Testing Mapper category of nodudes."""
    categoryTest("Mapper")
    
def test_03_GeometryCategory():
    """Testing Geometry category of nodudes."""
    categoryTest("Geometry")
    
def test_04_MacroCategory():
    """Testing Macro category of nodudes."""
    categoryTest("Macro")
    
def test_05_FilterCategory():
    """Testing  Filter  category of nodudes."""
    categoryTest("Filter")
    
def test_06_OutputCategory():
    """Testing Output category of nodudes."""
    categoryTest("Output")
    
def test_07_InputCategory():
    """Testing Input category of nodudes."""
    categoryTest("Input")
