# Complete Installation Guide for AI-Augmented Product Engineering Program

**Document Version:** 1.0  
**Last Updated:** 2026-09-29  
**For:** Participant Prerequisites - Caliber Training

---

## Table of Contents
1. [System Requirements Verification](#1-system-requirements-verification)
2. [Python 3.11.x Installation](#2-python-311x-installation)
3. [Git Installation](#3-git-installation)
4. [Visual Studio Code Installation](#4-visual-studio-code-installation)
5. [VS Code Extensions Setup](#5-vs-code-extensions-setup)
6. [Python Virtual Environment Setup](#6-python-virtual-environment-setup)
7. [GitHub Account & Repository Setup](#7-github-account--repository-setup)
8. [Environment Configuration](#8-environment-configuration)
9. [Network & LLM Endpoint Configuration](#9-network--llm-endpoint-configuration)
10. [Pre-Training Validation](#10-pre-training-validation)
11. [Final Readiness Checklist](#11-final-readiness-checklist)

---

## 1. System Requirements Verification

### Hardware Requirements

Before starting installation, verify your system meets these minimum requirements:

#### Operating System
- **Windows 10/11** (64-bit) OR
- **macOS 13 or later**

#### RAM
- **Minimum:** 8 GB RAM
- **Recommended:** 16 GB RAM

#### Disk Space
- **Minimum:** 10 GB free disk space

#### Network
- Stable internet connectivity (for downloads and GitHub operations)
- Administrative access for initial software installation

### How to Check Your System

#### **On Windows:**
1. Right-click on **"This PC"** or **"My Computer"**
2. Select **"Properties"**
3. Note your Windows version and installed RAM
4. Open **File Explorer** and check free disk space on your C: drive

#### **On macOS:**
1. Click **Apple Menu** → **About This Mac**
2. Note your macOS version and memory
3. Click **Storage** to see available disk space

---

## 2. Python 3.11.x Installation

### Step 1: Download Python

#### **Option A: Windows**

1. Visit **https://www.python.org/downloads/**
2. Look for **"Python 3.11.x"** (latest 3.11 version)
3. Click the **"Download Python 3.11.x"** button
4. This downloads the official Windows installer

#### **Option B: macOS**

1. Visit **https://www.python.org/downloads/**
2. Download the **macOS Installer** for Python 3.11.x
3. Choose between Intel (x86_64) or Apple Silicon (ARM64) based on your Mac

### Step 2: Install Python on Windows

1. **Locate the downloaded file:** Usually in your `Downloads` folder
2. **Double-click** the installer (e.g., `python-3.11.x-amd64.exe`)
3. **IMPORTANT:** Check the box **"Add Python 3.11 to PATH"** (bottom of first screen)
4. Click **"Install Now"** (for default installation)
   - OR click **"Customize installation"** if you want to choose specific features
5. **Verify the installation completes** (you'll see "Setup was successful")
6. Click **"Close"**

### Step 3: Install Python on macOS

1. **Double-click** the downloaded installer
2. Follow the installation wizard steps:
   - Accept the license agreement
   - Choose installation location (default is fine)
   - Wait for installation to complete
3. Python is installed in `/Library/Frameworks/Python.framework/Versions/3.11/`

### Step 4: Verify Python Installation

Open your terminal/PowerShell and run:

```bash
python --version
```

**Expected Output:**
```
Python 3.11.x (or Python 3.11.0, Python 3.11.1, etc.)
```

If you see an error, try:
- **Windows:** `py --version`
- **macOS:** `python3 --version`

### Step 5: Verify Pip Installation

Pip comes bundled with Python. Verify it:

```bash
pip --version
```

**Expected Output:**
```
pip 23.x.x from C:\Users\...\Python\Lib\site-packages\pip (python 3.11)
```

---

## 3. Git Installation

### Step 1: Download Git

1. Visit **https://git-scm.com/downloads**
2. Select your operating system:
   - **Windows:** Automatic detection, click the download link
   - **macOS:** Download the official macOS installer

### Step 2: Install Git on Windows

1. **Double-click** the downloaded installer (e.g., `Git-2.42.0-64-bit.exe`)
2. **Choose installation location** (default: `C:\Program Files\Git`)
3. **Component selection** - Keep defaults checked:
   - Git Bash
   - Git GUI
   - Git LFS
   - Windows Explorer integration
4. **Default editor:** Select **"Use Visual Studio Code as Git's default editor"** (if VS Code is already installed)
5. **Initial branch name:** Keep as **"master"** (or select "main")
6. **PATH environment:** Select **"Use Git from Git Bash only"** (or "Use Git and optional Unix tools from Windows Command Prompt")
7. **Line ending:** Select **"Checkout Windows-style, commit Unix-style CRLF"**
8. Click **"Next"** through remaining options
9. Click **"Install"**
10. Click **"Finish"** (uncheck "Launch Git Bash" if you prefer)

### Step 3: Install Git on macOS

1. **Double-click** the installer package
2. Follow the installation wizard
3. Authenticate with your Mac password
4. Wait for installation to complete

### Step 4: Verify Git Installation

Open your terminal/PowerShell and run:

```bash
git --version
```

**Expected Output:**
```
git version 2.42.0 (or any recent version)
```

### Step 5: Configure Git (First Time Setup)

Run these commands in your terminal:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

**Verify configuration:**

```bash
git config --list
```

---

## 4. Visual Studio Code Installation

### Step 1: Download VS Code

1. Visit **https://code.visualstudio.com/download**
2. Select your operating system:
   - **Windows:** "Windows (Stable)"
   - **macOS:** "Mac (Stable)" - Choose Intel or Apple Silicon

### Step 2: Install VS Code on Windows

1. **Double-click** the downloaded installer (e.g., `VSCodeUserSetup-x64-1.x.x.exe`)
2. Accept the license agreement
3. Select destination folder (default is fine)
4. Choose additional tasks:
   - **Check:** "Add to PATH"
   - **Check:** "Register Code as an editor for supported file types"
   - **Check:** "Add 'Open with Code' action to Windows Explorer file context menu"
   - **Check:** "Add 'Open with Code' action to Windows Explorer folder context menu"
5. Click **"Install"**
6. Click **"Finish"** and optionally launch VS Code

### Step 3: Install VS Code on macOS

1. **Drag** the VS Code icon to your **Applications** folder
2. Wait for copying to complete
3. Open **Applications** folder and double-click **Visual Studio Code**
4. Accept security confirmation if prompted
5. (Optional) Install command line tools:
   - Launch VS Code
   - Press `Cmd + Shift + P`
   - Type "shell command"
   - Select "Shell Command: Install 'code' command in PATH"

### Step 4: Verify VS Code Installation

Open a terminal and run:

```bash
code --version
```

**Expected Output:**
```
1.82.0 (or any recent version)
```

### Step 5: Launch VS Code

**Windows:** Search for "Visual Studio Code" in Start Menu  
**macOS:** Open Applications folder and double-click Visual Studio Code  
**OR** from terminal: `code .`

---

## 5. VS Code Extensions Setup

### Required Extensions

You need to install **4 required extensions**:

1. **Python** (by Microsoft)
2. **Pylance** (by Microsoft)
3. **GitHub Pull Requests and Issues** (by GitHub)
4. **Jupyter** (by Microsoft) - *If notebooks are included in training*

### Optional Extensions

- **Markdown Preview** (by Microsoft)
- **REST Client** (by Humao)

### How to Install Extensions in VS Code

#### Method 1: Via Extensions Marketplace (Recommended)

1. **Open VS Code**
2. Click the **Extensions icon** on the left sidebar (looks like 4 squares)
3. **Search for each extension** by name
4. Click the extension
5. Click **"Install"**
6. Wait for installation to complete
7. You may see a **"Reload Required"** button - click it

#### Method 2: Via Command Line

Open terminal and run:

```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension github.vscode-pull-request-github
code --install-extension ms-toolsai.jupyter
```

### Verify Extensions Installation

1. Open VS Code
2. Click **Extensions** icon in left sidebar
3. Click **"Installed"** to see all installed extensions
4. You should see all required extensions listed

### Configure Python Extension

1. Open **File** → **Preferences** → **Settings** (or press `Ctrl+,`)
2. Search for **"python.defaultInterpreterPath"**
3. This will be set automatically, but verify it points to your Python 3.11 installation

---

## 6. Python Virtual Environment Setup

A virtual environment isolates Python packages for this project.

### Step 1: Create Virtual Environment

#### **On Windows:**

Navigate to your project folder and run:

```bash
python -m venv .venv
```

This creates a folder called `.venv` in your project directory.

#### **On macOS:**

```bash
python3 -m venv .venv
```

### Step 2: Activate Virtual Environment

#### **On Windows:**

```bash
.venv\Scripts\activate
```

**You should see:** `(.venv)` appears at the start of your terminal prompt

#### **On macOS:**

```bash
source .venv/bin/activate
```

**You should see:** `(.venv)` appears at the start of your terminal prompt

### Step 3: Verify Virtual Environment Activation

Run:

```bash
python --version
```

Should show **Python 3.11.x**

### Step 4: Upgrade Pip (Optional but Recommended)

```bash
python -m pip install --upgrade pip
```

### Step 5: Configure VS Code to Use Virtual Environment

1. Open your project folder in VS Code
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
3. Type **"Python: Select Interpreter"**
4. Choose the interpreter from `.venv` folder
   - Should show path like: `.\venv\Scripts\python.exe`

### Step 6: Deactivate Virtual Environment (When Not Working)

```bash
deactivate
```

The `(.venv)` prefix should disappear from your terminal.

---

## 7. GitHub Account & Repository Setup

### Step 1: Create GitHub Account (If Not Existing)

1. Visit **https://github.com/signup**
2. Enter your email address
3. Create a password
4. Choose a username
5. Verify your email address
6. Complete the account setup
7. (Optional) Set up two-factor authentication for security

### Step 2: Verify GitHub Access

1. Go to **https://github.com** and sign in
2. Click your profile icon (top-right) → **Settings**
3. Verify your account is active

### Step 3: Set Up GitHub Authentication on Your Laptop

#### **Option A: Personal Access Token (Recommended)**

1. Go to **https://github.com/settings/tokens**
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Set token name: `training-token`
4. Set expiration: 90 days (or as needed for training)
5. Select scopes (minimum):
   - `repo` (full control of private repositories)
   - `user` (read user profile data)
6. Click **"Generate token"**
7. **Copy the token immediately** (you won't see it again)
8. Store it securely (use Windows Credential Manager or macOS Keychain)

#### **Option B: SSH Key**

1. Open terminal/PowerShell
2. Run: `ssh-keygen -t ed25519 -C "your-email@example.com"`
3. Accept default file location (press Enter)
4. Set a passphrase (optional but recommended)
5. Add SSH key to GitHub:
   - Go to **https://github.com/settings/keys**
   - Click **"New SSH key"**
   - Paste your public key (from `~/.ssh/id_ed25519.pub`)
   - Click **"Add SSH key"**

### Step 4: Configure Git Credentials

#### **Windows:**

1. Open PowerShell as Administrator
2. Run:
   ```bash
   git config --global credential.helper wincred
   ```
3. Next time you push/pull, enter your GitHub credentials once

#### **macOS:**

Credentials are automatically stored in Keychain.

### Step 5: Test GitHub Connection

```bash
git clone https://github.com/YOUR_USERNAME/test.git
```

This will prompt for authentication. Use your username and personal access token (or SSH key).

---

## 8. Environment Configuration

### Create .env File for LLM Credentials

This file stores sensitive information locally.

### Step 1: Create .env File

1. Open your project folder in VS Code
2. Right-click in the Explorer panel
3. Select **"New File"**
4. Name it: `.env`
5. Add the following lines:

```
LLM_ENDPOINT=
LLM_API_KEY=
LLM_MODEL=
LLM_API_VERSION=
```

### Step 2: Add Credentials (When Trainer Provides Them)

After training begins, your trainer will provide:
- **LLM_ENDPOINT:** The API endpoint URL
- **LLM_API_KEY:** Your temporary API key
- **LLM_MODEL:** The model/deployment name
- **LLM_API_VERSION:** The API version (if required)

Fill in these values in the `.env` file.

### Step 3: Configure .gitignore

Ensure `.env` is not committed to GitHub:

1. Create (or open) `.gitignore` file in your project root
2. Add this line:

```
.env
```

3. Save the file

This prevents accidentally pushing credentials to GitHub.

### Step 4: Load .env in Python

When writing Python code, load the .env file:

```python
from dotenv import load_dotenv
import os

load_dotenv()

llm_endpoint = os.getenv('LLM_ENDPOINT')
llm_api_key = os.getenv('LLM_API_KEY')
llm_model = os.getenv('LLM_MODEL')
```

**Install python-dotenv package:**

```bash
pip install python-dotenv
```

---

## 9. Network & LLM Endpoint Configuration

### Network Access Requirements

Verify your network allows HTTPS access to these domains:

- **github.com** - GitHub repository hosting
- **api.github.com** - GitHub API
- **raw.githubusercontent.com** - Raw GitHub content
- **objects.githubusercontent.com** - GitHub objects
- **pypi.org** - Python package index
- **files.pythonhosted.org** - Python packages
- **LLM endpoint** - Trainer-provided endpoint
- **Authentication endpoint** - If required by LLM service

### Test Network Connectivity

#### **Test GitHub Access:**

```bash
git clone https://github.com/YOUR_USERNAME/test.git
```

#### **Test PyPI Access:**

```bash
pip install requests
```

#### **Test LLM Endpoint:** (After trainer provides URL)

```python
import requests

endpoint = "YOUR_LLM_ENDPOINT"
headers = {"Authorization": f"Bearer YOUR_API_KEY"}

response = requests.get(endpoint, headers=headers)
print(response.status_code)
```

### Firewall/Proxy Configuration

If your organization uses a firewall/proxy:

1. Contact your IT department for:
   - Proxy server address
   - Port number
   - Authentication credentials (if required)

2. Configure Git:

```bash
git config --global http.proxy http://proxyuser:proxypass@proxyserver:port
git config --global https.proxy https://proxyuser:proxypass@proxyserver:port
```

3. Configure Pip:

Create/edit `~/.pip/pip.conf`:

```
[global]
proxy = [user:passwd@]proxy.server:port
```

---

## 10. Pre-Training Validation

### Run Environment Validation Script

Before training begins, you'll receive a validation script: `run_environment_check.py`

### How to Run Validation

1. **Place the script** in your project root directory
2. **Activate your virtual environment:**

```bash
# Windows
.venv\Scripts\activate

# macOS
source .venv/bin/activate
```

3. **Run the validation script:**

```bash
python run_environment_check.py
```

### What the Script Checks

- ✓ Python 3.11.x installation
- ✓ Pip availability
- ✓ Git installation and configuration
- ✓ Required Python packages
- ✓ GitHub repository access
- ✓ LLM endpoint connectivity
- ✓ Required training files
- ✓ Local ports availability
- ✓ Local application startup
- ✓ Basic test execution

### Expected Output

```
Environment Validation Report
==============================
[✓] Python version: Python 3.11.x
[✓] Pip available: pip 23.x.x
[✓] Git installed: git version 2.42.0
[✓] GitHub access: Successfully connected
[✓] LLM endpoint: Successfully connected
[✓] Required packages: All installed
[✓] Local ports: Available
[✓] All validations passed!
```

### Troubleshooting Validation Failures

| Issue | Solution |
|-------|----------|
| Python not found | Reinstall Python with "Add to PATH" option checked |
| Pip not available | Run `python -m pip install --upgrade pip` |
| GitHub access denied | Check credentials, verify SSH key or token |
| LLM endpoint unreachable | Verify network access, proxy settings |
| Port already in use | Close other applications using the port |
| Virtual environment issues | Recreate venv: delete `.venv` folder and rerun creation steps |

---

## 11. Final Readiness Checklist

Before training begins, verify all items below are complete:

### System & Laptop
- [ ] Windows 10/11 or macOS 13+ installed
- [ ] Minimum 8 GB RAM available (16 GB recommended)
- [ ] Minimum 10 GB free disk space
- [ ] Stable internet connectivity confirmed

### GitHub
- [ ] Personal GitHub account active
- [ ] Can sign in to GitHub successfully
- [ ] Can create a new private repository
- [ ] GitHub credentials/SSH key configured on laptop
- [ ] Git clone operations working
- [ ] Git commit operations working
- [ ] Git push operations working

### Python
- [ ] Python 3.11.x installed (64-bit)
- [ ] Python in system PATH
- [ ] `python --version` returns Python 3.11.x
- [ ] `pip --version` works
- [ ] Pip can install packages: `pip install requests` (test)

### Git
- [ ] Git installed and in PATH
- [ ] `git --version` returns a version number
- [ ] Git username configured globally
- [ ] Git email configured globally
- [ ] HTTPS cloning works
- [ ] Git credentials helper configured

### Visual Studio Code
- [ ] VS Code installed
- [ ] `code --version` returns a version number
- [ ] Can open VS Code from terminal

### VS Code Extensions
- [ ] Python extension by Microsoft installed
- [ ] Pylance extension by Microsoft installed
- [ ] GitHub Pull Requests extension installed
- [ ] Jupyter extension installed (if needed)
- [ ] Extensions appear in "Installed" tab

### Python Virtual Environment
- [ ] `.venv` folder created in project directory
- [ ] Virtual environment activates successfully
- [ ] `python --version` shows 3.11.x when activated
- [ ] Pip works in virtual environment
- [ ] Can install packages: `pip install requests` (in venv)
- [ ] VS Code uses `.venv` as Python interpreter

### Network & Access
- [ ] GitHub.com accessible from network
- [ ] PyPI.org accessible from network (test: `pip install requests`)
- [ ] Can clone GitHub repositories
- [ ] LLM endpoint URL accessible (after trainer provides it)

### Environment Files
- [ ] `.env` file created in project root
- [ ] `.gitignore` file includes `.env`
- [ ] Can create and read `.env` variables from Python

### Pre-Training Validation
- [ ] Received `run_environment_check.py` script
- [ ] Script runs without errors
- [ ] All validation checks pass
- [ ] No missing dependencies reported

### Security & Data
- [ ] Understand data is fictional/synthetic only
- [ ] Will not upload real customer/patient data
- [ ] Will not use production credentials
- [ ] Credentials stored in `.env` (not in code)
- [ ] Training materials reviewed

---

## Additional Resources

### Official Documentation
- **Python:** https://docs.python.org/3.11/
- **Git:** https://git-scm.com/doc
- **VS Code:** https://code.visualstudio.com/docs
- **GitHub:** https://docs.github.com/

### Useful Commands Reference

```bash
# Python
python --version
pip install package_name
pip list
python -m venv .venv

# Git
git config --list
git clone url
git add .
git commit -m "message"
git push
git pull

# VS Code
code .
code --version
code --install-extension extension-name
```

### Troubleshooting Contacts
- Trainer email: [To be provided]
- IT Support: [To be provided]
- GitHub Support: https://support.github.com

---

## Notes for Participants

✅ **Save this document** for reference during training  
✅ **Complete all steps** before training begins  
✅ **Run validation script** to confirm setup  
✅ **Note any errors** to report to trainer  
✅ **Do not store credentials** in code or GitHub  
✅ **Keep .env file** local only (never commit)  
✅ **Verify network access** to all required domains

---

**Document prepared for:** AI-Augmented Product Engineering Program  
**Total Setup Time:** Approximately 1-2 hours  
**Support:** Contact your trainer if you encounter any issues

