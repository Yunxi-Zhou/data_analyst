from my_numpy.basenumpy import BaseNumpy

class ArrayShape(BaseNumpy):
    def __init__(self,arr=None,ndmin=None):
        super().__init__()
        self.arr = arr
        self.ndmin = ndmin

    def return_shape(self):
        return self.ini_np(arr=self.arr,ndmin=self.ndmin)
    
    def return_reshape(self,*shape):
        arr = self.ini_np(arr=self.arr,return_print=False,return_arr=True)
        newarr = arr.reshape(*shape)
        return self.ini_np(arr=newarr)