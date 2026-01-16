from feature_extractor import extract_features
import joblib

model = joblib.load("quality_model.pkl")

code = """
def test(a,b):
 if a>0:
  if b>0:
   return a+b
"""

f = extract_features(code)

import pandas as pd
df = pd.DataFrame([f])

print("Prediction:", model.predict(df)[0])
