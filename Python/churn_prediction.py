import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("../Dataset/cleaned_churn.csv")

# Remove customerID
df = df.drop("customerID", axis=1)

# Convert categorical columns
df = pd.get_dummies(df, drop_first=True)

# Target variable
y = df["Churn_Yes"]

# Features
X = df.drop("Churn_Yes", axis=1)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(random_state=42)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\n========== CHURN PREDICTION ==========\n")
print("Model Accuracy:", round(accuracy * 100, 2), "%")