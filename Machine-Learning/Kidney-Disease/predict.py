import joblib
import pandas as pd


def predict_kidney_disease():

    model = joblib.load("Models/kidney_model.pkl")

    age = float(input("Enter Age: "))
    bp = float(input("Enter Blood Pressure: "))
    sg = float(input("Enter Specific Gravity: "))
    al = float(input("Enter Albumin: "))
    su = float(input("Enter Sugar: "))

    rbc = input("Enter Red Blood Cells (normal/abnormal): ")
    pc = input("Enter Pus Cell (normal/abnormal): ")
    pcc = input("Enter Pus Cell Clumps (present/notpresent): ")
    ba = input("Enter Bacteria (present/notpresent): ")

    bgr = float(input("Enter Blood Glucose Random: "))
    bu = float(input("Enter Blood Urea: "))
    sc = float(input("Enter Serum Creatinine: "))
    sod = float(input("Enter Sodium: "))
    pot = float(input("Enter Potassium: "))
    hemo = float(input("Enter Hemoglobin: "))
    pcv = float(input("Enter Packed Cell Volume: "))
    wc = float(input("Enter White Blood Cell Count: "))
    rc = float(input("Enter Red Blood Cell Count: "))

    htn = input("Enter Hypertension (yes/no): ")
    dm = input("Enter Diabetes Mellitus (yes/no): ")
    cad = input("Enter Coronary Artery Disease (yes/no): ")
    appet = input("Enter Appetite (good/poor): ")
    pe = input("Enter Pedal Edema (yes/no): ")
    ane = input("Enter Anemia (yes/no): ")


    user_data = pd.DataFrame([{
        "age": age,
        "bp": bp,
        "sg": sg,
        "al": al,
        "su": su,
        "rbc": rbc,
        "pc": pc,
        "pcc": pcc,
        "ba": ba,
        "bgr": bgr,
        "bu": bu,
        "sc": sc,
        "sod": sod,
        "pot": pot,
        "hemo": hemo,
        "pcv": pcv,
        "wc": wc,
        "rc": rc,
        "htn": htn,
        "dm": dm,
        "cad": cad,
        "appet": appet,
        "pe": pe,
        "ane": ane
    }])


    prediction = model.predict(user_data)


    if prediction[0] == 1:
        print("\nPrediction: Chronic Kidney Disease")

    else:
        print("\nPrediction: No Chronic Kidney Disease")


predict_kidney_disease()