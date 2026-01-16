"""
Code Quality Predictor - Test Samples
Use these samples to test your app at http://localhost:5000
"""

# ============================================================================
# GOOD QUALITY CODE SAMPLES
# ============================================================================

GOOD_SAMPLE_1 = """
# Calculate the factorial of a number
def calculate_factorial(n):
    \"\"\"
    Calculate the factorial of a given number.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
    \"\"\"
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)
"""

GOOD_SAMPLE_2 = """
# User authentication module
import hashlib
import secrets

def hash_password(password):
    \"\"\"
    Hash a password using SHA-256 with salt.
    \"\"\"
    salt = secrets.token_hex(16)
    password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    return password_hash, salt

def verify_password(password, password_hash, salt):
    \"\"\"
    Verify if the provided password matches the hash.
    \"\"\"
    computed_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    return computed_hash == password_hash
"""

GOOD_SAMPLE_3 = """
# Data processing utility
import json
from typing import List, Dict

def process_user_data(users: List[Dict]) -> List[Dict]:
    \"\"\"
    Process and clean user data.
    
    Args:
        users: List of user dictionaries
        
    Returns:
        List of processed user dictionaries
    \"\"\"
    processed = []
    for user in users:
        if user.get('email') and user.get('name'):
            processed.append({
                'name': user['name'].strip(),
                'email': user['email'].lower()
            })
    return processed
"""

# ============================================================================
# AVERAGE QUALITY CODE SAMPLES
# ============================================================================

AVERAGE_SAMPLE_1 = """
def add(a,b):
    return a+b

def subtract(x,y):
    return x-y

def multiply(num1,num2):
    return num1*num2
"""

AVERAGE_SAMPLE_2 = """
def process_data(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result

def filter_items(items):
    filtered = []
    for item in items:
        if len(item) > 3:
            filtered.append(item)
    return filtered
"""

AVERAGE_SAMPLE_3 = """
import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_perimeter(radius):
    return 2 * math.pi * radius
"""

# ============================================================================
# POOR QUALITY CODE SAMPLES
# ============================================================================

POOR_SAMPLE_1 = """
def a(x,y):
 if x>0:
  if y>0:
   if x>y:
    if y>10:
     return x
   return y
 return 0
"""

POOR_SAMPLE_2 = """
def b(p,q,r):
 if p>q:
  if q>r:
   if r>0:
    if p>10:
     if q>10:
      if r>10:
       return p+q+r
 return 0
"""

POOR_SAMPLE_3 = """
def c(a,b):
 if a>b:
  if b>0:
   if a>5:
    if b>5:
     if a>10:
      if b>10:
       return a+b
 return 0
"""

POOR_SAMPLE_4 = """
def x(y,z):
 if y>z:
  return y
 if z>y:
  return z
 if y==z:
  return 0
"""

# ============================================================================
# EDGE CASES AND SPECIAL SCENARIOS
# ============================================================================

EDGE_CASE_1 = """
# Very short code
def hello():
    return "world"
"""

EDGE_CASE_2 = """
# Code with many comments
# This is a comment
# Another comment
# Yet another comment
def test():
    # Function comment
    return True
"""

EDGE_CASE_3 = """
# Code with long lines
def process_very_long_function_name_with_many_parameters(param1, param2, param3, param4, param5, param6):
    result = param1 + param2 + param3 + param4 + param5 + param6
    return result
"""

EDGE_CASE_4 = """
# Mixed quality
def good_function(name):
    \"\"\"
    This is a well-documented function.
    \"\"\"
    return f"Hello, {name}"

def bad(x,y):
 if x>y:
  return x
 return y
"""

# ============================================================================
# PRINT ALL SAMPLES
# ============================================================================

if __name__ == "__main__":
    samples = {
        "GOOD SAMPLES": [
            ("Good Sample 1 - Well Documented Function", GOOD_SAMPLE_1),
            ("Good Sample 2 - Security Module", GOOD_SAMPLE_2),
            ("Good Sample 3 - Data Processing", GOOD_SAMPLE_3),
        ],
        "AVERAGE SAMPLES": [
            ("Average Sample 1 - Simple Functions", AVERAGE_SAMPLE_1),
            ("Average Sample 2 - Basic Logic", AVERAGE_SAMPLE_2),
            ("Average Sample 3 - Math Functions", AVERAGE_SAMPLE_3),
        ],
        "POOR SAMPLES": [
            ("Poor Sample 1 - Deep Nesting", POOR_SAMPLE_1),
            ("Poor Sample 2 - Very Deep Nesting", POOR_SAMPLE_2),
            ("Poor Sample 3 - Complex Nesting", POOR_SAMPLE_3),
            ("Poor Sample 4 - Multiple Conditions", POOR_SAMPLE_4),
        ],
        "EDGE CASES": [
            ("Edge Case 1 - Very Short", EDGE_CASE_1),
            ("Edge Case 2 - Many Comments", EDGE_CASE_2),
            ("Edge Case 3 - Long Lines", EDGE_CASE_3),
            ("Edge Case 4 - Mixed Quality", EDGE_CASE_4),
        ]
    }
    
    print("=" * 70)
    print("CODE QUALITY PREDICTOR - TEST SAMPLES")
    print("=" * 70)
    print("\nCopy and paste these samples into the web app to test predictions.\n")
    
    for category, sample_list in samples.items():
        print(f"\n{'=' * 70}")
        print(f"{category}")
        print(f"{'=' * 70}\n")
        
        for i, (name, code) in enumerate(sample_list, 1):
            print(f"{i}. {name}")
            print("-" * 70)
            print(code)
            print()
