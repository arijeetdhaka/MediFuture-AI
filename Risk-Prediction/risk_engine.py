def calculate_future_risk(
    diabetes,
    heart,
    kidney,
    liver,
    stroke,
    hypertension
):

    risks = []

    if diabetes == 1:
        risks.append("Increased Kidney Disease Risk")
        risks.append("Increased Heart Disease Risk")
        risks.append("Increased Stroke Risk")

    if hypertension == 1:
        risks.append("Increased Heart Disease Risk")
        risks.append("Increased Kidney Disease Risk")
        risks.append("Increased Stroke Risk")

    if heart == 1:
        risks.append("Increased Stroke Risk")

    if kidney == 1:
        risks.append("Increased Heart Disease Risk")

    if liver == 1:
        risks.append("Liver Health Requires Attention")

    if stroke == 1:
        risks.append("Cardiovascular Health Requires Attention")

    risks = list(set(risks))

    return risks