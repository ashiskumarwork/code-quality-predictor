# Code Quality Predictor

A Machine Learning web application that predicts code quality (Good, Average, Poor) based on code features.

## 🚀 Live Demo

[Deploy on Render](https://render.com) - See DEPLOYMENT_GUIDE.md for instructions

## 📋 Features

- **Code Quality Prediction**: Analyzes Python code and predicts quality
- **Feature Extraction**: Extracts 11 code quality features
- **ML Model**: Uses Random Forest Classifier with hyperparameter tuning
- **Web Interface**: Simple Flask web app for easy testing

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/code-quality-predictor.git
cd code-quality-predictor
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create dataset and train model:
```bash
python create_dataset.py
python train_model.py
```

5. Run the app:
```bash
python app.py
```

6. Open browser: `http://localhost:5000`

## 📁 Project Structure

```
code-quality-predictor/
├── app.py                 # Flask web application
├── feature_extractor.py   # Feature extraction logic
├── train_model.py         # Model training script
├── create_dataset.py      # Dataset generation
├── predict.py             # Prediction script
├── test.py                # Testing script
├── requirements.txt       # Python dependencies
├── quality_model.pkl      # Trained model
├── templates/
│   └── index.html         # Web interface
└── README.md
```

## 🧪 Testing

Use the provided test samples:
```bash
python test_samples.py
```

Or check `TEST_SAMPLES.md` for code samples to test in the web app.

## 📊 Model Features

The model uses 11 features:
- Lines of code
- Comment ratio
- Long lines count
- Maximum nesting depth
- Bad variable names count
- Function count
- Average line length
- Whitespace ratio
- Import count
- Docstring presence
- Cyclomatic complexity

## 🚀 Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed deployment instructions on Render.

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

Your Name

---

Made with ❤️ using Flask and scikit-learn
