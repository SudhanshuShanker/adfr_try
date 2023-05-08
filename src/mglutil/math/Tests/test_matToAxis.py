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

from mglutil.regression import testplus
from FlexTree.FTMotions import FTMotion_RotationAboutAxis, FTMotion_Hinge
import numpy

def diff(res, expect):
    return res-expect < 1.0e-6  # close enough -> true


def rotateObject():
    from mglutil.math.rotax import rotax
    from math import sin, cos, pi, sqrt, fabs
    import random

    degtorad = pi/180.
    point1 = [random.random()*8-4, random.random()*8-4.,random.random()*10-5]
    point2 = [random.random()*8-4, random.random()*8-4.,random.random()*10-5.]
    angle  = random.random()*360.
    transf = rotax(point1, point2, angle*degtorad, transpose=1)

    from mglutil.math.rotax import mat_to_axis_angle
    vector , pp, angle = mat_to_axis_angle(transf)

    from FlexTree.FTMotions import FTMotion_Hinge
    motion = FTMotion_Hinge(axis={'vector':vector,'point':pp})
    motion.configure(angle=angle)

    m1=numpy.array(motion.getMatrix()).ravel()
    m2=transf.ravel()
    bSame = True
    for i in range(len(m1)):
        if fabs(m1[i]-m2[i]) > 1e-4:
            bSame = False
    assert (bSame, True)


def test_rotateObject():
    for i in range(10):
        rotateObject()
    

harness = testplus.TestHarness( __name__,
                              funs = testplus.testcollect( globals()),
                              )

if __name__ == '__main__':
    print(harness)
    sys.exit( len( harness))