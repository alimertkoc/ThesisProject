"""
Adding headers to dataset.
Headers are important to point to the correct columns when processing data.
"""

import pandas as pd

df = pd.read_csv("carinfo.csv", header=None)
df.to_csv("CarDataset.csv", header=["model", "year", "fuel", "transmission", "mileage", "hp", "engineSize", "price"], index=False)
