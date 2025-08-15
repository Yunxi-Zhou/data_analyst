import pandas as pd

class Correlations:
    def __init__(self):
        self.sep = '-----------------------------'
        self.data = 'data/sample2.csv'
    
    def ini_read(self,data):
        print(self.sep)
        return pd.read_csv(data)
    
    def read_csv(self):
        return self.ini_read(self.data)
    
    # corr() calculates the relationship between each column in data set
    def corr_csv(self):
        df = self.ini_read(self.data)
        return df.corr()