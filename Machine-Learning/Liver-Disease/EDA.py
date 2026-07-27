import pandas as pd

df = pd.read_csv(
    "Datasets/Liver-Disease/indian_liver_patient.csv"
)

print("Shape of dataset:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTarget Values:")
print(df["Dataset"].value_counts())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())