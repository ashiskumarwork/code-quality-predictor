# 🚀 Quick Start - Deploy to Render

## Pre-Deployment Checklist

Before you start, make sure:

- [x] ✅ `requirements.txt` - Created
- [x] ✅ `.gitignore` - Created (allows quality_model.pkl)
- [x] ✅ `app.py` - Updated for production
- [x] ✅ `render.yaml` - Created (optional config)
- [ ] ⬜ `quality_model.pkl` - Must exist in project folder
- [ ] ⬜ Git repository initialized
- [ ] ⬜ Code pushed to GitHub
- [ ] ⬜ Render account created

---

## Step-by-Step Commands

### 1. Verify Model Exists
```bash
dir quality_model.pkl
```
If it doesn't exist, run:
```bash
python create_dataset.py
python train_model.py
```

### 2. Initialize Git (if not done)
```bash
git init
git add .
git commit -m "Initial commit: Code Quality Predictor"
```

### 3. Create GitHub Repository
1. Go to https://github.com/new
2. Create new repository (don't initialize with README)
3. Copy the repository URL

### 4. Connect to GitHub
```bash
# Replace YOUR_USERNAME and REPO_NAME
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

### 5. Deploy on Render
1. Go to https://render.com
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"
4. Connect your repository
5. Configure:
   - **Name:** code-quality-predictor
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Click "Create Web Service"
7. Wait for deployment (2-5 minutes)

### 6. Test Your App
- Click the URL provided by Render
- Test with a code sample
- Done! 🎉

---

## Need More Details?

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for complete step-by-step instructions with screenshots and troubleshooting.

---

## Common Issues

**Model not found?**
```bash
git add quality_model.pkl
git commit -m "Add model file"
git push
```

**Build fails?**
- Check `requirements.txt` has all packages
- Verify Python version in Render settings

**App crashes?**
- Check Render logs
- Verify `gunicorn` is in requirements.txt
