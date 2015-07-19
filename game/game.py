import os
from _core import ffi, lib

SHADER_PATH = os.path.abspath(os.path.join('..', 'shaders', 'simple'))

lib.RunCore(SHADER_PATH.encode('utf-8'))
