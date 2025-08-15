import pandas as pd

class FixData:
    def __init__(self):
        self.sep = '-----------------------------'
        self.data = 'data/sample.csv'
    
    def ini_read(self,data):
        print(self.sep)
        return pd.read_csv(data)
    
    def read_csv(self):
        return self.ini_read(self.data)
    
    def replace_value(self,row:int,attributes:str,value):
        df = self.ini_read(self.data)
        df.loc[row,attributes] = value
        return df
    
    def replace_loop(self,attributes:str,value:int):
        df = self.ini_read(self.data)
        for x in df.index:
            if df.loc[x, attributes] > value:
                df.loc[x, attributes] = value
        return df

    def remove_row(self,attributes:str,value:int):
        df = self.ini_read(self.data)
        for x in df.index:
            if df.loc[x, attributes] > value:
                df.drop(x, inplace=True)
        return df