import numpy as np

class BaseNumpy:
    def __init__(self):
        self.sep = '='*22
    
    def ini_np(self,arr=None,ndmin=None,dtype=None,return_print=True,return_dtype=False,return_arr=False):
        if ndmin is None and dtype is None:
            a = np.array(arr)
        elif ndmin is None:
            a = np.array(arr, dtype=dtype)
        elif dtype is None:
            a = np.array(arr, ndmin=ndmin)
        else:
            a = np.array(arr, ndmin=ndmin, dtype=dtype)
        #
        dt = np.asarray(arr).dtype
        kind = dt.kind
        itemsize = dt.itemsize
        byteorder = dt.byteorder

        if byteorder == '<':
            endian_txt = "little-endian"
        elif byteorder == '>':
            endian_txt = "big-endian"
        elif byteorder == '=':
            endian_txt = "system default endianness"
        elif byteorder == '|':
            endian_txt = "not applicable"
        else:
            endian_txt = "not applicable"

        if kind == 'i':
            tname = f"signed integer (int{itemsize*8})"
        elif kind == 'u':
            tname = f"unsigned integer (uint{itemsize*8})"
        elif kind == 'f':
            tname = f"floating point (float{itemsize*8})"
        elif kind == 'c':
            tname = f"complex number (complex{itemsize*8})"
        elif kind == 'b':
            tname = "boolean"
        elif kind == 'S':
            tname = f"byte string (aSCII, length={itemsize})"
        elif kind == 'U':
            tname = f"Unicode string (max length={itemsize // 4})"
        elif kind == 'O':
            tname = "Python object"
        else:
            tname = f"unknown type (kind='{kind}')"
        
        explain = f"{dt} -> {tname}, {endian_txt}, {itemsize} bytes per element"
        #
        if return_print:
            print(self.sep)
            print('Data of array:')
            print(a)
            print(f'Dim of array: {a.ndim}')
            print(f'Shape of array: {a.shape}')
        
        if return_dtype:
            print(f'Type of array: {np.array(a).dtype}')
            print(explain)
        
        if return_arr:
            return a