import joblib
import pandas as pd


def predict_liver_disease():

    model = joblib.load("Models/liver_model.pkl")

    age = float(input("Enter Age: "))
    gender = input("Enter Gender (Male/Female): ")

    total_bilirubin = float(input("Enter Total Bilirubin: "))
    direct_bilirubin = float(input("Enter Direct Bilirubin: "))
    alkaline_phosphotase = float(input("Enter Alkaline Phosphotase: "))
    alamine_aminotransferase = float(input("Enter Alamine Aminotransferase: "))
    aspartate_aminotransferase = float(input("Enter Aspartate Aminotransferase: "))
    total_protiens = float(input("Enter Total Proteins: "))
    albumin = float(input("Enter Albumin: "))
    albumin_globulin_ratio = float(
        input("Enter Albumin and Globulin Ratio: ")
    )

    user_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Total_Bilirubin": total_bilirubin,
        "Direct_Bilirubin": direct_bilirubin,
        "Alkaline_Phosphotase": alkaline_phosphotase,
        "Alamine_Aminotransferase": alamine_aminotransferase,
        "Aspartate_Aminotransferase": aspartate_aminotransferase,
        "Total_Protiens": total_protiens,
        "Albumin": albumin,
        "Albumin_and_Globulin_Ratio": albumin_globulin_ratio
    }])

    prediction = model.predict(user_data)

    if prediction[0] == 1:
        print("\nPrediction: Liver Disease")
    else:
        print("\nPrediction: No Liver Disease")


predict_liver_disease()