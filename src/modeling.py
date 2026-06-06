import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def entrenar_modelo(df):
    features = df.drop(['High_Risk','Job_Title'], axis=1)
    target = df['High_Risk']

    # encoding rápido
    features = pd.get_dummies(features, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model, X_test, y_test
