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

########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Wednesday 14 December 2005 09:15:47 
#    
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Daniel Stoffler, Michel Sanner and TSRI
#   
# revision: Guillaume Vareille
#  
#########################################################################
#
# $Header: /mnt/raid/services/cvs/DejaVu2/VisionInterface/Tests/Data/parenting1_net.py,v 1.1.1.1.4.1 2017/07/13 22:20:08 annao Exp $
#
# $Id: parenting1_net.py,v 1.1.1.1.4.1 2017/07/13 22:20:08 annao Exp $
#

from traceback import print_exc

## loading libraries ##
from Vision.StandardNodes import stdlib
masterNet.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

from DejaVu.VisionInterface.DejaVuNodes import vizlib
masterNet.getEditor().addLibraryInstance(vizlib,"DejaVu.VisionInterface.DejaVuNodes", "vizlib")

try:

    ## saving node Viewer ##
    from DejaVu.VisionInterface.DejaVuNodes import Viewer
    Viewer_0 = Viewer(constrkw = {}, name='Viewer', library=vizlib)
    masterNet.addNode(Viewer_0,231,263)
except:
    print("WARNING: failed to restore Viewer named Viewer in network masterNet")
    print_exc()
    node0=None
try:

    ## saving node polygons2 ##
    from DejaVu.VisionInterface.GeometryNodes import IndexedPolygonsNE
    polygons2_1 = IndexedPolygonsNE(constrkw = {}, name='polygons2', library=vizlib)
    masterNet.addNode(polygons2_1,12,178)
    polygons2_1.getInputPortByName('name').widget.configure(*(), **{'choices': ['polygons2']})
    polygons2_1.getInputPortByName("name").widget.set("polygons2")
    polygons2_1.configure(*(), **{'expanded': True})
except:
    print("WARNING: failed to restore IndexedPolygonsNE named polygons2 in network masterNet")
    print_exc()
    node1=None
try:

    ## saving node polygons ##
    from DejaVu.VisionInterface.GeometryNodes import IndexedPolygonsNE
    polygons_2 = IndexedPolygonsNE(constrkw = {}, name='polygons', library=vizlib)
    masterNet.addNode(polygons_2,339,98)
    polygons_2.getInputPortByName('name').widget.configure(*(), **{'choices': ['polygons']})
    polygons_2.getInputPortByName("name").widget.set("polygons")
    polygons_2.configure(*(), **{'expanded': True})
except:
    print("WARNING: failed to restore IndexedPolygonsNE named polygons in network masterNet")
    print_exc()
    node2=None
try:

    ## saving node polygons1 ##
    from DejaVu.VisionInterface.GeometryNodes import IndexedPolygonsNE
    polygons1_3 = IndexedPolygonsNE(constrkw = {}, name='polygons1', library=vizlib)
    masterNet.addNode(polygons1_3,187,147)
    polygons1_3.getInputPortByName('name').widget.configure(*(), **{'choices': ['polygons1']})
    polygons1_3.getInputPortByName("name").widget.set("polygons1")
    polygons1_3.configure(*(), **{'expanded': True})
except:
    print("WARNING: failed to restore IndexedPolygonsNE named polygons1 in network masterNet")
    print_exc()
    node3=None
try:

    ## saving node polygons1 ##
    from DejaVu.VisionInterface.GeometryNodes import IndexedPolygonsNE
    polygons1_4 = IndexedPolygonsNE(constrkw = {}, name='polygons1', library=vizlib)
    masterNet.addNode(polygons1_4,429,213)
    polygons1_4.getInputPortByName('name').widget.configure(*(), **{'choices': ['polygons1']})
    polygons1_4.getInputPortByName("name").widget.set("polygons1")
    polygons1_4.configure(*(), **{'expanded': True})
except:
    print("WARNING: failed to restore IndexedPolygonsNE named polygons1 in network masterNet")
    print_exc()
    node4=None
try:

    ## saving node [[0,1,2]] ##
    from Vision.StandardNodes import Eval
    __0_1_2___5 = Eval(constrkw = {}, name='[[0,1,2]]', library=stdlib)
    masterNet.addNode(__0_1_2___5,263,10)
    __0_1_2___5.getInputPortByName("command").widget.set("[[0,1,2]]")
    __0_1_2___5.configure(*(), **{'expanded': True})
except:
    print("WARNING: failed to restore Eval named [[0,1,2]] in network masterNet")
    print_exc()
    node5=None
try:

    ## saving node [[0,0,0],[1,0,0... ##
    from Vision.StandardNodes import Eval
    __0_0_0___1_0_0____6 = Eval(constrkw = {}, name='[[0,0,0],[1,0,0...', library=stdlib)
    masterNet.addNode(__0_0_0___1_0_0____6,23,30)
    __0_0_0___1_0_0____6.getInputPortByName("command").widget.set("[[0,0,0],[1,0,0],[0,1,0.]]")
    __0_0_0___1_0_0____6.configure(*(), **{'expanded': True})
except:
    print("WARNING: failed to restore Eval named [[0,0,0],[1,0,0... in network masterNet")
    print_exc()
    node6=None
masterNet.freeze()

## saving connections for network parenting1 ##
if __0_1_2___5 is not None and polygons2_1 is not None:
    masterNet.connectNodes(
        __0_1_2___5, polygons2_1, "result", "indices", blocking=True)
if __0_1_2___5 is not None and polygons1_3 is not None:
    masterNet.connectNodes(
        __0_1_2___5, polygons1_3, "result", "indices", blocking=True)
if __0_1_2___5 is not None and polygons_2 is not None:
    masterNet.connectNodes(
        __0_1_2___5, polygons_2, "result", "indices", blocking=True)
if __0_1_2___5 is not None and polygons1_4 is not None:
    masterNet.connectNodes(
        __0_1_2___5, polygons1_4, "result", "indices", blocking=True)
if __0_0_0___1_0_0____6 is not None and polygons2_1 is not None:
    masterNet.connectNodes(
        __0_0_0___1_0_0____6, polygons2_1, "result", "coords", blocking=True)
if __0_0_0___1_0_0____6 is not None and polygons1_3 is not None:
    masterNet.connectNodes(
        __0_0_0___1_0_0____6, polygons1_3, "result", "coords", blocking=True)
if __0_0_0___1_0_0____6 is not None and polygons_2 is not None:
    masterNet.connectNodes(
        __0_0_0___1_0_0____6, polygons_2, "result", "coords", blocking=True)
if __0_0_0___1_0_0____6 is not None and polygons1_4 is not None:
    masterNet.connectNodes(
        __0_0_0___1_0_0____6, polygons1_4, "result", "coords", blocking=True)
masterNet.unfreeze()
