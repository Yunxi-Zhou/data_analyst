import pandas as pd

class Duplicates:
    def __init__(self):
        self.sep = '---------------------------'
        self.data = 'data/sample.csv'

    def ini_read(self,data):
        print(self.sep)
        return pd.read_csv(data)
    
    def read_csv(self):
        return self.ini_read(self.data)
    
    def dup_bool(self):
        df = self.ini_read(self.data)
        return df.duplicated()
    
    def dup_remove(self):
        df = self.ini_read(self.data)
        df.drop_duplicates(inplace=True)
        return df