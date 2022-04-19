import pandas as pd
import csv

df = pd.read_csv("carinfo.csv", header=None)

print(df)

df.to_csv("example.csv", header=["model", "year", "fuel", "transmission", "mileage", "hp", "engineSize", "price"], index=False)
