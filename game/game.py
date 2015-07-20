import os
from _core import ffi, lib

RESOURCE_PATH = os.path.join('..', 'resources')
SHADER_PATH = os.path.abspath(os.path.join(RESOURCE_PATH, 'shaders', 'simple'))
IMAGE_PATH = os.path.abspath(os.path.join(RESOURCE_PATH, 'images', 'uvtemplate.dds'))

lib.RunCore(SHADER_PATH.encode('utf-8'), IMAGE_PATH.encode('utf-8'))
