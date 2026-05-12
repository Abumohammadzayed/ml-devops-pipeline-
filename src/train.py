from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Load data
data = load_iris()
X, y = data.data, data.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate
preds = clf.predict(X_test)
acc = accuracy_score(y_test, preds)
print(f"Test accuracy: {acc:.2f}")

# Save the model
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/iris_model.pkl")
print("Model saved to models/iris_model.pkl")
