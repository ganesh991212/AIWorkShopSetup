#!/usr/bin/env python3
"""
Automated Implementation & Fixes for Environment Setup
Fixes issues identified by environment validation script
"""

import os
import sys
import subprocess
import platform
from pathlib import Path
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class EnvironmentFixer:
    """Implement fixes for environment issues"""

    def __init__(self):
        self.fixes_applied = 0
        self.fixes_failed = 0
        self.start_time = datetime.now()

    def print_header(self, text):
        """Print section header"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}")
        print(f"  {text}")
        print(f"{'='*60}{Colors.ENDC}\n")

    def print_action(self, action, details=""):
        """Print action being taken"""
        detail_text = f" {details}" if details else ""
        print(f"{Colors.CYAN}→ {action}{detail_text}{Colors.ENDC}")

    def print_success(self, message):
        """Print success message"""
        print(f"{Colors.GREEN}✓ {message}{Colors.ENDC}")
        self.fixes_applied += 1

    def print_error(self, message):
        """Print error message"""
        print(f"{Colors.RED}✗ {message}{Colors.ENDC}")
        self.fixes_failed += 1

    def print_warning(self, message):
        """Print warning message"""
        print(f"{Colors.YELLOW}⚠ {message}{Colors.ENDC}")

    def run_command(self, cmd, shell=False, verbose=True):
        """Run shell command"""
        try:
            if verbose:
                self.print_action(f"Running: {cmd}")

            result = subprocess.run(
                cmd,
                shell=shell,
                capture_output=True,
                text=True,
                timeout=60
            )

            return result.returncode, result.stdout.strip(), result.stderr.strip()
        except subprocess.TimeoutExpired:
            return -1, "", "Command timeout"
        except Exception as e:
            return -1, "", str(e)

    # ==================== FIX 1: Virtual Environment ====================

    def fix_virtual_environment(self):
        """Create Python virtual environment"""
        self.print_header("FIX 1: CREATING VIRTUAL ENVIRONMENT")

        venv_path = Path(".venv")

        if venv_path.exists():
            self.print_warning("Virtual environment already exists at .venv")
            return True

        self.print_action("Creating virtual environment")

        code, output, err = self.run_command("python -m venv .venv")

        if code == 0:
            self.print_success("Virtual environment created successfully")
            self.print_action("Note", "Activate with: .venv\\Scripts\\activate")
            return True
        else:
            self.print_error(f"Failed to create virtual environment: {err}")
            return False

    # ==================== FIX 2: .env File ====================

    def fix_env_file(self):
        """Create .env file"""
        self.print_header("FIX 2: CREATING .ENV FILE")

        env_path = Path(".env")

        if env_path.exists():
            self.print_warning(".env file already exists")
            return True

        self.print_action("Creating .env file with template")

        env_template = """# LLM Configuration
# Add your LLM credentials below (provided by trainer)
LLM_ENDPOINT=
LLM_API_KEY=
LLM_MODEL=
LLM_API_VERSION=

# Other environment variables can be added here
# Note: This file should NEVER be committed to GitHub
# It's excluded by .gitignore
"""

        try:
            with open(env_path, 'w') as f:
                f.write(env_template)

            self.print_success(".env file created")
            self.print_action("Note", "Fill in LLM credentials when trainer provides them")
            return True
        except Exception as e:
            self.print_error(f"Failed to create .env file: {e}")
            return False

    # ==================== FIX 3: .gitignore ====================

    def fix_gitignore(self):
        """Create or update .gitignore"""
        self.print_header("FIX 3: CREATING/UPDATING .gitignore")

        gitignore_path = Path(".gitignore")

        gitignore_content = """# Environment variables (credentials)
.env
.env.local

# Virtual environment
.venv/
venv/
env/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
.coverage
htmlcov/

# Logs
*.log
logs/

# IDE settings (VS Code specific)
.vscode/settings.json
.vscode/launch.json
"""

        try:
            if gitignore_path.exists():
                with open(gitignore_path, 'r') as f:
                    content = f.read()
                    if '.env' in content:
                        self.print_warning(".gitignore already has .env entry")
                        return True
                    else:
                        self.print_action("Updating .gitignore to include .env")
                        with open(gitignore_path, 'a') as f:
                            f.write("\n# Environment files\n.env\n")
            else:
                self.print_action("Creating .gitignore")
                with open(gitignore_path, 'w') as f:
                    f.write(gitignore_content)

            self.print_success(".gitignore created/updated")
            return True
        except Exception as e:
            self.print_error(f"Failed to create .gitignore: {e}")
            return False

    # ==================== FIX 4: Git Credential Helper ====================

    def fix_git_credentials(self):
        """Configure Git credential helper"""
        self.print_header("FIX 4: CONFIGURING GIT CREDENTIALS")

        self.print_action("Checking current system", platform.system())

        if platform.system() == "Windows":
            cred_helper = "wincred"
        elif platform.system() == "Darwin":  # macOS
            cred_helper = "osxkeychain"
        else:
            cred_helper = "store"

        self.print_action(f"Setting credential helper to: {cred_helper}")

        code, output, err = self.run_command(
            f"git config --global credential.helper {cred_helper}"
        )

        if code == 0:
            self.print_success(f"Git credential helper configured: {cred_helper}")
            self.print_action("Note", "You'll be prompted for credentials on first git operation")
            return True
        else:
            self.print_error(f"Failed to configure credential helper: {err}")
            return False

    # ==================== FIX 5: Install Required Packages ====================

    def fix_required_packages(self):
        """Install required Python packages"""
        self.print_header("FIX 5: INSTALLING REQUIRED PACKAGES")

        packages = [
            ("python-dotenv", "Environment variable management"),
            ("requests", "HTTP library"),
            ("pytest", "Testing framework"),
        ]

        self.print_action("Note", "Installing to system Python (not virtual environment)")
        self.print_action("Reminder", "Activate .venv before running pip in your project")

        for package, description in packages:
            self.print_action(f"Installing {package}", f"({description})")

            code, output, err = self.run_command(f"pip install {package}")

            if code == 0:
                self.print_success(f"{package} installed successfully")
            else:
                self.print_warning(f"Failed to install {package}, will try again in venv")

    # ==================== FIX 6: Install Optional Packages ====================

    def fix_optional_packages(self):
        """Install optional but useful packages"""
        self.print_header("FIX 6: INSTALLING OPTIONAL PACKAGES")

        optional_packages = [
            ("psutil", "System monitoring (for validation checks)"),
        ]

        for package, description in optional_packages:
            self.print_action(f"Installing {package}", f"({description})")

            code, output, err = self.run_command(f"pip install {package}")

            if code == 0:
                self.print_success(f"{package} installed successfully")
            else:
                self.print_warning(f"Optional package {package} failed (non-critical)")

    # ==================== FIX 7: Create Project Structure ====================

    def fix_project_structure(self):
        """Create recommended project structure"""
        self.print_header("FIX 7: CREATING PROJECT STRUCTURE")

        directories = [
            "src",
            "tests",
            "docs",
            "data",
        ]

        for directory in directories:
            dir_path = Path(directory)

            if dir_path.exists():
                self.print_warning(f"Directory {directory} already exists")
            else:
                self.print_action(f"Creating directory", directory)
                dir_path.mkdir(parents=True, exist_ok=True)

                # Create __init__.py for Python packages
                if directory in ["src", "tests"]:
                    init_file = dir_path / "__init__.py"
                    init_file.touch()

                self.print_success(f"Created {directory}/")

    # ==================== FIX 8: Create Requirements.txt ====================

    def fix_requirements_txt(self):
        """Create requirements.txt file"""
        self.print_header("FIX 8: CREATING requirements.txt")

        req_path = Path("requirements.txt")

        if req_path.exists():
            self.print_warning("requirements.txt already exists")
            return True

        self.print_action("Creating requirements.txt")

        requirements_content = """# AI-Augmented Product Engineering Program
# Python Dependencies

# Environment Management
python-dotenv==1.0.0

# HTTP & Networking
requests==2.31.0

# Testing
pytest==7.4.0
pytest-cov==4.1.0

# Development
black==23.7.0
flake8==6.1.0
pylint==2.17.5

# Data Processing (if needed)
# pandas==2.0.3
# numpy==1.24.3

# LLM Integration (update with trainer provided packages)
# openai==0.27.8
# anthropic==0.7.0

# Add other dependencies as needed during training
"""

        try:
            with open(req_path, 'w') as f:
                f.write(requirements_content)

            self.print_success("requirements.txt created")
            self.print_action("Note", "Install with: pip install -r requirements.txt (in .venv)")
            return True
        except Exception as e:
            self.print_error(f"Failed to create requirements.txt: {e}")
            return False

    # ==================== FIX 9: Create README.md ====================

    def fix_readme(self):
        """Create README.md for project"""
        self.print_header("FIX 9: CREATING PROJECT README.md")

        readme_path = Path("README.md")

        if readme_path.exists():
            self.print_warning("README.md already exists")
            return True

        self.print_action("Creating README.md")

        readme_content = """# AI-Augmented Product Engineering Program

Training project for Caliber Training - AI-Augmented Product Engineering

## Prerequisites

- Python 3.11.x
- Git
- Visual Studio Code
- Virtual environment (.venv)

## Setup Instructions

1. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   - Create `.env` file with LLM credentials
   - Keep `.env` out of git (already in .gitignore)

4. **Run Validation**
   ```bash
   python run_environment_check.py
   ```

## Project Structure

```
.
├── src/              # Source code
├── tests/            # Test files
├── docs/             # Documentation
├── data/             # Data files
├── .env              # Environment variables (not in git)
├── .gitignore        # Git ignore rules
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Running Tests

```bash
pytest tests/
pytest -v --cov=src tests/  # With coverage
```

## Development Workflow

1. Create feature branch: `git checkout -b feature/my-feature`
2. Make changes and commit: `git commit -m "description"`
3. Push to GitHub: `git push origin feature/my-feature`
4. Create Pull Request on GitHub

## Troubleshooting

See `TROUBLESHOOTING_GUIDE.md` for common issues and solutions.

See `INSTALLATION_GUIDE.md` for detailed setup instructions.

## Support

Contact your trainer for questions or issues.

## Training Resources

- `INSTALLATION_GUIDE.md` - Complete installation guide
- `QUICK_REFERENCE_CHECKLIST.md` - Quick commands reference
- `TROUBLESHOOTING_GUIDE.md` - Problem solving guide
- `README_SETUP.md` - Documentation navigation

---

**Program:** AI-Augmented Product Engineering Program
**Training:** Caliber Training
**Created:** 2026-09-29
"""

        try:
            with open(readme_path, 'w') as f:
                f.write(readme_content)

            self.print_success("README.md created")
            return True
        except Exception as e:
            self.print_error(f"Failed to create README.md: {e}")
            return False

    # ==================== FIX 10: Verify Git Configuration ====================

    def fix_git_verification(self):
        """Verify and display Git configuration"""
        self.print_header("FIX 10: VERIFYING GIT CONFIGURATION")

        configs = [
            ("user.name", "Git User Name"),
            ("user.email", "Git User Email"),
            ("credential.helper", "Credential Helper"),
        ]

        for config_key, config_name in configs:
            code, value, err = self.run_command(
                f"git config --global {config_key}",
                verbose=False
            )

            if code == 0 and value:
                self.print_success(f"{config_name}: {value}")
            else:
                self.print_warning(f"{config_name}: Not configured")

    # ==================== SUMMARY ====================

    def print_summary(self):
        """Print fix summary"""
        self.print_header("IMPLEMENTATION SUMMARY")

        print(f"{Colors.GREEN}✓ Fixes Applied: {self.fixes_applied}{Colors.ENDC}")
        print(f"{Colors.RED}✗ Fixes Failed: {self.fixes_failed}{Colors.ENDC}")
        print(f"\n{Colors.BOLD}Total Fixes: {self.fixes_applied + self.fixes_failed}")

        duration = (datetime.now() - self.start_time).total_seconds()
        print(f"Time Taken: {duration:.1f} seconds{Colors.ENDC}\n")

        if self.fixes_failed == 0:
            print(f"{Colors.GREEN}{Colors.BOLD}✓ ALL IMPLEMENTATIONS COMPLETED SUCCESSFULLY!{Colors.ENDC}\n")
            return True
        else:
            print(f"{Colors.YELLOW}{Colors.BOLD}⚠ Some implementations had issues - see above{Colors.ENDC}\n")
            return False

    def print_next_steps(self):
        """Print next steps"""
        self.print_header("NEXT STEPS")

        print(f"{Colors.BOLD}1. Activate Virtual Environment:{Colors.ENDC}")
        if platform.system() == "Windows":
            print(f"   .venv\\Scripts\\activate\n")
        else:
            print(f"   source .venv/bin/activate\n")

        print(f"{Colors.BOLD}2. Install Project Dependencies:{Colors.ENDC}")
        print(f"   pip install -r requirements.txt\n")

        print(f"{Colors.BOLD}3. Add LLM Credentials (when trainer provides them):{Colors.ENDC}")
        print(f"   Edit .env file with your LLM configuration\n")

        print(f"{Colors.BOLD}4. Run Validation Again:{Colors.ENDC}")
        print(f"   python run_environment_check.py\n")

        print(f"{Colors.BOLD}5. Review Documentation:{Colors.ENDC}")
        print(f"   • README.md - Project overview")
        print(f"   • INSTALLATION_GUIDE.md - Detailed setup")
        print(f"   • QUICK_REFERENCE_CHECKLIST.md - Quick commands\n")

    def run_all_fixes(self):
        """Run all fixes"""
        print(f"\n{Colors.BOLD}{Colors.HEADER}")
        print("╔════════════════════════════════════════════════════════╗")
        print("║  Environment Setup - Automated Implementation          ║")
        print("║  Fixing Issues Identified by Validation Script        ║")
        print("╚════════════════════════════════════════════════════════╝")
        print(f"{Colors.ENDC}")

        # Run all fixes
        self.fix_virtual_environment()
        self.fix_env_file()
        self.fix_gitignore()
        self.fix_git_credentials()
        self.fix_required_packages()
        self.fix_optional_packages()
        self.fix_project_structure()
        self.fix_requirements_txt()
        self.fix_readme()
        self.fix_git_verification()

        # Print summary and next steps
        success = self.print_summary()
        self.print_next_steps()

        return success


def main():
    """Main entry point"""
    fixer = EnvironmentFixer()
    success = fixer.run_all_fixes()

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
