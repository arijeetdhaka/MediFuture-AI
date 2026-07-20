import pandas as pd
df = pd.read_csv("Datasets/Diabetes/diabetes.csv")
print("shape of dataset:",df.shape)
print("\nfirst 5 rows:\n",df.head())
print("\nno of columns:\n",df.columns)
print("\ndatatypes of columns:\n",df.dtypes)
print("\nchecking for null values:\n",df.isnull().sum())


