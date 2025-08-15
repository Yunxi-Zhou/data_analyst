import pandas as pd

class ReadJson:
    def __init__(self):
        self.sep = "----------------------"
        self.customers = 'data/customers.json'
        # JSON objects have the same format as Python dictionaries
        self.data = {
            "Duration":{
                "0":60,
                "1":60,
                "2":60,
                "3":45,
                "4":45,
                "5":60
            },
            "Pulse":{
                "0":110,
                "1":117,
                "2":103,
                "3":109,
                "4":117,
                "5":102
            },
            "Maxpulse":{
                "0":130,
                "1":145,
                "2":135,
                "3":175,
                "4":148,
                "5":127
            },
            "Calories":{
                "0":409,
                "1":479,
                "2":340,
                "3":282,
                "4":406,
                "5":300
            }
        }

    def ini_json(self,data):
        print(self.sep)
        return pd.read_json(data)

    def to_str(self):
        return self.ini_json(self.customers)
    
    def entire_str(self):
        return self.ini_json(self.customers).to_string()
    
    def json_data(self,data):
        print(self.sep)
        return pd.DataFrame(data)