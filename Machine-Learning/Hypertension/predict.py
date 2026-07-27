import joblib
import pandas as pd


def predict_hypertension():

    model = joblib.load(
        "Models/hypertension_model.pkl"
    )

    age = float(input("Enter Age: "))
    salt_intake = float(input("Enter Salt Intake: "))
    stress_score = float(input("Enter Stress Score: "))
    sleep_duration = float(input("Enter Sleep Duration: "))
    bmi = float(input("Enter BMI: "))

    bp_history = input("Enter BP History: ")
    medication = input("Enter Medication: ")
    family_history = input("Enter Family History: ")
    exercise_level = input("Enter Exercise Level: ")
    smoking_status = input("Enter Smoking Status: ")


    user_data = pd.DataFrame([{
        "Age": age,
        "Salt_Intake": salt_intake,
        "Stress_Score": stress_score,
        "Sleep_Duration": sleep_duration,
        "BMI": bmi,
        "BP_History": bp_history,
        "Medication": medication,
        "Family_History": family_history,
        "Exercise_Level": exercise_level,
        "Smoking_Status": smoking_status
    }])


    prediction = model.predict(user_data)


    if prediction[0] == 1:
        print("\nPrediction: Hypertension Risk Detected")

    else:
        print("\nPrediction: No Hypertension Risk Detected")


predict_hypertension()