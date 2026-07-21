import pandas as pd
df = pd.read_csv("Datasets/Diabetes/diabetes.csv")
print("shape of dataset:",df.shape)
print("\nfirst 5 rows:\n",df.head())
print("\nno of columns:\n",df.columns)
print("\ndatatypes of columns:\n",df.dtypes)
print("\nchecking for null values:\n",df.isnull().sum())
print("\nchecking for duplicate values:\n",df.duplicated().sum())
print("\nstatistics of dataset:\n",df.describe())
print("\nPercentage Distribution of target variable:\n")
print(df["Outcome"].value_counts(normalize=True)*100)
columns = ["Glucose",
           "BloodPressure",
           "SkinThickness",
           "Insulin",
           "BMI"]

print("\nPercentage of Zero Values:\n")

for column in columns:
    zero_percentage = ((df[column] == 0).sum()/len(df))*100

    print(f"{column} : {zero_percentage:.2f}%")

#correlation analysis
print("\nCorrelation Analysis:\n")
print(df.corr())

