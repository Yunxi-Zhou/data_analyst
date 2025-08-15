import pandas as pd

class PdSeries:

    def __init__(self):
        self.sep = "----------------------"
        self.a = [1,7,2]
        self.b = {"day1": 420, "day2": 380, "day3": 390}
        self.c = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
        }
    
    def ini_series(self, data, index=None):
        s = pd.Series(data, index=index)
        print(self.sep)
        return s

    def series(self):
        return self.ini_series(self.a)
    
    def labels(self):
        return self.ini_series(self.a, index=["x","y","z"])
    
    def dic(self):
        return self.ini_series(self.b)
    
    def dic2(self):
        return self.ini_series(self.b, index=["day1","day2"])
    
    def multi(self):
        return self.ini_series(self.c)