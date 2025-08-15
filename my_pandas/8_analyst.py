import pandas as pd

class Analyst:
    def __init__(self):
        self.sep = '----------------------'
        self.data = 'data/customers-100.csv'
    
    def ini_csv(self,data):
        print(self.sep)
        return pd.read_csv(data)
    
    def return_head(self,nums):
        return self.ini_csv(self.data).head(nums)
    
    # return first/last 5 rows of the DataFrame --> tail()/head() no numbers input
    def return_tail(self):
        return self.ini_csv(self.data).tail()
    
    def return_info(self):
        return self.ini_csv(self.data).info()