from preprocessing import preprocess_data

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


def train_models():

    X_train, X_test, y_train, y_test = preprocess_data()


    # Logistic Regression
    logistic_model = LogisticRegression()
    logistic_model.fit(X_train, y_train)
    print("Logistic Regression Trained Successfully.")


    # Decision Tree
    decision_model = DecisionTreeClassifier()
    decision_model.fit(X_train, y_train)
    print("Decision Tree Trained Successfully.")


    # Random Forest
    random_model = RandomForestClassifier()
    random_model.fit(X_train, y_train)
    print("Random Forest Trained Successfully.")


    # KNN
    knn_model = KNeighborsClassifier()
    knn_model.fit(X_train, y_train)
    print("KNN Trained Successfully.")


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