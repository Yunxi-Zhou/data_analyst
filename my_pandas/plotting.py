import pandas as pd
import matplotlib.pyplot as plt

class Plotting:
    def __init__(self):
        self.data = 'data/sample2.csv'
        
    def ini_read(self,data):
        return pd.read_csv(data)
    
    def read_csv(self):
        return self.ini_read(self.data)
    
    def return_plot(self):
        df = self.ini_read(self.data)
        df.plot()
        plt.show()

    def scatter_plot(self,x,y):
        df = self.ini_read(self.data)
        df.plot(kind='scatter',x=x,y=y)
        plt.show()
    
    def plot_attr(self,attr,kind):
        df = self.ini_read(self.data)
        df[attr].plot(kind=kind)
        plt.title(f"{attr}({kind})")
        plt.show()