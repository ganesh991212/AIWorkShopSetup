# Quick Reference Checklist - Training Setup

**Quick Setup Reference | AI-Augmented Product Engineering Program**

---

## 🚀 Quick Installation Sequence

### Phase 1: System Check (5 mins)
```
[ ] Windows 10/11 or macOS 13+
[ ] 8 GB+ RAM installed
[ ] 10 GB+ free disk space
[ ] Internet connectivity working
```

### Phase 2: Software Installation (30 mins)

#### Python 3.11.x
```bash
# Verify installation
python --version    # Should show: Python 3.11.x
pip --version       # Should show: pip 23.x.x or later
```
**Download:** https://www.python.org/downloads/

#### Git
```bash
# Verify installation
git --version       # Should show: git version 2.42.0+
# Configure globally (one time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
**Download:** https://git-scm.com/downloads

#### Visual Studio Code
```bash
# Verify installation
code --version      # Should show version number
```
**Download:** https://code.visualstudio.com/download

### Phase 3: VS Code Extensions (10 mins)

Open VS Code Extensions tab and install:
```
[ ] Python (Microsoft)
[ ] Pylance (Microsoft)
[ ] GitHub Pull Requests (GitHub)
[ ] Jupyter (Microsoft) - optional
```

Or via terminal:
```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension github.vscode-pull-request-github
code --install-extension ms-toolsai.jupyter
```

### Phase 4: Python Virtual Environment (5 mins)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS
python3 -m venv .venv
source .venv/bin/activate
```

**Verify activation:** Prompt should show `(.venv)`

### Phase 5: GitHub Setup (10 mins)

```bash
# Create account
Visit: https://github.com/signup

# Test git operations
git clone https://github.com/YOUR_USERNAME/test.git
cd test
git add .
git commit -m "test"
git push
```

### Phase 6: Environment Configuration (5 mins)

Create `.env` file in project root:
```
LLM_ENDPOINT=
LLM_API_KEY=
LLM_MODEL=
LLM_API_VERSION=
```

Create `.gitignore`:
```
.env
```

### Phase 7: Validation (5 mins)

```bash
# Run validator script (provided by trainer)
python run_environment_check.py
```

---

## 📋 Pre-Training Validation Commands

Run these commands to verify everything works:

```bash
# 1. Python version
python --version

# 2. Pip version
pip --version

# 3. Git version and config
git --version
git config --list

# 4. Activate virtual environment
# Windows: .venv\Scripts\activate
# macOS: source .venv/bin/activate

# 5. Verify Python in venv
python --version

# 6. Test pip install
pip install requests

# 7. Test git clone
git clone https://github.com/user/repo.git

# 8. Test GitHub credentials
git push

# 9. Run validation script
python run_environment_check.py
```

---

## ✅ Final Readiness Checklist

### System Setup
- [ ] OS: Windows 10/11 or macOS 13+
- [ ] RAM: 8 GB minimum
- [ ] Disk Space: 10 GB free
- [ ] Internet: Stable connection

### Software Installed
- [ ] Python 3.11.x (64-bit)
- [ ] Git (latest stable)
- [ ] Visual Studio Code (latest stable)
- [ ] Browser: Chrome or Edge (latest)

### Python Setup
- [ ] `python --version` → Python 3.11.x ✓
- [ ] `pip --version` → pip 23.x+ ✓
- [ ] Virtual environment created (.venv)
- [ ] Virtual environment activates correctly

### Git Setup
- [ ] `git --version` → git 2.42.0+ ✓
- [ ] User name configured globally ✓
- [ ] User email configured globally ✓
- [ ] GitHub account active ✓
- [ ] Can create private repository ✓

### GitHub Authentication
- [ ] Personal access token created OR SSH key configured
- [ ] Git credentials helper configured
- [ ] Can clone repository (test command)
- [ ] Can push to repository (test command)

### VS Code Setup
- [ ] VS Code installed and launches ✓
- [ ] Python extension installed ✓
- [ ] Pylance extension installed ✓
- [ ] GitHub Pull Requests extension installed ✓
- [ ] Python interpreter set to .venv ✓

### Network Access
- [ ] github.com accessible ✓
- [ ] api.github.com accessible ✓
- [ ] pypi.org accessible ✓
- [ ] files.pythonhosted.org accessible ✓
- [ ] LLM endpoint accessible ✓ (after trainer provides URL)

### Environment Files
- [ ] `.env` file created ✓
- [ ] `.gitignore` contains `.env` ✓
- [ ] Can read environment variables from Python ✓

### Security
- [ ] No credentials in Python files ✓
- [ ] No credentials in GitHub ✓
- [ ] Credentials in `.env` only ✓
- [ ] `.env` excluded from git ✓

### Pre-Training Validation
- [ ] Received validation script ✓
- [ ] Validation script runs successfully ✓
- [ ] All checks pass ✓
- [ ] No errors or warnings ✓

---

## 🔧 Common Issues & Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| `python` command not found | Add Python to PATH: Reinstall with "Add Python to PATH" checked |
| `pip` not found | Run: `python -m pip install --upgrade pip` |
| Git not found | Reinstall Git from https://git-scm.com/downloads |
| VS Code extensions not installing | Reload window: Press `Ctrl+Shift+P` → "Reload Window" |
| Virtual env not activating | Delete `.venv` and recreate: `python -m venv .venv` |
| GitHub auth fails | Check credentials: Use PAT or SSH key (not password) |
| LLM endpoint unreachable | Check network/proxy settings, verify URL from trainer |
| Port 8000/5000 in use | Close other apps using the port, or change port in code |

---

## 🔑 Key Commands Reference

### Python & Virtual Environment
```bash
python --version                    # Check Python version
python -m venv .venv              # Create virtual environment
.venv\Scripts\activate             # Activate (Windows)
source .venv/bin/activate          # Activate (macOS)
pip install package_name            # Install package
pip list                            # List installed packages
pip freeze > requirements.txt       # Save dependencies
pip install -r requirements.txt     # Install from file
deactivate                          # Deactivate venv
```

### Git
```bash
git config --global user.name "Name"        # Set name
git config --global user.email "email"      # Set email
git clone url                               # Clone repository
git add .                                   # Stage all changes
git commit -m "message"                     # Commit changes
git push                                    # Push to GitHub
git pull                                    # Pull from GitHub
git status                                  # Check status
git log --oneline                          # View commit history
```

### VS Code
```bash
code .                              # Open current folder
code --version                      # Check VS Code version
code --install-extension name       # Install extension
Ctrl+Shift+P                       # Open command palette
Ctrl+`                             # Open integrated terminal
Ctrl+,                             # Open settings
```

---

## 📞 Support Resources

### Official Docs
- Python: https://docs.python.org/3.11/
- Git: https://git-scm.com/doc
- VS Code: https://code.visualstudio.com/docs
- GitHub: https://docs.github.com/

### Common Tasks
| Task | Link |
|------|------|
| Python Installation | https://wiki.python.org/moin/BeginnersGuide/Download |
| Git Setup | https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup |
| GitHub Auth | https://docs.github.com/en/authentication |
| VS Code Python | https://code.visualstudio.com/docs/languages/python |

### Troubleshooting
- GitHub Issues: https://support.github.com
- Python Help: https://www.python.org/community/
- VS Code Issues: https://github.com/microsoft/vscode/issues

---

## ⏱️ Expected Setup Time

| Task | Time |
|------|------|
| System verification | 5 min |
| Python installation | 10 min |
| Git installation | 5 min |
| VS Code installation | 10 min |
| VS Code extensions | 5 min |
| Virtual environment | 5 min |
| GitHub setup | 10 min |
| Environment config | 5 min |
| Validation | 5 min |
| **Total** | **~60 min** |

---

## 💾 Important Files & Locations

```
Project Root/
├── .venv/                  # Virtual environment (don't commit)
├── .env                    # Credentials (don't commit)
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
├── src/                   # Your source code
├── tests/                 # Test files
└── README.md             # Project documentation
```

---

## 🚨 Critical Do's and Don'ts

### ✅ DO:
- Use virtual environment for all development
- Store credentials in `.env` file
- Use `.gitignore` to exclude `.env`
- Use personal access token (not password) for GitHub
- Commit frequently with clear messages
- Test before pushing to GitHub
- Use only synthetic/fictional data in training

### ❌ DON'T:
- Don't commit `.env` file to GitHub
- Don't use production credentials for training
- Don't upload real customer/patient data
- Don't store credentials in Python files
- Don't use command-line passwords (use tokens/SSH)
- Don't modify `.gitignore` without understanding
- Don't skip the validation script

---

## 📌 Important Notes

1. **Administrative Access:** May be required during initial software installation
2. **Network Restrictions:** Verify network allows access to github.com, pypi.org, and trainer-provided LLM endpoint
3. **Credentials:** Trainer will provide LLM credentials during training (not now)
4. **Training Materials:** All data is fictional and synthetic
5. **Support:** Contact trainer if validation fails or issues arise

---

**Setup Document Version:** 1.0  
**Last Updated:** 2026-09-29  
**Expected Completion:** 60 minutes  
**Support:** trainer@example.com
