# Troubleshooting Guide - Training Environment Setup

**Common Issues & Solutions | AI-Augmented Product Engineering Program**

---

## Table of Contents
1. [Python Issues](#python-issues)
2. [Git & GitHub Issues](#git--github-issues)
3. [Visual Studio Code Issues](#visual-studio-code-issues)
4. [Virtual Environment Issues](#virtual-environment-issues)
5. [Network & Firewall Issues](#network--firewall-issues)
6. [LLM Endpoint Issues](#llm-endpoint-issues)
7. [Package Installation Issues](#package-installation-issues)
8. [Validation Script Issues](#validation-script-issues)
9. [Windows-Specific Issues](#windows-specific-issues)
10. [macOS-Specific Issues](#macos-specific-issues)

---

## Python Issues

### Issue: "Python command not found" or "'python' is not recognized"

**Symptoms:**
```
'python' is not recognized as an internal or external command
-bash: python: command not found
```

**Solution:**

**Option 1: Reinstall Python with PATH enabled (Recommended)**
1. Uninstall Python from Control Panel (Windows) or Applications (macOS)
2. Download Python from https://www.python.org/downloads/
3. **During installation, check the box:** "Add Python to PATH"
4. Click "Install Now"
5. Verify: `python --version`

**Option 2: Add Python to PATH manually (Windows)**
1. Find where Python is installed (usually `C:\Python311`)
2. Right-click "This PC" → "Properties" → "Advanced system settings"
3. Click "Environment Variables"
4. Under "System variables", find "Path" and click "Edit"
5. Click "New" and add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311`
6. Click "OK" and restart terminal
7. Verify: `python --version`

**Option 3: Use python3 (macOS/Linux)**
```bash
python3 --version
# Use python3 instead of python in all commands
```

**Option 4: Use py (Windows Alternative)**
```bash
py --version
# Use py instead of python in commands
```

---

### Issue: "Python is installed but wrong version" or "python --version" shows Python 2.x

**Symptoms:**
```
Python 2.7.18    # Should be Python 3.11.x
```

**Solution:**

1. **Check all Python installations:**

   **Windows:**
   ```bash
   py --list-paths
   ```

   **macOS/Linux:**
   ```bash
   which python
   which python3
   ```

2. **Use specific version:**

   **Windows:**
   ```bash
   py -3.11 --version
   py -3.11 -m pip install package_name
   ```

   **macOS/Linux:**
   ```bash
   python3.11 --version
   python3.11 -m pip install package_name
   ```

3. **Create alias (Optional):**

   **Windows PowerShell:**
   ```powershell
   Set-Alias python "C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\python.exe"
   ```

   **macOS/Linux:**
   ```bash
   alias python=python3.11
   ```

---

### Issue: "pip is not recognized" or "pip install fails"

**Symptoms:**
```
'pip' is not recognized as an internal or external command
pip: command not found
```

**Solution:**

**Option 1: Use pip module (Recommended)**
```bash
python -m pip install --upgrade pip
python -m pip install package_name
```

**Option 2: Reinstall pip**
```bash
# Windows
python -m ensurepip --upgrade

# macOS/Linux
python3 -m ensurepip --upgrade
```

**Option 3: Check pip location**
```bash
# Windows
py -m pip --version

# macOS/Linux
python3 -m pip --version
```

---

## Git & GitHub Issues

### Issue: "Git command not found" or "'git' is not recognized"

**Symptoms:**
```
'git' is not recognized as an internal or external command
-bash: git: command not found
```

**Solution:**

1. **Reinstall Git from https://git-scm.com/downloads**
2. **During installation (Windows):**
   - Select: "Use Git from Git Bash only" (or Windows Command Prompt)
   - Do NOT select "Only Windows Explorer integration"
3. **Restart terminal/PowerShell**
4. **Verify:** `git --version`

**Alternative (Windows):**
Add Git to PATH manually:
1. Find Git installation: Usually `C:\Program Files\Git\bin`
2. Add to PATH (see Python PATH instructions above)
3. Restart terminal

---

### Issue: "fatal: Authentication failed" or "Permission denied"

**Symptoms:**
```
fatal: Authentication failed for 'https://github.com/...'
Permission denied (publickey)
fatal: Could not read from remote repository
```

**Solution:**

**For HTTPS (Personal Access Token):**

1. **Create Personal Access Token (if not done):**
   - Go to https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Check `repo` and `user` scopes
   - Set expiration to 90 days
   - Copy token immediately

2. **Store credentials locally:**

   **Windows (Recommended):**
   ```bash
   git config --global credential.helper wincred
   ```
   Then on next push/pull, enter username and token.

   **macOS:**
   ```bash
   git config --global credential.helper osxkeychain
   ```

   **Linux:**
   ```bash
   git config --global credential.helper store
   ```

3. **Test git operations:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/test.git
   ```

**For SSH (SSH Key):**

1. **Generate SSH key (if not done):**
   ```bash
   ssh-keygen -t ed25519 -C "your-email@example.com"
   ```
   Press Enter for default location, set passphrase (optional)

2. **Add SSH key to GitHub:**
   - Copy key: `cat ~/.ssh/id_ed25519.pub` (macOS/Linux)
   - Go to https://github.com/settings/keys
   - Click "New SSH key"
   - Paste entire key content
   - Click "Add SSH key"

3. **Test SSH:**
   ```bash
   ssh -T git@github.com
   ```

4. **Use SSH for cloning:**
   ```bash
   git clone git@github.com:YOUR_USERNAME/repo.git
   ```

---

### Issue: "fatal: Not a git repository"

**Symptoms:**
```
fatal: Not a git repository (or any of the parent directories): .git
```

**Solution:**

1. **Initialize git repository:**
   ```bash
   cd your_project_folder
   git init
   ```

2. **OR clone existing repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/repo.git
   cd repo
   ```

3. **Verify .git folder exists:**
   ```bash
   ls -la    # Should show .git folder
   ```

---

### Issue: "fatal: origin does not appear to be a 'git' repository"

**Symptoms:**
```
fatal: 'origin' does not appear to be a 'git' repository
fatal: Could not read from remote repository
```

**Solution:**

1. **Check current remote:**
   ```bash
   git remote -v
   ```

2. **If empty, add remote:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   ```

3. **Verify remote added:**
   ```bash
   git remote -v
   ```

4. **Now try push/pull:**
   ```bash
   git push -u origin main
   ```

---

## Visual Studio Code Issues

### Issue: "Command 'code' not found" or "VS Code won't launch from terminal"

**Symptoms:**
```
'code' is not recognized as an internal or external command
-bash: code: command not found
```

**Solution:**

**Windows:**
1. Right-click VS Code installer
2. Run as Administrator
3. Check box: "Add to PATH"
4. Reinstall
5. Restart terminal

**macOS:**
1. Open VS Code
2. Press `Cmd + Shift + P`
3. Type "shell command"
4. Select "Shell Command: Install 'code' command in PATH"
5. Restart terminal
6. Test: `code .`

---

### Issue: "Extensions not installing" or "Extension installation fails"

**Symptoms:**
```
Extension installation failed
Error: Could not install extension
```

**Solution:**

1. **Reload VS Code:**
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
   - Type "Reload Window"
   - Press Enter

2. **Clear extension cache:**

   **Windows:**
   ```bash
   rm -r %userprofile%\.vscode\extensions
   ```

   **macOS:**
   ```bash
   rm -rf ~/.vscode/extensions
   ```

3. **Reinstall extensions:**
   - Open Extensions tab (Ctrl+Shift+X)
   - Search for each extension
   - Click Install

4. **Install from command line:**
   ```bash
   code --install-extension ms-python.python
   code --install-extension ms-python.vscode-pylance
   ```

---

### Issue: "Python interpreter not found" or "Can't select interpreter"

**Symptoms:**
- No Python interpreters shown in list
- Red squiggly lines under Python code
- "IntelliSense not working"

**Solution:**

1. **Verify Python installed:**
   ```bash
   python --version
   ```

2. **Set Python path in VS Code settings:**
   - Press `Ctrl+,` to open Settings
   - Search "python.defaultInterpreterPath"
   - Set to full path:
     - **Windows:** `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\python.exe`
     - **macOS:** `/usr/local/bin/python3.11`

3. **Select interpreter manually:**
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose from list (should see .venv option)

4. **Reinstall Python extension:**
   - Open Extensions (Ctrl+Shift+X)
   - Search "Python"
   - Click the Microsoft Python extension
   - Click Uninstall
   - Click Install

---

### Issue: "Terminal not opening in VS Code" or "integrated terminal fails"

**Symptoms:**
```
Failed to launch the terminal process
Could not start terminal process
```

**Solution:**

1. **Change default shell:**
   - Press `Ctrl+Shift+P`
   - Type "Terminal: Select Default Shell"
   - Choose PowerShell (Windows) or Bash (macOS)

2. **Check terminal settings:**
   - Press `Ctrl+,` (Settings)
   - Search "terminal.integrated.shell"
   - Verify shell path exists

3. **Restart VS Code:**
   - Close VS Code completely
   - Reopen VS Code
   - Try opening terminal again (`Ctrl+``)

---

## Virtual Environment Issues

### Issue: "Virtual environment not activating" or ".venv folder not working"

**Symptoms:**
```
No (.venv) prefix in terminal prompt
python still uses system interpreter
```

**Solution:**

**Windows:**
```bash
# Recreate virtual environment
rmdir .venv /s /q
python -m venv .venv
.venv\Scripts\activate

# Verify activation
python --version    # Should show 3.11.x
where python        # Should show path inside .venv
```

**macOS/Linux:**
```bash
# Recreate virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate

# Verify activation
python --version    # Should show 3.11.x
which python        # Should show path inside .venv
```

---

### Issue: "Permission denied" when activating virtual environment

**Symptoms:**
```
.venv\Scripts\activate: Permission denied
bash: .venv/bin/activate: Permission denied
```

**Solution:**

**Windows:**
```bash
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Give execute permission
chmod +x .venv/bin/activate
source .venv/bin/activate
```

---

### Issue: "ModuleNotFoundError" after activating virtual environment

**Symptoms:**
```
ModuleNotFoundError: No module named 'requests'
```

**Solution:**

1. **Verify virtual environment is activated:**
   - Look for `(.venv)` prefix in terminal
   - Run `which python` (should show .venv path)

2. **Install package in virtual environment:**
   ```bash
   pip install package_name
   ```

3. **Install all dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify package installed:**
   ```bash
   pip list    # Should show package_name
   ```

---

## Network & Firewall Issues

### Issue: "Unable to access github.com" or "GitHub unreachable"

**Symptoms:**
```
Could not resolve hostname
Connection refused
Certificate verification failed
```

**Solution:**

1. **Test network connectivity:**
   ```bash
   ping github.com
   curl https://github.com
   ```

2. **Check firewall settings:**
   - Ensure firewall allows HTTPS (port 443)
   - Add github.com to allowed domains

3. **Configure proxy (if behind corporate proxy):**

   ```bash
   # Windows
   git config --global http.proxy http://proxyuser:proxypass@proxyserver:port
   git config --global https.proxy https://proxyuser:proxypass@proxyserver:port

   # macOS/Linux
   git config --global http.proxy http://proxyuser:proxypass@proxyserver:port
   ```

4. **Test Git connection:**
   ```bash
   git clone https://github.com/test/test.git
   ```

---

### Issue: "pip install fails" or "Cannot fetch packages"

**Symptoms:**
```
ERROR: Could not find a version that satisfies the requirement
Timeout downloading package
403 Forbidden
```

**Solution:**

1. **Test PyPI connectivity:**
   ```bash
   pip install --upgrade pip
   ```

2. **Use different PyPI mirror (if blocked):**
   ```bash
   pip install -i https://pypi.org/simple/ package_name
   ```

3. **Configure pip proxy:**

   Create/edit `~/.pip/pip.conf`:
   ```
   [global]
   proxy = [user:passwd@]proxy.server:port
   index-url = https://pypi.org/simple/
   ```

4. **Clear pip cache:**
   ```bash
   pip cache purge
   pip install package_name
   ```

---

## LLM Endpoint Issues

### Issue: "Cannot connect to LLM endpoint" or "LLM request timeout"

**Symptoms:**
```
Connection refused
Timeout
404 Not Found
401 Unauthorized
```

**Solution:**

1. **Verify endpoint URL:**
   - Double-check URL from trainer
   - Ensure no typos
   - Verify protocol (https://)

2. **Check LLM_ENDPOINT environment variable:**
   ```bash
   # Create .env file with:
   LLM_ENDPOINT=https://your-endpoint-url
   LLM_API_KEY=your-key
   LLM_MODEL=model-name
   ```

3. **Test endpoint connectivity:**
   ```python
   import requests
   import os
   from dotenv import load_dotenv

   load_dotenv()
   endpoint = os.getenv('LLM_ENDPOINT')
   api_key = os.getenv('LLM_API_KEY')

   headers = {"Authorization": f"Bearer {api_key}"}
   response = requests.get(endpoint, headers=headers, timeout=10)
   print(response.status_code)
   print(response.text)
   ```

4. **Check network access:**
   ```bash
   curl -H "Authorization: Bearer YOUR_KEY" https://your-endpoint-url
   ```

5. **Verify credentials:**
   - Confirm API key is valid
   - Check expiration date
   - Ensure correct model name

---

### Issue: "401 Unauthorized" or "Invalid API key"

**Symptoms:**
```
401 Unauthorized
Invalid credentials
Authentication failed
```

**Solution:**

1. **Verify API key in .env:**
   ```bash
   # Check .env file has correct key:
   cat .env
   ```

2. **Check for whitespace issues:**
   ```
   # Make sure no extra spaces:
   LLM_API_KEY=actual_key_no_spaces
   ```

3. **Reload environment variables:**
   ```python
   from dotenv import load_dotenv
   import os
   
   load_dotenv(override=True)  # Force reload
   key = os.getenv('LLM_API_KEY')
   ```

4. **Request new credentials from trainer:**
   - Trainer may need to rotate/regenerate key
   - Ensure key hasn't expired

---

## Package Installation Issues

### Issue: "pip install fails with version conflict"

**Symptoms:**
```
ERROR: pip's dependency resolver does not currently take into account all the packages
There are conflicting dependencies
```

**Solution:**

1. **Upgrade pip:**
   ```bash
   python -m pip install --upgrade pip
   ```

2. **Install with no dependencies:**
   ```bash
   pip install --no-deps package_name
   ```

3. **Use specific version:**
   ```bash
   pip install package_name==1.0.0
   ```

4. **Clear pip cache:**
   ```bash
   pip cache purge
   ```

5. **Start fresh (Nuclear option):**
   ```bash
   # Delete and recreate virtual environment
   rmdir .venv /s /q        # Windows
   rm -rf .venv             # macOS/Linux
   
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # macOS: source .venv/bin/activate
   
   pip install -r requirements.txt
   ```

---

## Validation Script Issues

### Issue: "Validation script fails" or "run_environment_check.py has errors"

**Symptoms:**
```
[✗] Python version check failed
[✗] GitHub access failed
[✗] LLM endpoint unreachable
```

**Solution:**

1. **Run with verbose output:**
   ```bash
   python run_environment_check.py -v
   python run_environment_check.py --verbose
   ```

2. **Check specific component:**
   ```bash
   # Test Python
   python --version
   
   # Test Git
   git --version
   
   # Test GitHub
   git clone https://github.com/test/test.git
   
   # Test LLM
   curl https://your-llm-endpoint
   ```

3. **Check virtual environment:**
   ```bash
   # Ensure .venv is activated
   which python    # Should show .venv path
   python --version
   ```

4. **Check dependencies:**
   ```bash
   pip list
   pip install -r requirements.txt
   ```

---

## Windows-Specific Issues

### Issue: "PowerShell script cannot run" or ".ps1 file won't execute"

**Symptoms:**
```
File cannot be loaded because running scripts is disabled on this system
```

**Solution:**

1. **Run PowerShell as Administrator**
2. **Change execution policy:**
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. **Confirm by typing:** `Y` and press Enter

---

### Issue: "Line endings issues" or "CRLF vs LF mismatch"

**Symptoms:**
```
fatal: CRLF would be replaced by LF
inconsistent line endings
```

**Solution:**

1. **Set Git line ending handling:**
   ```bash
   git config --global core.autocrlf true
   ```

2. **Normalize existing files:**
   ```bash
   git rm --cached -r .
   git add -r .
   git commit -m "Normalize line endings"
   ```

---

## macOS-Specific Issues

### Issue: "Xcode Command Line Tools required"

**Symptoms:**
```
xcrun: error: unable to find utility
git: command not found
```

**Solution:**

1. **Install Xcode Command Line Tools:**
   ```bash
   xcode-select --install
   ```

2. **Accept license:**
   ```bash
   sudo xcode-select --accept-license
   ```

3. **Verify installation:**
   ```bash
   git --version
   python --version
   ```

---

### Issue: "Python not found on macOS" or "python3 required"

**Symptoms:**
```
-bash: python: command not found
```

**Solution:**

1. **Install via Homebrew (Recommended):**
   ```bash
   brew install python@3.11
   ```

2. **Link Python 3.11:**
   ```bash
   brew link python@3.11
   ```

3. **Verify installation:**
   ```bash
   python3.11 --version
   ```

4. **Create alias:**
   ```bash
   echo 'alias python=python3.11' >> ~/.zshrc
   source ~/.zshrc
   ```

---

### Issue: "Permission denied" errors on macOS

**Symptoms:**
```
Permission denied: 'file'
```

**Solution:**

1. **Check file permissions:**
   ```bash
   ls -la filename
   ```

2. **Add execute permission:**
   ```bash
   chmod +x filename
   ```

3. **For directories:**
   ```bash
   chmod -R u+x directory_name
   ```

---

## Getting More Help

### Before Contacting Support

1. **Run validation script with verbose output:**
   ```bash
   python run_environment_check.py -v
   ```

2. **Collect system information:**
   ```bash
   python --version
   pip --version
   git --version
   code --version
   ```

3. **Save error messages:**
   - Take screenshot of error
   - Save full error text

### Contact Information

- **Trainer Email:** [Provided during training]
- **GitHub Issues:** https://github.com/...
- **Python Help:** https://www.python.org/community/
- **VS Code Issues:** https://github.com/microsoft/vscode/issues

### Useful Debug Commands

```bash
# System information
python -c "import platform; print(platform.platform())"

# Python path
python -c "import sys; print(sys.executable)"

# Python paths
python -c "import sys; print('\n'.join(sys.path))"

# Installed packages
pip list

# Git configuration
git config --list

# Virtual environment info
python -c "import sys; print(sys.prefix)"
```

---

**Last Updated:** 2026-09-29  
**Document Version:** 1.0  
**Training Program:** AI-Augmented Product Engineering Program
