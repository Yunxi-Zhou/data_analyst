import pandas as pd

class DataFrame:

    def __init__(self):
        self.sep = "----------------------"
        self.a = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
        }
    
    def ini_frame(self,data,index=None):
        print(self.sep)
        return pd.DataFrame(data, index=index)
    
    def loc_row(self, data, a):
        return self.ini_frame(data).loc[a]
    
    def load_data(self):
        return self.ini_frame(self.a)
    
    def name_index(self):
        return self.ini_frame(self.a, index = ["day1","day2","day3"])
    
    def read_file(self):
        print(self.sep)
        return pd.read_csv('data/customers-100.csv')