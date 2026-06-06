
from sklearn.metrics import classification_report, accuracy_score

def evaluar_modelo(model, X_test, y_test):
    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nReporte:\n", classification_report(y_test, y_pred))