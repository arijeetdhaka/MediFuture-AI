from train import train_models

from sklearn.metrics import(
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


    #--------------------------------------------------
    # Logistic Regression
    #--------------------------------------------------

    logistic_prediction = logistic_model.predict(X_test)

    logistic_accuracy = accuracy_score(
        y_test,
        logistic_prediction
    )

    print("\n========== Logistic Regression ==========\n")

    print("Accuracy :", logistic_accuracy)

    print("Precision :",
          precision_score(
              y_test,
              logistic_prediction
          )
    )

    print("Recall :",
          recall_score(
              y_test,
              logistic_prediction
          )
    )

    print("F1 Score :",
          f1_score(
              y_test,
              logistic_prediction
          )
    )

    print("\nConfusion Matrix :")

    print(
        confusion_matrix(
            y_test,
            logistic_prediction
        )
    )



    #--------------------------------------------------
    # Decision Tree
    #--------------------------------------------------

    decision_prediction = decision_model.predict(X_test)

    decision_accuracy = accuracy_score(
        y_test,
        decision_prediction
    )

    print("\n========== Decision Tree ==========\n")

    print("Accuracy :", decision_accuracy)

    print("Precision :",
          precision_score(
              y_test,
              decision_prediction
          )
    )

    print("Recall :",
          recall_score(
              y_test,
              decision_prediction
          )
    )

    print("F1 Score :",
          f1_score(
              y_test,
              decision_prediction
          )
    )

    print("\nConfusion Matrix :")

    print(
        confusion_matrix(
            y_test,
            decision_prediction
        )
    )



    #--------------------------------------------------
    # Random Forest
    #--------------------------------------------------

    random_prediction = random_model.predict(X_test)

    random_accuracy = accuracy_score(
        y_test,
        random_prediction
    )

    print("\n========== Random Forest ==========\n")

    print("Accuracy :", random_accuracy)

    print("Precision :",
          precision_score(
              y_test,
              random_prediction
          )
    )

    print("Recall :",
          recall_score(
              y_test,
              random_prediction
          )
    )

    print("F1 Score :",
          f1_score(
              y_test,
              random_prediction
          )
    )

    print("\nConfusion Matrix :")

    print(
        confusion_matrix(
            y_test,
            random_prediction
        )
    )



    #--------------------------------------------------
    # KNN
    #--------------------------------------------------

    knn_prediction = knn_model.predict(X_test)

    knn_accuracy = accuracy_score(
        y_test,
        knn_prediction
    )

    print("\n========== KNN ==========\n")

    print("Accuracy :", knn_accuracy)

    print("Precision :",
          precision_score(
              y_test,
              knn_prediction
          )
    )

    print("Recall :",
          recall_score(
              y_test,
              knn_prediction
          )
    )

    print("F1 Score :",
          f1_score(
              y_test,
              knn_prediction
          )
    )

    print("\nConfusion Matrix :")

    print(
        confusion_matrix(
            y_test,
            knn_prediction
        )
    )



    #--------------------------------------------------
    # Selecting Best Model
    #--------------------------------------------------

    best_accuracy = max(

        logistic_accuracy,
        decision_accuracy,
        random_accuracy,
        knn_accuracy

    )


    if best_accuracy == logistic_accuracy:

        best_model = logistic_model

        print("\nBEST MODEL : Logistic Regression")


    elif best_accuracy == decision_accuracy:

        best_model = decision_model

        print("\nBEST MODEL : Decision Tree")


    elif best_accuracy == random_accuracy:

        best_model = random_model

        print("\nBEST MODEL : Random Forest")


    else:

        best_model = knn_model

        print("\nBEST MODEL : KNN")



    return (

        best_model,
        X_test,
        y_test

    )



if __name__ == "__main__":

    evaluate_models()