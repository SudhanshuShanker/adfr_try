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
# Date: Dec 2005  Authors: Guillaume Vareille, Michel Sanner
#
#       vareille@scripps.edu
#       sanner@scripps.edu
#
# Copyright: Guillaume Vareille, Michel Sanner, and TSRI
#
#############################################################################
#
# $Header: /mnt/raid/services/cvs/DejaVu2/VisionInterface/Tests/test_parentingGeom.py,v 1.1.1.1.4.1 2017/07/13 22:20:08 annao Exp $
#
# $Id: test_parentingGeom.py,v 1.1.1.1.4.1 2017/07/13 22:20:08 annao Exp $
#

import sys
ed = None

def setUp():
    global ed
    from Vision.VPE import VisualProgramingEnvironment
    ed = VisualProgramingEnvironment(name='Vision', withShell=0,)
    from DejaVu.VisionInterface.DejaVuNodes import vizlib
    ed.addLibraryInstance(vizlib, 'DejaVu.VisionInterface.DejaVuNodes',
                          'vizlib')
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

#===============================================================================
#this concerns the rethinking of IndexedPolygonsNE
#=============================================================================
def test_01_connect_one_geometry_node():
    # creat a connection form polygon 1 to Viewer and maek sure geom is added
    ed.loadNetwork('Data/parenting1_net.py')
    net = ed.currentNetwork
    net.runOnNewData.value = True
    net.run()
    polNode = net.getNodeByName('polygons1')[0]
    viewer = net.getNodeByName('Viewer')[0]
    net.connectNodes(polNode, viewer)
    g = polNode.geom()
    assert g.parent == viewer.vi.rootObject    
    assert viewer.vi.rootObject.children[-1] == g
    assert viewer.vi.GUI.tvolist.objToNode[g].parent.name == \
                                            viewer.vi.rootObject.name
    assert viewer.vi.GUI.tvolist.objToNode[g].name == g.name
    assert g.node().getInputPortByName('geoms').widget.get() == g.name
    assert g.node().name == g.name
    ed.deleteNetwork(net)
    
def test_02_addSecondGeomWithSameName():
    # start from end of test_01 and connect polyg
    ed.loadNetwork('Data/parenting1_net.py')
    net = ed.currentNetwork
    net.runOnNewData.value = True
    net.run()
    polNode1, polNode2 = net.getNodeByName('polygons1')
    viewer = net.getNodeByName('Viewer')[0]
    net.connectNodes(polNode1, viewer)
    net.connectNodes(polNode2, viewer)
    g2 = polNode2.geom()
    assert g2.parent == viewer.vi.rootObject
    assert viewer.vi.rootObject.children[-1] == g2
    assert viewer.vi.GUI.tvolist.objToNode[g2].parent.name == viewer.vi.rootObject.name
    assert viewer.vi.GUI.tvolist.objToNode[g2].name == g2.name
    assert g2.node().getInputPortByName('geoms').widget.get() == g2.name
    assert g2.node().name == g2.name
    assert polNode1.geom().name != g2.name
    ed.deleteNetwork(net)

def test_03_parentPolygon():
    # start from end of test_02 and parent polyg before running
    ed.loadNetwork('Data/parenting1_net.py')
    net = ed.currentNetwork
    polNode1, polNode2 = net.getNodeByName('polygons1')
    viewer = net.getNodeByName('Viewer')[0]
    net.connectNodes(polNode1, viewer)
    net.connectNodes(polNode2, viewer)
    net.connectNodes(polNode1, polNode2, portNode2 ='parent',
                     doNotSchedule=True, doNotCb=True)
    #import pdb;pdb.set_trace()
    net.run()
    g1 = polNode1.geom()
    g2 = polNode2.geom()
    assert g2.parent == g1
    assert g2 in g1.children
    assert viewer.vi.GUI.tvolist.objToNode[g1].parent.name == \
                                        viewer.vi.rootObject.name
    assert viewer.vi.GUI.tvolist.objToNode[g2].parent.name == g1.name
    ed.deleteNetwork(net)

def test_04_reparentPolygon():
    # start from end of test_02 and reparent polyg after running
    ed.loadNetwork('Data/parenting1_net.py')
    net = ed.currentNetwork
    net.runOnNewData.value = True
    net.run()
    polNode1, polNode2 = net.getNodeByName('polygons1')
    viewer = net.getNodeByName('Viewer')[0]
    net.connectNodes(polNode1, viewer)
    net.connectNodes(polNode2, viewer)
    net.connectNodes(polNode1, polNode2, portNode2 ='parent')
    g1 = polNode1.geom()
    g2 = polNode2.geom()
    assert g2.parent == g1
    assert g2 in g1.children
    assert viewer.vi.GUI.tvolist.objToNode[g1].parent.name == \
                                        viewer.vi.rootObject.name
    assert viewer.vi.GUI.tvolist.objToNode[g2].parent.name == g1.name
    ed.deleteNetwork(net)

def test_05_parentMacro():
    # start from here
    ed.loadNetwork('Data/parentsAndMacro_net.py')
    net = ed.currentNetwork
    net.run()
    viewer = net.getNodeByName('Viewer')[0]
    indpol2 =viewer.vi.FindObjectByName('|indpol1|2|indpol2')
    assert indpol2 is not None
    ed.deleteNetwork(net)
#=============================================================================
