def calculate_health_score(risk_score):

    health_score = 100 - risk_score

    if health_score < 0:
        health_score = 0

    if health_score >= 80:
        status = "Excellent"

    elif health_score >= 60:
        status = "Good"

    elif health_score >= 40:
        status = "Moderate"

    else:
        status = "Poor"

    return health_score, status