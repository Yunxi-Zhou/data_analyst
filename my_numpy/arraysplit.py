import pandas as pd
from my_numpy.basenumpy import BaseNumpy

class ArraySplit(BaseNumpy):
    def __init__(self,arr):
        super().__init__()
        self.arr = arr
