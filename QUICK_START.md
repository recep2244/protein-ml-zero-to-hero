# Quick Start Guide

Get the curriculum running in under 5 minutes. No prior experience with Python or GitHub is required.

> **Prefer to skip local setup?** See [CLOUD_SETUP.md](CLOUD_SETUP.md) to run every notebook in your browser using Google Colab — nothing to install.

---

## Step 1: Install Python 3.10 or later

You need Python 3.10 or a newer 3.x version.

**Check if you already have it:**
```bash
python --version
```
If you see `Python 3.10.x` or higher, skip to Step 2.

### Windows

1. Go to https://www.python.org/downloads/
2. Click **Download Python 3.10** (or the latest 3.x).
3. Run the installer.
4. **Important:** On the first screen of the installer, check the box that says **"Add Python to PATH"** before clicking Install.
5. Open a new Command Prompt window and verify:
   ```
   python --version
   ```

### macOS

Option A — Official installer (easiest):
1. Go to https://www.python.org/downloads/
2. Download and run the macOS installer for Python 3.10+.

Option B — Homebrew (if you already use Homebrew):
```bash
brew install python@3.10
```

Verify:
```bash
python3 --version
```

### Linux (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip -y
python3.10 --version
```

---

## Step 2: Install Git and clone the repository

**Check if Git is installed:**
```bash
git --version
```

### Install Git

- **Windows:** Download from https://git-scm.com/download/win and run the installer. Accept all defaults.
- **macOS:** Run `git --version` in Terminal; if Git is not installed, macOS will prompt you to install developer tools.
- **Linux:** `sudo apt install git -y`

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/hackerrank.git
cd hackerrank
```

Replace `YOUR_USERNAME/hackerrank` with the actual repository URL if different.

---

## Step 3: Create a virtual environment and install dependencies

A virtual environment keeps this project's packages separate from your system Python.

```bash
# Create the virtual environment (do this once)
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS / Linux:
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

You will see many packages installing. This takes 2–5 minutes depending on your internet speed.

**Verify the installation:**
```bash
python -c "import torch; import numpy; import Bio; print('All good!')"
```

---

## Step 4: Launch Jupyter and open the first notebook

```bash
jupyter notebook
```

Your browser will open automatically to the Jupyter file browser. If it does not, copy the URL from the terminal output (it looks like `http://127.0.0.1:8888/?token=...`) and paste it into your browser.

Navigate to:
```
00_python_ml_basics/
```
and open `00_python_review.ipynb` (or the first `.ipynb` file in that folder).

---

## Step 5: Your first 5 minutes in notebook 00/00

1. **Read the TL;DR cell** at the top. It tells you in plain English what you will learn.
2. **Run the first code cell** by clicking on it and pressing `Shift + Enter`.
3. Work through the notebook from top to bottom, running each cell in order.
4. When you see a cell marked `# EXERCISE:`, try to write the solution yourself before looking at `# SOLUTION:`.
5. If a cell produces an error, read the error message carefully — it usually tells you exactly what went wrong.

That is it. You are now set up and working through the curriculum.

---

## If Something Fails

Here are fixes for the 5 most common errors:

### Error 1: `python` is not recognized / command not found

**Cause:** Python was not added to your system PATH.

**Fix (Windows):** Uninstall Python and reinstall, this time checking "Add Python to PATH" on the first installer screen.

**Fix (macOS/Linux):** Try `python3` instead of `python`. If that works, create an alias:
```bash
echo 'alias python=python3' >> ~/.bashrc && source ~/.bashrc
```

---

### Error 2: `pip install -r requirements.txt` fails with permission errors

**Cause:** You are installing into the system Python instead of the virtual environment.

**Fix:** Make sure you activated the virtual environment first:
```bash
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```
The prompt should show `(venv)` before it. Then re-run `pip install -r requirements.txt`.

---

### Error 3: `ModuleNotFoundError: No module named 'torch'` (or any other package)

**Cause:** You are running Jupyter with the wrong Python kernel (not the virtual environment).

**Fix:**
```bash
# With your venv activated, install the Jupyter kernel for this environment
pip install ipykernel
python -m ipykernel install --user --name=venv --display-name "Python (venv)"
```
Then, inside Jupyter, go to **Kernel > Change Kernel** and select **"Python (venv)"**.

---

### Error 4: `jupyter: command not found`

**Cause:** Jupyter was not installed, or the virtual environment is not active.

**Fix:**
```bash
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install jupyter
jupyter notebook
```

---

### Error 5: Port 8888 is already in use

**Cause:** Another Jupyter server (or another program) is using port 8888.

**Fix:**
```bash
jupyter notebook --port 8889
```
Or close the other Jupyter session first.

---

## Next Steps

- Follow **Path A** (HackerRank Certification) in `CLAUDE.md` if your goal is assessment prep.
- Follow **Path C** (Structural ML) if your goal is Isomorphic Labs / DeepMind interviews.
- See `STUDY_PLAN.md` for a week-by-week schedule.
- See `CLOUD_SETUP.md` if you prefer to work entirely in Google Colab without any local installation.
