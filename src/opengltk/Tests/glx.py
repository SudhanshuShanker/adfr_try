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

#does not work: GLX_XXX (like GLX_RGBA) are not exposed (GL/glxtokens.h)
# Red Book 2d ed. p. 476

if __name__ == '__main__':
    import sys
    sys.path.insert(0, '../../')
    from opengltk.extent import _glxlib
    from inspect import currentframe

    dpy = _glxlib.glXOpenDisplay()
    print(('-->', currentframe().f_lineno))
    #dpy = _glxlib.glxGetCurrentDisplay()
    screen = 0 # _glxlib.glxDefaultScreen( dpy)
    print(('-->', currentframe().f_lineno))
    vi = _glxlib.glChooseVisual( dpy, screen,
                           [_glxlib.GLX_RGBA,
                            (_glxlib.GLX_RED_SIZE, 1),
                            (_glxlib.GLX_GREEN_SIZE, 1),
                            (_glxlib.GLX_BLUE_SIZE, 1),
                            ])
    if vi:
        swap_flag = 0
    else:
        swap_flag = 1
        vi = _glxlib.glxChooseVisual( dpy, screen,
                               [_glxlib.GLX_RGBA, _glxlib.GLX_DOUBLE_BUFFER,
                                (_glxlib.GLX_GLXLIB_RED_SIZE, 1),
                                (_glxlib.GLX_GREEN_SIZE, 1),
                                (_glxlib.GLX_BLUE_SIZE, 1),
                                ])
    cx = _glxlib.glxCreateContext( dpy, vi, _glxlib.GLXContext_Null, 1)

    print('some more X functions are missing to go further...')
    print('see source in Red Book')
    
    _glxlib.glxXCloseDisplay( dpy)



