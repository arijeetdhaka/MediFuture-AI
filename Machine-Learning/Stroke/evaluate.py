from train import train_models

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


def evaluate_models():

    (
        logistic_model,
        decision_model,
        random_model,
        knn_model,
        X_test,
        y_test
    ) = train_models()


    # Logistic Regression

    logistic_prediction = logistic_model.predict(X_test)

    logistic_accuracy = accuracy_score(y_test, logistic_prediction)
    logistic_precision = precision_score(y_test, logistic_prediction)
    logistic_recall = recall_score(y_test, logistic_prediction)
    logistic_f1 = f1_score(y_test, logistic_prediction)

    print("\n========== Logistic Regression ==========")
    print("Accuracy :", logistic_accuracy)
    print("Precision :", logistic_precision)
    print("Recall :", logistic_recall)
    print("F1 Score :", logistic_f1)
    print("Confusion Matrix :")
    print(confusion_matrix(y_test, logistic_prediction))


    # Decision Tree

    decision_prediction = decision_model.predict(X_test)

    decision_accuracy = accuracy_score(y_test, decision_prediction)
    decision_precision = precision_score(y_test, decision_prediction)
    decision_recall = recall_score(y_test, decision_prediction)
    decision_f1 = f1_score(y_test, decision_prediction)

    print("\n========== Decision Tree ==========")
    print("Accuracy :", decision_accuracy)
    print("Precision :", decision_precision)
    print("Recall :", decision_recall)
    print("F1 Score :", decision_f1)
    print("Confusion Matrix :")
    print(confusion_matrix(y_test, decision_prediction))


    # Random Forest

    random_prediction = random_model.predict(X_test)

    random_accuracy = accuracy_score(y_test, random_prediction)
    random_precision = precision_score(y_test, random_prediction)
    random_recall = recall_score(y_test, random_prediction)
    random_f1 = f1_score(y_test, random_prediction)

    print("\n========== Random Forest ==========")
    print("Accuracy :", random_accuracy)
    print("Precision :", random_precision)
    print("Recall :", random_recall)
    print("F1 Score :", random_f1)
    print("Confusion Matrix :")
    print(confusion_matrix(y_test, random_prediction))


    # KNN

    knn_prediction = knn_model.predict(X_test)

    knn_accuracy = accuracy_score(y_test, knn_prediction)
    knn_precision = precision_score(y_test, knn_prediction)
    knn_recall = recall_score(y_test, knn_prediction)
    knn_f1 = f1_score(y_test, knn_prediction)

    print("\n========== KNN ==========")
    print("Accuracy :", knn_accuracy)
    print("Precision :", knn_precision)
    print("Recall :", knn_recall)
    print("F1 Score :", knn_f1)
    print("Confusion Matrix :")
    print(confusion_matrix(y_test, knn_prediction))


    # Select best model using F1 score

    best_f1 = max(
        logistic_f1,
        decision_f1,
        random_f1,
        knn_f1
    )

    if best_f1 == logistic_f1:

        best_model = logistic_model
        print("\nBEST MODEL : Logistic Regression")

    elif best_f1 == decision_f1:

        best_model = decision_model
        print("\nBEST MODEL : Decision Tree")

    elif best_f1 == random_f1:

        best_model = random_model
        print("\nBEST MODEL : Random Forest")

    else:

        best_model = knn_model
        print("\nBEST MODEL : KNN")


    return best_model


if __name__ == "__main__":
    evaluate_models()