import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
import joblib

# Load dataset
df = pd.read_csv("code_quality_dataset.csv")

X = df.drop("label", axis=1)
y = df["label"]

# Stratified split to maintain class distribution
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("=" * 50)
print("Training Model with Cross-Validation")
print("=" * 50)

# Cross-validation with default model
base_model = RandomForestClassifier(random_state=42)
cv_scores = cross_val_score(base_model, X_train, y_train, cv=5, scoring='accuracy')
print(f"\nBase Model CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# Hyperparameter tuning with simple grid search
print("\nPerforming Hyperparameter Tuning...")
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)

print(f"\nBest Parameters: {grid_search.best_params_}")
print(f"Best CV Score: {grid_search.best_score_:.4f}")

# Use best model
model = grid_search.best_estimator_

# Evaluate on test set
pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)
precision = precision_score(y_test, pred, average='weighted')
recall = recall_score(y_test, pred, average='weighted')
f1 = f1_score(y_test, pred, average='weighted')

print("\n" + "=" * 50)
print("Test Set Performance")
print("=" * 50)
print(f"Accuracy:  {acc:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

print("\n" + "=" * 50)
print("Classification Report")
print("=" * 50)
print(classification_report(y_test, pred))

print("\n" + "=" * 50)
print("Confusion Matrix")
print("=" * 50)
print(confusion_matrix(y_test, pred))

# Feature importance
print("\n" + "=" * 50)
print("Feature Importance")
print("=" * 50)
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print(feature_importance.to_string(index=False))

# Save model
joblib.dump(model, "quality_model.pkl")
print("\n✓ Model saved as quality_model.pkl")
