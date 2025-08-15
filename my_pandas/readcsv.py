import pandas as pd

class ReadCSV:
    def __init__(self):
        self.sep = "----------------------"
        self.data = 'data/customers-100.csv'

    def ini_read(self,data):
        print(self.sep)
        return pd.read_csv(data)
    
    def set_row(self, nums):
        pd.options.display.max_rows = nums
    
    def to_str(self):
        return self.ini_read(self.data)
    
    def system_max(self):
        # check the system's maximum rows with the statements
        print(self.sep)
        return pd.options.display.max_rows
    
    def max_rows(self):
        self.set_row(9999)
        return self.ini_read(self.data)