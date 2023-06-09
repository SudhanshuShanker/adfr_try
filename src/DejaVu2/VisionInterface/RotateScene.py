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

## Automatically adapted for numpy.oldnumeric Jul 23, 2007 by 

########################################################################
#
#    Vision Macro - Python source code - file generated by vision
#    Tuesday 28 March 2006 11:26:49 
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
# $Header: /mnt/raid/services/cvs/DejaVu2/VisionInterface/RotateScene.py,v 1.1.1.1.4.1 2017/07/13 22:20:08 annao Exp $
#
# $Id: RotateScene.py,v 1.1.1.1.4.1 2017/07/13 22:20:08 annao Exp $
#

from NetworkEditor.macros import MacroNode
class RotateScene(MacroNode):

    def __init__(self, constrkw={}, name='RotateScene', **kw):
        kw['name'] = name
        MacroNode.__init__(*(self,), **kw)

    def beforeAddingToNetwork(self, net):
        MacroNode.beforeAddingToNetwork(self, net)
        ## loading libraries ##
        from symserv.VisionInterface.SymservNodes import symlib
        net.editor.addLibraryInstance(symlib,"symserv.VisionInterface.SymservNodes", "symlib")

        from Vision.StandardNodes import stdlib
        net.editor.addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

        from DejaVu2.VisionInterface.DejaVu2Nodes import vizlib
        net.editor.addLibraryInstance(vizlib,"DejaVu2.VisionInterface.DejaVu2Nodes", "vizlib")


    def afterAddingToNetwork(self):
        from NetworkEditor.macros import MacroNode
        MacroNode.afterAddingToNetwork(self)
        ## loading libraries ##
        from symserv.VisionInterface.SymservNodes import symlib
        from Vision.StandardNodes import stdlib
        from DejaVu2.VisionInterface.DejaVu2Nodes import vizlib
        ## building macro network ##
        RotateScene_0 = self
        from traceback import print_exc

        ## loading libraries ##
        from symserv.VisionInterface.SymservNodes import symlib
        self.macroNetwork.getEditor().addLibraryInstance(symlib,"symserv.VisionInterface.SymservNodes", "symlib")

        from Vision.StandardNodes import stdlib
        self.macroNetwork.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

        from DejaVu2.VisionInterface.DejaVu2Nodes import vizlib
        self.macroNetwork.getEditor().addLibraryInstance(vizlib,"DejaVu2.VisionInterface.DejaVu2Nodes", "vizlib")

        try:
            ## saving node input Ports ##
            input_Ports_1 = self.macroNetwork.ipNode
            input_Ports_1.move(45, 17)
        except:
            print("WARNING: failed to restore MacroInputNode named input Ports in network self.macroNetwork")
            print_exc()
            input_Ports_1=None

        try:
            ## saving node output Ports ##
            output_Ports_2 = self.macroNetwork.opNode
            output_Ports_2.move(228, 460)
        except:
            print("WARNING: failed to restore MacroOutputNode named output Ports in network self.macroNetwork")
            print_exc()
            output_Ports_2=None

        try:
            ## saving node Rotate ##
            from symserv.VisionInterface.SymservNodes import SymRotNE
            Rotate_3 = SymRotNE(constrkw = {}, name='Rotate', library=symlib)
            self.macroNetwork.addNode(Rotate_3,543,101)
            Rotate_3.inputPortByName['matrices'].configure(*(), **{'color': 'cyan', 'cast': True, 'shape': 'rect'})
            Rotate_3.inputPortByName['vector'].configure(*(), **{'datatype': 'list', 'cast': True, 'shape': 'oval', 'color': 'cyan', 'height': 8})
            Rotate_3.inputPortByName['point'].configure(*(), **{'color': 'white', 'cast': True, 'shape': 'diamond'})
            Rotate_3.inputPortByName['angle'].configure(*(), **{'color': 'green', 'cast': True, 'shape': 'circle'})
            Rotate_3.inputPortByName['identity'].configure(*(), **{'color': 'yellow', 'cast': True, 'shape': 'circle'})
            Rotate_3.outputPortByName['outMatrices'].configure(*(), **{'color': 'cyan', 'shape': 'rect'})
            Rotate_3.inputPortByName['vector'].unbindWidget()
            Rotate_3.inputPortByName['angle'].widget.set(0.0, run=False)
            Rotate_3.inputPortByName['angle'].unbindWidget()
        except:
            print("WARNING: failed to restore SymRotNE named Rotate in network self.macroNetwork")
            print_exc()
            Rotate_3=None

        try:
            ## saving node One Redraw ##
            from DejaVu2.VisionInterface.DejaVu2Nodes import OneRedraw
            One_Redraw_4 = OneRedraw(constrkw = {}, name='One Redraw', library=vizlib)
            self.macroNetwork.addNode(One_Redraw_4,22,452)
            One_Redraw_4.inputPortByName['viewer'].configure(*(), **{'color': 'yellow', 'cast': True, 'shape': 'rect'})
            One_Redraw_4.inputPortByName['trigger'].configure(*(), **{'color': 'white', 'cast': True, 'shape': 'diamond'})
        except:
            print("WARNING: failed to restore OneRedraw named One Redraw in network self.macroNetwork")
            print_exc()
            One_Redraw_4=None

        try:
            ## saving node Choose Geom ##
            from DejaVu2.VisionInterface.DejaVu2Nodes import SelectGeometry
            Choose_Geom_5 = SelectGeometry(constrkw = {}, name='Choose Geom', library=vizlib)
            self.macroNetwork.addNode(Choose_Geom_5,412,220)
            Choose_Geom_5.inputPortByName['viewer'].configure(*(), **{'color': 'yellow', 'cast': True, 'shape': 'rect'})
            Choose_Geom_5.inputPortByName['geomName'].configure(*(), **{'color': 'white', 'cast': True, 'shape': 'oval'})
            Choose_Geom_5.outputPortByName['geometry'].configure(*(), **{'color': 'red', 'shape': 'rect'})
            Choose_Geom_5.inputPortByName['geomName'].widget.configure(*(), **{'autoList': False, 'choices': ('root',)})
            Choose_Geom_5.inputPortByName['geomName'].widget.set("root", run=False)
        except:
            print("WARNING: failed to restore SelectGeometry named Choose Geom in network self.macroNetwork")
            print_exc()
            Choose_Geom_5=None

        try:
            ## saving node range ##
            from Vision.StandardNodes import Range
            range_6 = Range(constrkw = {}, name='range', library=stdlib)
            self.macroNetwork.addNode(range_6,246,147)
            range_6.inputPortByName['fromInd'].configure(*(), **{'color': 'yellow', 'cast': True, 'shape': 'circle'})
            range_6.inputPortByName['toInd'].configure(*(), **{'color': 'yellow', 'cast': True, 'shape': 'circle'})
            range_6.inputPortByName['step'].configure(*(), **{'color': 'yellow', 'cast': True, 'shape': 'circle'})
            range_6.outputPortByName['data'].configure(*(), **{'color': 'cyan', 'shape': 'oval'})
            range_6.inputPortByName['toInd'].unbindWidget()
        except:
            print("WARNING: failed to restore Range named range in network self.macroNetwork")
            print_exc()
            range_6=None

        try:
            ## saving node iterate ##
            from Vision.StandardNodes import Iterate
            iterate_7 = Iterate(constrkw = {}, name='iterate', library=stdlib)
            self.macroNetwork.addNode(iterate_7,283,204)
            iterate_7.inputPortByName['listToLoopOver'].configure(*(), **{'color': 'cyan', 'cast': True, 'shape': 'oval'})
            iterate_7.outputPortByName['oneItem'].configure(*(), **{'color': 'white', 'shape': 'diamond'})
            iterate_7.outputPortByName['iter'].configure(*(), **{'color': 'yellow', 'shape': 'circle'})
            iterate_7.outputPortByName['begin'].configure(*(), **{'color': 'yellow', 'shape': 'rect'})
            iterate_7.outputPortByName['end'].configure(*(), **{'color': 'yellow', 'shape': 'rect'})
            iterate_7.outputPortByName['maxIter'].configure(*(), **{'color': 'yellow', 'shape': 'circle'})
        except:
            print("WARNING: failed to restore Iterate named iterate in network self.macroNetwork")
            print_exc()
            iterate_7=None

        try:
            ## saving node flattenRotation ##
            from Vision.StandardNodes import Generic
            flattenRotation_8 = Generic(constrkw = {}, name='flattenRotation', library=stdlib)
            self.macroNetwork.addNode(flattenRotation_8,560,200)
            flattenRotation_8.addInputPort(*(), **{'name': 'in0', 'cast': True, 'datatype': 'instancemat(0)', 'height': 8, 'width': 12, 'shape': 'rect', 'color': 'cyan'})
            flattenRotation_8.addOutputPort(*(), **{'name': 'out0', 'datatype': 'float(16)', 'height': 10, 'width': 10, 'shape': 'rect', 'color': 'white'})
            code = """def doit(self, in0):
    self.outputData(out0=in0[0].ravel())
"""
            flattenRotation_8.configure(function=code)
        except:
            print("WARNING: failed to restore Generic named flattenRotation in network self.macroNetwork")
            print_exc()
            flattenRotation_8=None

        try:
            ## saving node Pass ##
            from Vision.StandardNodes import Pass
            Pass_9 = Pass(constrkw = {}, name='Pass', library=stdlib)
            self.macroNetwork.addNode(Pass_9,333,339)
            Pass_9.inputPortByName['in1'].configure(*(), **{'color': 'white', 'cast': True, 'shape': 'diamond'})
            Pass_9.outputPortByName['out1'].configure(*(), **{'color': 'white', 'shape': 'diamond'})
            Pass_9.configure(*(), **{'specialPortsVisible': True})
        except:
            print("WARNING: failed to restore Pass named Pass in network self.macroNetwork")
            print_exc()
            Pass_9=None

        try:
            ## saving node angle ##
            from Vision.StandardNodes import DialNE
            angle_10 = DialNE(constrkw = {}, name='angle', library=stdlib)
            self.macroNetwork.addNode(angle_10,244,5)
            angle_10.inputPortByName['dial'].configure(*(), **{'color': 'green', 'cast': True, 'shape': 'circle'})
            angle_10.inputPortByName['mini'].configure(*(), **{'datatype': 'int', 'cast': True, 'shape': 'circle', 'color': 'yellow'})
            angle_10.inputPortByName['maxi'].configure(*(), **{'datatype': 'int', 'cast': True, 'shape': 'circle', 'color': 'yellow'})
            angle_10.outputPortByName['value'].configure(*(), **{'datatype': 'int', 'color': 'yellow', 'shape': 'circle'})
            angle_10.inputPortByName['dial'].widget.configure(*(), **{'type': 'int', 'oneTurn': 100.0})
            angle_10.inputPortByName['dial'].widget.set(360, run=False)
        except:
            print("WARNING: failed to restore DialNE named angle in network self.macroNetwork")
            print_exc()
            angle_10=None

        try:
            ## saving node nbSteps ##
            from Vision.StandardNodes import DialNE
            nbSteps_11 = DialNE(constrkw = {}, name='nbSteps', library=stdlib)
            self.macroNetwork.addNode(nbSteps_11,634,7)
            nbSteps_11.inputPortByName['dial'].configure(*(), **{'color': 'green', 'cast': True, 'shape': 'circle'})
            nbSteps_11.inputPortByName['mini'].configure(*(), **{'color': 'green', 'cast': True, 'shape': 'circle'})
            nbSteps_11.inputPortByName['maxi'].configure(*(), **{'color': 'green', 'cast': True, 'shape': 'circle'})
            nbSteps_11.outputPortByName['value'].configure(*(), **{'color': 'green', 'shape': 'circle'})
            nbSteps_11.inputPortByName['dial'].widget.configure(*(), **{'oneTurn': 10.0})
            nbSteps_11.inputPortByName['dial'].widget.set(1.0, run=False)
        except:
            print("WARNING: failed to restore DialNE named nbSteps in network self.macroNetwork")
            print_exc()
            nbSteps_11=None

        try:
            ## saving node select axis ##
            from DejaVu2.VisionInterface.DejaVu2Nodes import SelectAxis
            select_axis_12 = SelectAxis(constrkw = {}, name='select axis', library=stdlib)
            self.macroNetwork.addNode(select_axis_12,528,40)
            select_axis_12.inputPortByName['x-axis'].configure(*(), **{'color': 'yellow', 'cast': True, 'shape': 'rect'})
            select_axis_12.inputPortByName['y-axis'].configure(*(), **{'color': 'yellow', 'cast': True, 'shape': 'rect'})
            select_axis_12.inputPortByName['z-axis'].configure(*(), **{'color': 'yellow', 'cast': True, 'shape': 'rect'})
            select_axis_12.outputPortByName['rotationAxis'].configure(*(), **{'color': 'cyan', 'shape': 'oval'})
        except:
            print("WARNING: failed to restore SelectAxis named select axis in network self.macroNetwork")
            print_exc()
            select_axis_12=None

        try:
            ## saving node call method ##
            from Vision.StandardNodes import CallMethod
            call_method_13 = CallMethod(constrkw = {}, name='call method', library=stdlib)
            self.macroNetwork.addNode(call_method_13,412,339)
            call_method_13.inputPortByName['objects'].configure(*(), **{'datatype': 'geom', 'cast': True, 'shape': 'rect', 'color': 'red'})
            call_method_13.inputPortByName['signature'].configure(*(), **{'color': 'white', 'cast': True, 'shape': 'oval'})
            call_method_13.addInputPort(*(), **{'name': 'mat', 'cast': True, 'datatype': 'None', 'height': 8, 'width': 12, 'shape': 'diamond', 'color': 'white'})
            call_method_13.outputPortByName['objects'].configure(*(), **{'color': 'white', 'shape': 'diamond'})
            call_method_13.outputPortByName['results'].configure(*(), **{'color': 'white', 'shape': 'diamond'})
            call_method_13.inputPortByName['signature'].widget.set("ConcatRotation %mat", run=False)
            call_method_13.configure(*(), **{'specialPortsVisible': True})
        except:
            print("WARNING: failed to restore CallMethod named call method in network self.macroNetwork")
            print_exc()
            call_method_13=None

        self.macroNetwork.freeze()

        ## saving connections for network RotateScene ##
        if range_6 is not None and iterate_7 is not None:
            try:
                self.macroNetwork.connectNodes(
                    range_6, iterate_7, "data", "listToLoopOver", blocking=True)
            except:
                print("WARNING: failed to restore connection between range_6 and iterate_7 in network self.macroNetwork")
        if Rotate_3 is not None and flattenRotation_8 is not None:
            try:
                self.macroNetwork.connectNodes(
                    Rotate_3, flattenRotation_8, "outMatrices", "in0", blocking=True)
            except:
                print("WARNING: failed to restore connection between Rotate_3 and flattenRotation_8 in network self.macroNetwork")
        if iterate_7 is not None and Pass_9 is not None:
            try:
                self.macroNetwork.connectNodes(
                    iterate_7, Pass_9, "oneItem", "in1", blocking=True)
            except:
                print("WARNING: failed to restore connection between iterate_7 and Pass_9 in network self.macroNetwork")
        if angle_10 is not None and range_6 is not None:
            try:
                self.macroNetwork.connectNodes(
                    angle_10, range_6, "value", "toInd", blocking=True)
            except:
                print("WARNING: failed to restore connection between angle_10 and range_6 in network self.macroNetwork")
        if nbSteps_11 is not None and Rotate_3 is not None:
            try:
                self.macroNetwork.connectNodes(
                    nbSteps_11, Rotate_3, "value", "angle", blocking=True)
            except:
                print("WARNING: failed to restore connection between nbSteps_11 and Rotate_3 in network self.macroNetwork")
        if select_axis_12 is not None and Rotate_3 is not None:
            try:
                self.macroNetwork.connectNodes(
                    select_axis_12, Rotate_3, "rotationAxis", "vector", blocking=True)
            except:
                print("WARNING: failed to restore connection between select_axis_12 and Rotate_3 in network self.macroNetwork")
        output_Ports_2 = self.macroNetwork.opNode
        if iterate_7 is not None and output_Ports_2 is not None:
            try:
                self.macroNetwork.connectNodes(
                    iterate_7, output_Ports_2, "oneItem", "new", blocking=True)
            except:
                print("WARNING: failed to restore connection between iterate_7 and output_Ports_2 in network self.macroNetwork")
        if Choose_Geom_5 is not None and call_method_13 is not None:
            try:
                self.macroNetwork.connectNodes(
                    Choose_Geom_5, call_method_13, "geometry", "objects", blocking=True)
            except:
                print("WARNING: failed to restore connection between Choose_Geom_5 and call_method_13 in network self.macroNetwork")
        if Pass_9 is not None and call_method_13 is not None:
            try:
                self.macroNetwork.specialConnectNodes(
                    Pass_9, call_method_13, "trigger", "runNode", blocking=True)
            except:
                print("WARNING: failed to restore connection between Pass_9 and call_method_13 in network self.macroNetwork")
        if flattenRotation_8 is not None and call_method_13 is not None:
            try:
                self.macroNetwork.connectNodes(
                    flattenRotation_8, call_method_13, "out0", "mat", blocking=True)
            except:
                print("WARNING: failed to restore connection between flattenRotation_8 and call_method_13 in network self.macroNetwork")
        if call_method_13 is not None and One_Redraw_4 is not None:
            try:
                self.macroNetwork.connectNodes(
                    call_method_13, One_Redraw_4, "objects", "trigger", blocking=True)
            except:
                print("WARNING: failed to restore connection between call_method_13 and One_Redraw_4 in network self.macroNetwork")
        input_Ports_1 = self.macroNetwork.ipNode
        if input_Ports_1 is not None and One_Redraw_4 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, One_Redraw_4, "new", "viewer", blocking=True)
            except:
                print("WARNING: failed to restore connection between input_Ports_1 and One_Redraw_4 in network self.macroNetwork")
        if input_Ports_1 is not None and Choose_Geom_5 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, Choose_Geom_5, "One Redraw_viewer", "viewer", blocking=True)
            except:
                print("WARNING: failed to restore connection between input_Ports_1 and Choose_Geom_5 in network self.macroNetwork")
        self.macroNetwork.unfreeze()

        ## modifying MacroOutputNode dynamic ports
        output_Ports_2 = self.macroNetwork.opNode
        output_Ports_2.inputPorts[1].configure(singleConnection=True)

        RotateScene_0.shrink()

        ## reset modifications ##
        RotateScene_0.resetTags()
        RotateScene_0.buildOriginalList()
