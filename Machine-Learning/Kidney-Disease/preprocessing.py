import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocess_data():

    df = pd.read_csv("Datasets/Kidney-Disease/kidney_disease.csv")

    # Remove ID column
    if "id" in df.columns:
        df = df.drop("id", axis=1)


    # Clean text values
    df = df.replace({
        "\t?": pd.NA,
        "?": pd.NA,
        "\tno": "no",
        "\tyes": "yes",
        " yes": "yes",
        "\tnotckd": "notckd",
        "ckd\t": "ckd"
    })


    # Convert target into numbers
    df["classification"] = df["classification"].replace({
        "ckd": 1,
        "notckd": 0
    })


    # Separate features and target
    X = df.drop("classification", axis=1)

    y = df["classification"]


    # Convert categorical columns into numbers
    X = pd.get_dummies(X, drop_first=True)


    # Convert everything to numeric
    X = X.apply(pd.to_numeric, errors="coerce")


    # Fill missing values using median
    X = X.fillna(X.median())


    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )


    # Scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)

    X_test = scaler.transform(X_test)


    return X_train, X_test, y_train, y_test, scaler