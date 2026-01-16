# Code Quality Predictor - Test Samples

Copy and paste these code samples into your web app to test predictions.

---

## ✅ GOOD QUALITY SAMPLES

### Sample 1: Well Documented Function
```python
# Calculate the factorial of a number
def calculate_factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)
```

### Sample 2: Security Module
```python
# User authentication module
import hashlib
import secrets

def hash_password(password):
    """
    Hash a password using SHA-256 with salt.
    """
    salt = secrets.token_hex(16)
    password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    return password_hash, salt

def verify_password(password, password_hash, salt):
    """
    Verify if the provided password matches the hash.
    """
    computed_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    return computed_hash == password_hash
```

### Sample 3: Data Processing
```python
# Data processing utility
import json
from typing import List, Dict

def process_user_data(users: List[Dict]) -> List[Dict]:
    """
    Process and clean user data.
    
    Args:
        users: List of user dictionaries
        
    Returns:
        List of processed user dictionaries
    """
    processed = []
    for user in users:
        if user.get('email') and user.get('name'):
            processed.append({
                'name': user['name'].strip(),
                'email': user['email'].lower()
            })
    return processed
```

---

## ⚠️ AVERAGE QUALITY SAMPLES

### Sample 1: Simple Functions
```python
def add(a,b):
    return a+b

def subtract(x,y):
    return x-y

def multiply(num1,num2):
    return num1*num2
```

### Sample 2: Basic Logic
```python
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
```

### Sample 3: Math Functions
```python
import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_perimeter(radius):
    return 2 * math.pi * radius
```

---

## ❌ POOR QUALITY SAMPLES

### Sample 1: Deep Nesting
```python
def a(x,y):
 if x>0:
  if y>0:
   if x>y:
    if y>10:
     return x
   return y
 return 0
```

### Sample 2: Very Deep Nesting
```python
def b(p,q,r):
 if p>q:
  if q>r:
   if r>0:
    if p>10:
     if q>10:
      if r>10:
       return p+q+r
 return 0
```

### Sample 3: Complex Nesting
```python
def c(a,b):
 if a>b:
  if b>0:
   if a>5:
    if b>5:
     if a>10:
      if b>10:
       return a+b
 return 0
```

### Sample 4: Multiple Conditions
```python
def x(y,z):
 if y>z:
  return y
 if z>y:
  return z
 if y==z:
  return 0
```

---

## 🔍 EDGE CASES

### Very Short Code
```python
# Very short code
def hello():
    return "world"
```

### Many Comments
```python
# This is a comment
# Another comment
# Yet another comment
def test():
    # Function comment
    return True
```

### Long Lines
```python
# Code with long lines
def process_very_long_function_name_with_many_parameters(param1, param2, param3, param4, param5, param6):
    result = param1 + param2 + param3 + param4 + param5 + param6
    return result
```

### Mixed Quality
```python
# Mixed quality
def good_function(name):
    """
    This is a well-documented function.
    """
    return f"Hello, {name}"

def bad(x,y):
 if x>y:
  return x
 return y
```

---

## 📝 How to Use

1. Start your Flask app: `python app.py`
2. Open browser: `http://localhost:5000`
3. Copy any sample above
4. Paste into the text area
5. Click "Predict Quality"
6. See the prediction result!

---

## 💡 Testing Tips

- **Test Good samples first** - Should predict "Good"
- **Test Poor samples** - Should predict "Poor" 
- **Test Average samples** - Should predict "Average"
- **Try edge cases** - See how the model handles unusual code
- **Mix and match** - Try combining different code styles
