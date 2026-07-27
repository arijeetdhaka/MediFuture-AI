import joblib

from evaluate import evaluate_models


def save_best_model():

    best_model = evaluate_models()

    joblib.dump(
        best_model,
        "Models/hypertension_model.pkl"
    )

    print("\nHypertension Model Saved Successfully.")


save_best_model()