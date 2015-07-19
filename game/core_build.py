#!/usr/bin/env python

import os
from cffi import FFI

COMPILE = True
CORE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..',
                        'core')

ffi = FFI()

if COMPILE:
    ffi.set_source(
        "_core", """
            #include "core.h"
        """,
        libraries=['run_rabbit_run'],
        library_dirs=[os.path.join(CORE_DIR, 'build')],
        include_dirs=[os.path.join(CORE_DIR, 'include')]
    )

ffi.cdef("""
    int RunCore(void);
""")

if not COMPILE:
    lib = ffi.dlopen(os.path.join(CORE_DIR, 'build', 'librun_rabbit_run.so'))

    print(lib.RunCore())

if __name__ == '__main__':
    if COMPILE:
        ffi.compile()
