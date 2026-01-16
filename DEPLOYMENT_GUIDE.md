# 🚀 Deployment Guide - Code Quality Predictor

Complete guide to deploy your Code Quality Predictor on Render.com

---

## 📋 Prerequisites

Before starting, make sure you have:
- ✅ GitHub account (free)
- ✅ Render account (free tier available)
- ✅ Git installed on your computer
- ✅ Your model file (`quality_model.pkl`) ready

---

## Step 1: Prepare Your Project for GitHub

### 1.1 Check Current Status

First, let's see what files you have:
```bash
# In your project directory
dir
```

### 1.2 Make Sure Model File Exists

**IMPORTANT:** Your `quality_model.pkl` file needs to be committed to GitHub because Render needs it.

**Option A: If you already have the model file**
- Make sure `quality_model.pkl` exists in your project folder
- We'll commit it to GitHub (it's small, so it's fine)

**Option B: If you need to create the model**
```bash
# 1. Create dataset
python create_dataset.py

# 2. Train model
python train_model.py

# Verify model exists
dir quality_model.pkl
```

---

## Step 2: Initialize Git Repository

### 2.1 Check if Git is Already Initialized

```bash
# Check if .git folder exists
dir .git
```

If you see `.git` folder, skip to Step 2.3. If not, continue:

### 2.2 Initialize Git Repository

```bash
# Initialize git
git init

# Add all files
git add .

# Make your first commit
git commit -m "Initial commit: Code Quality Predictor"
```

### 2.3 Check Git Status

```bash
git status
```

You should see your files listed. Make sure `quality_model.pkl` is included!

---

## Step 3: Create GitHub Repository

### 3.1 Create New Repository on GitHub

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **"+"** icon in the top right → **"New repository"**
3. Fill in the details:
   - **Repository name:** `code-quality-predictor` (or any name you like)
   - **Description:** "Machine Learning project to predict code quality"
   - **Visibility:** Choose **Public** (free) or **Private** (if you have GitHub Pro)
   - **DO NOT** check "Initialize with README" (we already have files)
4. Click **"Create repository"**

### 3.2 Connect Local Repository to GitHub

GitHub will show you commands. Use these (replace `YOUR_USERNAME` with your GitHub username):

```bash
# Add GitHub as remote (replace YOUR_USERNAME with your actual GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/code-quality-predictor.git

# Rename branch to main (if needed)
git branch -M main

# Push your code
git push -u origin main
```

**Example:**
```bash
git remote add origin https://github.com/johnsmith/code-quality-predictor.git
git branch -M main
git push -u origin main
```

### 3.3 Verify on GitHub

1. Go to your repository on GitHub
2. You should see all your files including:
   - `app.py`
   - `requirements.txt`
   - `quality_model.pkl`
   - `templates/`
   - etc.

---

## Step 4: Deploy on Render

### 4.1 Sign Up / Sign In to Render

1. Go to [render.com](https://render.com)
2. Click **"Get Started for Free"** or **"Sign In"**
3. Sign up with your GitHub account (recommended - easier integration)

### 4.2 Create New Web Service

1. In Render dashboard, click **"New +"** → **"Web Service"**
2. Click **"Connect account"** if you haven't connected GitHub
3. Select your repository: `code-quality-predictor`
4. Click **"Connect"**

### 4.3 Configure Your Service

Fill in the settings:

**Basic Settings:**
- **Name:** `code-quality-predictor` (or any name)
- **Region:** Choose closest to you (e.g., `Oregon (US West)`)
- **Branch:** `main` (or `master` if that's your branch)
- **Root Directory:** Leave empty (default is root)
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

**Advanced Settings (Optional):**
- **Environment:** `Python 3`
- **Python Version:** `3.11.0` (or latest)

### 4.4 Deploy

1. Scroll down and click **"Create Web Service"**
2. Render will start building your app
3. Wait 2-5 minutes for deployment
4. You'll see build logs - watch for any errors

### 4.5 Check Deployment Status

Look for:
- ✅ **"Build successful"** message
- ✅ **"Your service is live at..."** message with a URL

Your app URL will look like:
```
https://code-quality-predictor.onrender.com
```

---

## Step 5: Test Your Deployed App

1. Click on the URL provided by Render
2. You should see your Code Quality Predictor interface
3. Test with a code sample:
   ```python
   def test():
       return "hello"
   ```
4. Click "Predict Quality"
5. You should see a prediction!

---

## 🔧 Troubleshooting

### Problem: Build Fails

**Solution:**
- Check build logs in Render dashboard
- Make sure `requirements.txt` has all dependencies
- Verify Python version compatibility

### Problem: App Crashes on Start

**Solution:**
- Check logs in Render dashboard
- Make sure `quality_model.pkl` is in the repository
- Verify `gunicorn` is in `requirements.txt`

### Problem: Model Not Found Error

**Solution:**
1. Make sure `quality_model.pkl` is committed to GitHub:
   ```bash
   git add quality_model.pkl
   git commit -m "Add model file"
   git push
   ```
2. Render will auto-deploy after you push

### Problem: Can't Push to GitHub

**Solution:**
- Make sure you're authenticated:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```
- For HTTPS, GitHub may ask for a Personal Access Token instead of password

---

## 📝 Important Notes

### Free Tier Limitations

Render free tier:
- ✅ Free hosting
- ⚠️ Apps sleep after 15 minutes of inactivity (first request after sleep takes ~30 seconds)
- ⚠️ Limited build minutes per month

### Updating Your App

Whenever you make changes:

1. **Make changes locally**
2. **Commit changes:**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```
3. **Render auto-deploys** - it will detect the push and rebuild automatically!

### Model Updates

If you retrain your model:

```bash
# 1. Retrain locally
python create_dataset.py
python train_model.py

# 2. Commit new model
git add quality_model.pkl
git commit -m "Update model with new training"
git push

# 3. Render will auto-deploy with new model
```

---

## ✅ Deployment Checklist

Before deploying, make sure:

- [ ] `requirements.txt` exists with all dependencies
- [ ] `.gitignore` exists (excludes venv, __pycache__)
- [ ] `quality_model.pkl` exists and is committed
- [ ] `app.py` is configured for production
- [ ] `templates/index.html` exists
- [ ] Git repository initialized
- [ ] Code pushed to GitHub
- [ ] Render service created and configured

---

## 🎉 You're Done!

Your app should now be live! Share the Render URL with others.

**Next Steps:**
- Customize the UI (optional)
- Add more features (optional)
- Monitor usage in Render dashboard

---

## 📞 Need Help?

If you encounter issues:
1. Check Render build logs
2. Check Render runtime logs
3. Verify all files are in GitHub
4. Make sure model file is committed

Good luck with your deployment! 🚀
