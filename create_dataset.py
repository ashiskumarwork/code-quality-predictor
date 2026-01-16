from feature_extractor import extract_features
import pandas as pd

def label_quality(f):
    score = 0

    # Good signals
    if f["comment_ratio"] > 0.2:
        score += 2

    if f["bad_names"] < 3:
        score += 2

    if f["max_depth"] <= 1:
        score += 1

    # Bad signals
    if f["max_depth"] > 2:
        score -= 2

    if f["bad_names"] > 6:
        score -= 2

    if f["lines"] > 20:
        score -= 1

    if score >= 2:
        return "Good"
    elif score >= 0:
        return "Average"
    else:
        return "Poor"


samples = []

# Generate multiple patterns - increased from 30 to 100 for better dataset
for i in range(100):

    # Good quality code examples
    good_code = f"""
# function {i}
def add_numbers_{i}(a, b):
    # clean code
    return a + b
"""
    samples.append(good_code)

    good_code2 = f"""
# Calculate sum of two numbers
def calculate_sum_{i}(num1, num2):
    \"\"\"
    This function adds two numbers together.
    \"\"\"
    result = num1 + num2
    return result
"""
    samples.append(good_code2)

    # Average quality code examples
    avg_code = f"""
def add{i}(a,b):
    return a+b
"""
    samples.append(avg_code)

    avg_code2 = f"""
def process{i}(x,y):
    if x>0:
        return x+y
    return 0
"""
    samples.append(avg_code2)

    # Poor quality code examples
    poor_code = f"""
def a{i}(x,y):
 if x>0:
  if y>0:
   if x>y:
    return x
"""
    samples.append(poor_code)

    poor_code2 = f"""
def b{i}(p,q):
 if p>q:
  if q>0:
   if p>10:
    if q>10:
     return p+q
"""
    samples.append(poor_code2)


rows = []

for code in samples:
    f = extract_features(code)
    f["label"] = label_quality(f)
    rows.append(f)

df = pd.DataFrame(rows)
df.to_csv("code_quality_dataset.csv", index=False)

print(df["label"].value_counts())
print("New Dataset Created!")
