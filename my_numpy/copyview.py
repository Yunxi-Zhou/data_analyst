import numpy as np
from my_numpy.basenumpy import BaseNumpy

class CopyView(BaseNumpy):
    def __init__(self,arr=None):
        super().__init__()
        self.arr = arr
    
    def return_copy(self):
        arr = self.ini_np(self.arr,return_print=False,return_arr=True)
        arr_copy = arr.copy()
        arr_copy[0] = 42
        return self.ini_np(arr), self.ini_np(arr_copy)

    def return_view(self,an=None,cn=None,change_arr=False,change_view=False):
        arr = self.ini_np(self.arr,return_print=False,return_arr=True)
        arr_view = arr.view()
        if change_arr:
            arr[an] = cn
        if change_view:
            arr_view[an] = cn
        return self.ini_np(arr), self.ini_np(arr_view)
    
    # copies owns the data, and views does not own the data
    # attribute base: return None if the array owns the data
    # means copy return None and view return base
    def return_compare(self):
        arr = self.ini_np(self.arr,return_print=False,return_arr=True)
        arr_copy = arr.copy()
        arr_view = arr.view()
        return self.ini_np(arr_copy.base), self.ini_np(arr_view.base)