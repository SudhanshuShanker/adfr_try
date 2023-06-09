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
## Copyright (c) MGL TSRI 2016
##
################################################################################

import sys
from mglutil.regression import testplus

def setUpSuite():
    from geomutils import efitlib
def test_lib():
    from geomutils import efitlib
    ellipse = efitlib.ellipsoid()
    ellipseInfo = efitlib.efit_info()
    from .Data.crn_coords import crn_coords
    ell_scale = 1.0  # 0.0 or belove defaults to 1.0
    cov_scale= 1.75  # 0.0 or smaller defaults to 1.75
    efitlib.fitEllipse(crn_coords, ell_scale, cov_scale, ellipseInfo, ellipse)

    print('center:', ellipse.getPosition())
    print('scaling:', ellipse.getAxis())
    print('orientation', ellipse.getOrientation())

    ellipse = efitlib.ellipsoid()
    ellipseInfo = efitlib.efit_info()
    from .Data.cv_coords import cv_coords
    efitlib.fitEllipse(cv_coords, ell_scale, cov_scale, ellipseInfo, ellipse)

    ## print 'weightflag:', ellipseInfo.weightflag
    ## print 'covarflag:', ellipseInfo.covarflag
    ## print 'volumeflag:', ellipseInfo.volumeflag
    ## print 'matrixflag:', ellipseInfo.matrixflag
    ## print 'nocenterflag:', ellipseInfo.nocenterflag
    ## print 'noscaleflag:', ellipseInfo.noscaleflag
    ## print 'nosortflag:', ellipseInfo.nosortflag
    ## print 'count:', ellipseInfo.count
    ## print 'cov_scale:', ellipseInfo.cov_scale
    ## print 'ell_scale:', ellipseInfo.ell_scale

    print('center:', ellipse.getPosition())
    print('scaling:', ellipse.getAxis())
    print('orientation', ellipse.getOrientation())

    vec = [.28, 0.89, 1.5]
    vec1=efitlib.vec_normalize(vec)
    print("vector:", vec)
    print("normalized vector:", vec1)
    

if __name__ == '__main__':
    testplus.chdir()
    harness = testplus.TestHarness( __name__,
                                connect = (setUpSuite, (), {}),
                                funs = testplus.testcollect( globals()),
                                )
    print(harness)
    sys.exit( len( harness))
