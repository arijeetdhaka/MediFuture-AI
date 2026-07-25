import joblib

from evaluate import evaluate_models


def save_best_model():

    best_model, X_test, y_test, scaler = evaluate_models()

    joblib.dump(
        best_model,
        "Models/heart_model.pkl"
    )

    joblib.dump(
        scaler,
        "Models/heart_scaler.pkl"
    )

    print("\nHeart Disease Model Saved Successfully.")
    print("Heart Disease Scaler Saved Successfully.")


save_best_model()