def calculate_future_risk(
    diabetes,
    heart,
    kidney,
    liver,
    stroke,
    hypertension
):

    risk_score = 0
    risks = []

    if diabetes == 1:
        risk_score += 20
        risks.append("Higher risk of Kidney Disease")
        risks.append("Higher risk of Heart Disease")
        risks.append("Higher risk of Stroke")

    if hypertension == 1:
        risk_score += 20
        risks.append("Higher risk of Heart Disease")
        risks.append("Higher risk of Kidney Disease")
        risks.append("Higher risk of Stroke")

    if heart == 1:
        risk_score += 15
        risks.append("Higher risk of Stroke")

    if kidney == 1:
        risk_score += 15
        risks.append("Higher risk of Heart Disease")

    if liver == 1:
        risk_score += 10
        risks.append("Liver health requires monitoring")

    if stroke == 1:
        risk_score += 20
        risks.append("Cardiovascular health requires monitoring")

    risks = list(set(risks))

    if risk_score >= 60:
        level = "HIGH"

    elif risk_score >= 30:
        level = "MODERATE"

    else:
        level = "LOW"

    return risk_score, level, risks