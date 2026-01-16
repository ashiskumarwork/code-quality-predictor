from flask import Flask, request, render_template
import joblib
import pandas as pd
from feature_extractor import extract_features
import os

app = Flask(__name__)

# Load model once at startup (more efficient)
model_path = "quality_model.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("✓ Model loaded successfully")
else:
    model = None
    print("⚠ Warning: Model file not found!")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        if model is None:
            error = "Model not available. Please train the model first."
        else:
            code = request.form.get("code", "").strip()
            
            if not code:
                error = "Please enter some code to analyze."
            else:
                try:
                    f = extract_features(code)
                    df = pd.DataFrame([f])
                    result = model.predict(df)[0]
                except Exception as e:
                    error = f"Error processing code: {str(e)}"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    # For local development
    app.run(debug=True, host="0.0.0.0", port=5000)
else:
    # For production (Render will use this)
    # Gunicorn will handle the app
    pass
