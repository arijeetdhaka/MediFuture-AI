import joblib
import pandas as pd


def predict_diabetes():

    model = joblib.load(
        "Models/Diabetes_model.pkl"
    )

    scaler = joblib.load(
        "Models/diabetes_scaler.pkl"
    )


    pregnancies = int(input("Enter Pregnancies : "))
    glucose = float(input("Enter Glucose : "))
    blood_pressure = float(input("Enter Blood Pressure : "))
    skin_thickness = float(input("Enter Skin Thickness : "))
    insulin = float(input("Enter Insulin : "))
    bmi = float(input("Enter BMI : "))
    diabetes_pedigree = float(
        input("Enter Diabetes Pedigree Function : ")
    )
    age = int(input("Enter Age : "))


    user_data = [[

        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age

    ]]


    user_data = scaler.transform(
        user_data
    )


    prediction = model.predict(
        user_data
    )


    if prediction[0] == 1:

        print("\nPrediction : Diabetic.")

    else:

        print("\nPrediction : Non-Diabetic.")



predict_diabetes()