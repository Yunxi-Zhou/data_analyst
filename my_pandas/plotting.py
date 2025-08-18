import pandas as pd
import matplotlib.pyplot as plt

class Plotting:
    def __init__(self):
        self.sep = '--------------------------------'
        self.data = 'data/sample2.csv'
        
    def ini_read(self,data):
        print(self.sep)
        return pd.read_csv(data)
    
    def read_csv(self):
        return self.ini_read(self.data)
    
    def return_plot(self):
        df = self.ini_read(self.data)
        df.plot()
        plt.show()