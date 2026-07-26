import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def preprocess_data():

    # Load dataset
    df = pd.read_csv(
        "Datasets/Kidney-Disease/kidney_disease.csv"
    )

    # Remove ID because it is not a medical feature
    if "id" in df.columns:
        df = df.drop("id", axis=1)


    # Clean spaces and tabs from text columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()


    # Replace ? with missing value
    df = df.replace("?", pd.NA)


    # -------------------------
    # TARGET CLEANING
    # -------------------------

    df["classification"] = (
        df["classification"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # ckd = 1
    # notckd = 0
    df["classification"] = df["classification"].map({
        "ckd": 1,
        "notckd": 0
    })

    # Remove rows having invalid/missing target
    df = df.dropna(subset=["classification"])

    # Force target to integer
    df["classification"] = df["classification"].astype("int64")


    # Separate features and target
    X = df.drop("classification", axis=1)

    y = df["classification"]


    # Numerical columns
    numeric_columns = [
        "age",
        "bp",
        "sg",
        "al",
        "su",
        "bgr",
        "bu",
        "sc",
        "sod",
        "pot",
        "hemo",
        "pcv",
        "wc",
        "rc"
    ]


    # Convert numerical columns to actual numbers
    for column in numeric_columns:

        X[column] = pd.to_numeric(
            X[column],
            errors="coerce"
        )


    # Everything else is categorical
    categorical_columns = [
        column
        for column in X.columns
        if column not in numeric_columns
    ]


    # Numerical preprocessing
    numeric_pipeline = Pipeline([
        (
            "imputer",
            SimpleImputer(strategy="median")
        ),
        (
            "scaler",
            StandardScaler()
        )
    ])


    # Categorical preprocessing
    categorical_pipeline = Pipeline([
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "encoder",
            OneHotEncoder(handle_unknown="ignore")
        )
    ])


    # Apply different preprocessing to
    # numerical and categorical columns
    preprocessor = ColumnTransformer([
        (
            "numeric",
            numeric_pipeline,
            numeric_columns
        ),
        (
            "categorical",
            categorical_pipeline,
            categorical_columns
        )
    ])


    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )


    # Temporary checks
    print("Target values:", y.unique())
    print("Target dtype:", y.dtype)

    print("y_train values:", y_train.unique())
    print("y_train dtype:", y_train.dtype)


    return (
        X_train,
        X_test,
        y_train,
        y_test,
        preprocessor
    )