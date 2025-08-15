import pandas as pd

class CleanData:
    def __init__(self):
        self.sep = '----------------------'
        self.data = 'data/sample.csv'
    
    def ini_read(self,data):
        print(self.sep)
        return pd.read_csv(data)

    def read_data(self):
        return self.ini_read(self.data)
    
    # remove all rows with NULL values
    # ex. remove 23 -> 21 22 24 25 ..
    def remove_row(self):
        return self.ini_read(self.data).dropna().to_string()
    
    def remove_inplace(self):
        df = self.ini_read(self.data)
        df.dropna(inplace=True)
        return df.to_string()

    def replace_empty(self, data):
        df = self.ini_read(self.data)
        df.fillna(data, inplace=True)
        return df
    
    def replace_mean(self, data):
        df = self.ini_read(self.data)
        x = df[data].mean()
        df.fillna({data: x}, inplace=True)
        return df
    
    def replace_median(self, data):
        df = self.ini_read(self.data)
        x = df[data].median()
        df.fillna({data: x}, inplace=True)
        return df

    # Mode = the value that appears most frequently
    def replace_mode(self, data,nums):
        df = self.ini_read(self.data)
        x = df[data].mode()[nums]
        df.fillna({data: x}, inplace=True)
        return df
    
if __name__ == '__main__':
    res = CleanData()
    print(res.read_data())
    print(res.remove_row())
    print(res.remove_inplace())
    print(res.replace_empty(130))
    print(res.replace_empty({"Calories":130}))
    print(res.replace_mean("Calories"))
    print(res.replace_median("Calories"))
    print(res.replace_mode("Calories",0))