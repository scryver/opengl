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
            #include "cwrapper.h"
        """,
        libraries=['run_rabbit_run'],
        library_dirs=[os.path.join(CORE_DIR, 'build')],
        include_dirs=[os.path.join(CORE_DIR, 'include')]
    )

ffi.cdef("""
    typedef struct Core Core;

    Core* NewCore(void);
    void Core_Init(Core *c, const char *shaderPath, const char *imagePath);
    void Core_Run(Core *c);
    void DeleteCore(Core *c);
""")

if not COMPILE:
    lib = ffi.dlopen(os.path.join(CORE_DIR, 'build', 'librun_rabbit_run.so'))

    print(lib.RunCore())

if __name__ == '__main__':
    if COMPILE:
        ffi.compile()
