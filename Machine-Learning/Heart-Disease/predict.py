import joblib


def predict_heart_disease():

    model = joblib.load("Models/heart_model.pkl")
    scaler = joblib.load("Models/heart_scaler.pkl")

    age = float(input("Enter Age: "))
    sex = float(input("Enter Sex (1 = Male, 0 = Female): "))
    cp = float(input("Enter Chest Pain Type: "))
    trestbps = float(input("Enter Resting Blood Pressure: "))
    chol = float(input("Enter Cholesterol: "))
    fbs = float(input("Enter Fasting Blood Sugar: "))
    restecg = float(input("Enter Resting ECG: "))
    thalach = float(input("Enter Maximum Heart Rate: "))
    exang = float(input("Enter Exercise Induced Angina: "))
    oldpeak = float(input("Enter Oldpeak: "))
    slope = float(input("Enter Slope: "))
    ca = float(input("Enter Number of Major Vessels: "))
    thal = float(input("Enter Thal: "))

    user_data = [[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]]

    scaled_data = scaler.transform(user_data)

    prediction = model.predict(scaled_data)

    if prediction[0] == 1:
        print("\nPrediction: Heart Disease")
    else:
        print("\nPrediction: No Heart Disease")


predict_heart_disease()