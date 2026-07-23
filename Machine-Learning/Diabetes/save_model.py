import joblib

from evaluate import evaluate_models


def save_best_model():

    best_model, X_test, y_test,scaler = evaluate_models()

    joblib.dump(
        best_model,
        "Models/Diabetes_model.pkl"
    )

    print("\nBest Model Saved Successfully.")
    joblib.dump(
        scaler,
        "Models/diabetes_scaler.pkl"
    )
    print("\nScaler Saved Successfully.")

save_best_model()