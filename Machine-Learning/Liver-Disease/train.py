from preprocessing import preprocess_data

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


def train_models():

    X_train, X_test, y_train, y_test, preprocessor = preprocess_data()


    logistic_model = Pipeline([
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(max_iter=1000))
    ])

    logistic_model.fit(X_train, y_train)
    print("Logistic Regression trained successfully.")


    decision_model = Pipeline([
        ("preprocessor", preprocessor),
        ("model", DecisionTreeClassifier(random_state=42))
    ])

    decision_model.fit(X_train, y_train)
    print("Decision Tree trained successfully.")


    random_model = Pipeline([
        ("preprocessor", preprocessor),
        ("model", RandomForestClassifier(random_state=42))
    ])

    random_model.fit(X_train, y_train)
    print("Random Forest trained successfully.")


    knn_model = Pipeline([
        ("preprocessor", preprocessor),
        ("model", KNeighborsClassifier())
    ])

    knn_model.fit(X_train, y_train)
    print("KNN trained successfully.")


    return (
        logistic_model,
        decision_model,
        random_model,
        knn_model,
        X_test,
        y_test
    )


if __name__ == "__main__":
    train_models()