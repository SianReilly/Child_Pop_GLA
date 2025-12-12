# Population Projections Streamlit App

Interactive visualization comparing Mid-Year Estimates (MYEs) with GLA 2024-based population projections.

## Features

- 📊 Interactive charts comparing actual data with projections
- 🔄 Toggle between age groups (0-15 and 0-19)
- 👥 Optional gender breakdown view
- 📈 Key statistics and metrics
- 📋 Data table view

## How to Deploy on Streamlit Cloud (FREE)

### Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in (or create a free account)
2. Click the "+" icon in the top right → "New repository"
3. Name it something like `population-projections`
4. Make it **Public**
5. Click "Create repository"

### Step 2: Upload Your Files

1. On your new repository page, click "uploading an existing file"
2. Drag and drop these two files:
   - `app.py`
   - `requirements.txt`
3. Click "Commit changes"

### Step 3: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign up" and sign in with your GitHub account
3. Click "New app"
4. Select:
   - **Repository**: Your repository name (e.g., `population-projections`)
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click "Deploy"!

### Step 4: Share Your App

- After ~2-3 minutes, you'll get a URL like: `https://yourname-population-projections.streamlit.app`
- Share this URL with anyone - they can access it instantly without any installation!

## Local Development (Optional)

To run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Data Structure

The app expects data with these columns:
- Dataset (e.g., "MYEs", "GLA RO 5yr Migration")
- Year
- Age Group
- Persons
- Male
- Female

## Updating Data

To update the data in the future, simply:
1. Edit the `default_data` dictionary in `app.py`
2. Commit the changes to GitHub
3. Streamlit Cloud will automatically redeploy (takes ~1 minute)

---

**Note:** Streamlit Cloud is completely free for public apps with reasonable usage limits.
