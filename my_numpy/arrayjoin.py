import numpy as np
from my_numpy.basenumpy import BaseNumpy

class ArrayJoin(BaseNumpy):
    def __init__(self,arr1=None,arr2=None):
        super().__init__()
        self.sep = '='*22
        self.arr1 = arr1
        self.arr2 = arr2
    
    def init_np(self):
        arr1 = self.ini_np(self.arr1, return_print=False, return_arr=True)
        arr2 = self.ini_np(self.arr2, return_print=False, return_arr=True)
        print(self.sep)
        return arr1, arr2
    
    # join arrays by axes by linear al
    def return_con(self,axis=0):
        arr1, arr2 = self.init_np()
        arr = np.concatenate((arr1,arr2),axis=axis)
        print(arr)

    # stack() is also join arrays along a *new* axis
    # if axis is not explicitly passed it is taken as 0 axis = none means axis = 0
    def return_stack(self,axis=0):
        arr1, arr2 = self.init_np()
        arr = np.stack((arr1,arr2),axis=axis)
        print(arr)
    
    # hstack(): stack along rows
    def return_hstack(self):
        arr1, arr2 = self.init_np()
        arr = np.hstack((arr1,arr2))
        print(arr)

    # vstack(): stack along columns
    def return_vstack(self):
        arr1, arr2 = self.init_np()
        arr = np.vstack((arr1,arr2))
        print(arr)

    # dstack(): stack along height, which is the same as the depth
    def return_dstack(self):
        arr1, arr2 = self.init_np()
        arr = np.dstack((arr1,arr2))
        print(arr)