from preprocessing import preprocess_data

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


def train_models():

    X_train, X_test, y_train, y_test, scaler = preprocess_data()

    logistic_model = LogisticRegression()
    logistic_model.fit(X_train, y_train)
    print("Logistic Regression trained successfully.")


    decision_model = DecisionTreeClassifier(random_state=42)
    decision_model.fit(X_train, y_train)
    print("Decision Tree trained successfully.")


    random_model = RandomForestClassifier(random_state=42)
    random_model.fit(X_train, y_train)
    print("Random Forest trained successfully.")


    knn_model = KNeighborsClassifier()
    knn_model.fit(X_train, y_train)
    print("KNN trained successfully.")


    return (
        logistic_model,
        decision_model,
        random_model,
        knn_model,
        X_test,
        y_test,
        scaler
    )


if __name__ == "__main__":
    train_models()