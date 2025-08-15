import pandas as pd

# my data set
mds = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

mv = pd.DataFrame(mds)

print(mv)