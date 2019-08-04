from ctypes import *

class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]

go_library = windll.LoadLibrary("test-windows.dll")
go_library.Dump.argtypes = [GoString]
go_library.Dump.restype = c_char_p

if __name__ == "__main__":
    go_library.Dump(GoString(b"test", 4))