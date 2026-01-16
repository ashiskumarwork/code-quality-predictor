from feature_extractor import extract_features

sample_code = """
# This function adds numbers
def add(a, b):
    return a + b

def bad(x,y):
    if x>0:
        if y>0:
            return x+y
"""

print(extract_features(sample_code))
