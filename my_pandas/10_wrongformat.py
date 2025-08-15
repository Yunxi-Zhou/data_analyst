import pandas as pd

class WrongFormat:
    def __init__(self):
        self.sep = '----------------------'
        self.data = ('data/sample.csv')

    def ini_read(self,data):
        print(self.sep)
        return pd.read_csv(data)

    def to_date(self, data):
        df = self.ini_read(self.data)
        df[data] = pd.to_datetime(df[data], format='mixed')
        return df.to_string()
    
    def remove_null(self,data):
        df = self.ini_read(self.data)
        df.dropna(subset=[data], inplace=True)
        return df