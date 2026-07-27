import joblib
import pandas as pd


def predict_stroke():

    model = joblib.load("Models/stroke_model.pkl")

    gender = input("Enter Gender (Male/Female): ")
    age = float(input("Enter Age: "))
    hypertension = int(input("Enter Hypertension (0 = No, 1 = Yes): "))
    heart_disease = int(input("Enter Heart Disease (0 = No, 1 = Yes): "))
    ever_married = input("Enter Ever Married (Yes/No): ")
    work_type = input(
        "Enter Work Type (Private/Self-employed/Govt_job/children/Never_worked): "
    )
    residence_type = input("Enter Residence Type (Urban/Rural): ")
    avg_glucose_level = float(input("Enter Average Glucose Level: "))
    bmi = float(input("Enter BMI: "))
    smoking_status = input(
        "Enter Smoking Status (formerly smoked/never smoked/smokes/Unknown): "
    )

    user_data = pd.DataFrame([{
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "ever_married": ever_married,
        "work_type": work_type,
        "Residence_type": residence_type,
        "avg_glucose_level": avg_glucose_level,
        "bmi": bmi,
        "smoking_status": smoking_status
    }])

    prediction = model.predict(user_data)

    if prediction[0] == 1:
        print("\nPrediction: Stroke Risk Detected")
    else:
        print("\nPrediction: No Stroke Risk Detected")


predict_stroke()