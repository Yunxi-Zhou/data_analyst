import numpy as np

class NdArrays:
    def __init__(self):
        self.sep = '----------------'

    def array_info(self,arr,ndmin=None):
        print(self.sep)
        arr_obj = np.array(arr) if ndmin is None else np.array(arr,ndmin=ndmin)
        print(arr_obj)
        print(f'dim: {arr_obj.ndim}')
        return arr_obj, arr_obj.ndim
    
    def return_index(self,arr):
        print(f"index is {arr}")

    def return_slice(self,arr):
        print(f"Slice element is {arr}")