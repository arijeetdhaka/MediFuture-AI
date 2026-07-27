import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def preprocess_data():

    df = pd.read_csv(
        "Datasets/Hypertension/hypertension_dataset.csv"
    )

    # Convert target:
    # Yes = 1 (Hypertension)
    # No = 0 (No Hypertension)
    df["Has_Hypertension"] = df["Has_Hypertension"].map({
        "Yes": 1,
        "No": 0
    })

    # Separate features and target
    X = df.drop("Has_Hypertension", axis=1)
    y = df["Has_Hypertension"]

    # Numerical columns
    numeric_columns = [
        "Age",
        "Salt_Intake",
        "Stress_Score",
        "Sleep_Duration",
        "BMI"
    ]

    # Categorical columns
    categorical_columns = [
        "BP_History",
        "Medication",
        "Family_History",
        "Exercise_Level",
        "Smoking_Status"
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

    # Combine numerical and categorical preprocessing
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

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test, preprocessor