import ctypes
from ctypes import *

i=c_int(99)
pi=pointer(i)
pi.contents=i
print(pi.contents)