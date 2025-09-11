import numpy as np
from my_numpy.basenumpy import BaseNumpy

class ArrayIterate(BaseNumpy):
    def __init__(self,arr=None):
        super().__init__()
        self.arr = arr
    
    def return_1d(self):
        self.ini_np(self.arr)
        for x in self.arr:
            print(x)
    
    def return_2d(self):
        self.ini_np(self.arr)
        for x in self.arr:
            print(x)
            for y in x:
                print(y)

    def return_3d(self):
        self.ini_np(self.arr)
        for x in self.arr:
            print(x)
            for y in x:
                print(y)
                for z in y:
                    print(z)
    
    # advanced iterations
    def return_nditer(self,slice_obj=None,flags=None,op_dtypes=None):
        arr = self.ini_np(self.arr,return_arr=True)
        if slice_obj is not None:
            arr = arr[slice_obj]
        for x in np.nditer(arr,flags=flags,op_dtypes=op_dtypes):
            print(x)
    
    # return index of the element while iterating
    def return_nd(self):
        arr = self.ini_np(self.arr,return_arr=True)
        for idx, x in np.ndenumerate(arr):
            print(idx, x)