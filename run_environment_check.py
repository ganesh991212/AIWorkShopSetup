#!/usr/bin/env python3
"""
Environment Validation Script for AI-Augmented Product Engineering Program
Validates all prerequisites and system configuration before training
"""

import os
import sys
import subprocess
import platform
import json
from pathlib import Path
from datetime import datetime
import shutil

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class EnvironmentValidator:
    """Comprehensive environment validation for training setup"""

    def __init__(self):
        self.checks_passed = 0
        self.checks_failed = 0
        self.warnings = 0
        self.results = []
        self.start_time = datetime.now()

    def print_header(self, text):
        """Print section header"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}")
        print(f"  {text}")
        print(f"{'='*60}{Colors.ENDC}\n")

    def print_check(self, status, check_name, details=""):
        """Print individual check result"""
        if status == "pass":
            symbol = f"{Colors.GREEN}✓{Colors.ENDC}"
            self.checks_passed += 1
        elif status == "fail":
            symbol = f"{Colors.RED}✗{Colors.ENDC}"
            self.checks_failed += 1
        else:  # warning
            symbol = f"{Colors.YELLOW}⚠{Colors.ENDC}"
            self.warnings += 1

        detail_text = f" ({details})" if details else ""
        print(f"{symbol} {check_name}{detail_text}")

        self.results.append({
            "status": status,
            "check": check_name,
            "details": details,
            "timestamp": datetime.now().isoformat()
        })

    def run_command(self, cmd, shell=False):
        """Run shell command and return output"""
        try:
            result = subprocess.run(
                cmd,
                shell=shell,
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode, result.stdout.strip(), result.stderr.strip()
        except subprocess.TimeoutExpired:
            return -1, "", "Command timeout"
        except Exception as e:
            return -1, "", str(e)

    # ==================== SYSTEM CHECKS ====================

    def check_os(self):
        """Check operating system"""
        self.print_header("1. OPERATING SYSTEM CHECK")

        os_name = platform.system()
        os_version = platform.release()

        if os_name in ["Windows", "Darwin"]:
            self.print_check("pass", f"OS detected: {os_name} {os_version}")
        else:
            self.print_check("fail", f"Unsupported OS: {os_name} (requires Windows or macOS)")

    def check_hardware(self):
        """Check hardware requirements"""
        self.print_header("2. HARDWARE REQUIREMENTS")

        # RAM check
        try:
            import psutil
            ram_gb = psutil.virtual_memory().total / (1024**3)
            if ram_gb >= 8:
                self.print_check("pass", f"RAM: {ram_gb:.1f} GB", "Meets minimum 8 GB")
            else:
                self.print_check("fail", f"RAM: {ram_gb:.1f} GB", "Below minimum 8 GB")
        except ImportError:
            self.print_check("warning", "RAM check skipped", "psutil not installed")

        # Disk space check
        try:
            import shutil
            disk_usage = shutil.disk_usage("/")
            free_gb = disk_usage.free / (1024**3)
            if free_gb >= 10:
                self.print_check("pass", f"Free disk space: {free_gb:.1f} GB", "Meets minimum 10 GB")
            else:
                self.print_check("fail", f"Free disk space: {free_gb:.1f} GB", "Below minimum 10 GB")
        except Exception as e:
            self.print_check("warning", "Disk space check failed", str(e))

    # ==================== PYTHON CHECKS ====================

    def check_python(self):
        """Check Python installation and version"""
        self.print_header("3. PYTHON INSTALLATION")

        # Check Python in PATH
        code, version_out, err = self.run_command("python --version", shell=True)

        if code == 0:
            version_str = version_out.split()[-1]
            if version_str.startswith("3.11"):
                self.print_check("pass", "Python installed", f"Version {version_str}")
            else:
                self.print_check("fail", "Python version mismatch", f"Found {version_str}, need 3.11.x")
        else:
            self.print_check("fail", "Python not found", "Run: python --version")

    def check_pip(self):
        """Check pip installation"""
        self.print_header("4. PIP INSTALLATION")

        code, version_out, err = self.run_command("pip --version", shell=True)

        if code == 0:
            self.print_check("pass", "Pip installed", version_out.split()[1])
        else:
            self.print_check("fail", "Pip not found", "Run: python -m pip install --upgrade pip")

    def check_python_in_path(self):
        """Check if Python executable is in PATH"""
        self.print_header("5. PYTHON PATH CONFIGURATION")

        python_path = shutil.which("python")
        if python_path:
            self.print_check("pass", "Python in PATH", python_path)
        else:
            self.print_check("fail", "Python not in PATH", "See TROUBLESHOOTING_GUIDE.md")

    # ==================== GIT CHECKS ====================

    def check_git(self):
        """Check Git installation"""
        self.print_header("6. GIT INSTALLATION")

        code, version_out, err = self.run_command("git --version", shell=True)

        if code == 0:
            self.print_check("pass", "Git installed", version_out)
        else:
            self.print_check("fail", "Git not found", "Install from https://git-scm.com/downloads")

    def check_git_config(self):
        """Check Git configuration"""
        self.print_header("7. GIT CONFIGURATION")

        # Check user name
        code, name_out, err = self.run_command("git config --global user.name", shell=True)
        if code == 0 and name_out:
            self.print_check("pass", "Git user name configured", name_out)
        else:
            self.print_check("fail", "Git user name not configured",
                           "Run: git config --global user.name 'Your Name'")

        # Check user email
        code, email_out, err = self.run_command("git config --global user.email", shell=True)
        if code == 0 and email_out:
            self.print_check("pass", "Git user email configured", email_out)
        else:
            self.print_check("fail", "Git user email not configured",
                           "Run: git config --global user.email 'your@email.com'")

    # ==================== VS CODE CHECKS ====================

    def check_vscode(self):
        """Check Visual Studio Code installation"""
        self.print_header("8. VISUAL STUDIO CODE INSTALLATION")

        code, version_out, err = self.run_command("code --version", shell=True)

        if code == 0:
            version = version_out.split('\n')[0]
            self.print_check("pass", "VS Code installed", f"Version {version}")
        else:
            self.print_check("fail", "VS Code not found", "Install from https://code.visualstudio.com")

    def check_vscode_extensions(self):
        """Check required VS Code extensions"""
        self.print_header("9. VS CODE EXTENSIONS")

        required_extensions = [
            ("ms-python.python", "Python"),
            ("ms-python.vscode-pylance", "Pylance"),
            ("github.vscode-pull-request-github", "GitHub Pull Requests"),
        ]

        code, extensions_out, err = self.run_command("code --list-extensions", shell=True)

        if code == 0:
            extensions_list = extensions_out.lower()
            for ext_id, ext_name in required_extensions:
                if ext_id.lower() in extensions_list:
                    self.print_check("pass", f"{ext_name} extension", "Installed")
                else:
                    self.print_check("fail", f"{ext_name} extension",
                                   f"Run: code --install-extension {ext_id}")
        else:
            self.print_check("warning", "Could not check extensions", "Check manually in VS Code")

    # ==================== VIRTUAL ENVIRONMENT CHECKS ====================

    def check_venv(self):
        """Check Python virtual environment"""
        self.print_header("10. PYTHON VIRTUAL ENVIRONMENT")

        venv_path = Path(".venv")

        if venv_path.exists():
            if (venv_path / "pyvenv.cfg").exists():
                self.print_check("pass", "Virtual environment exists", ".venv folder found")
            else:
                self.print_check("fail", "Virtual environment invalid", ".venv/pyvenv.cfg not found")
        else:
            self.print_check("fail", "Virtual environment not found",
                           "Run: python -m venv .venv")

    def check_venv_activation(self):
        """Check if running in virtual environment"""
        self.print_header("11. VIRTUAL ENVIRONMENT ACTIVATION")

        in_venv = hasattr(sys, 'real_prefix') or (
            hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
        )

        if in_venv:
            self.print_check("pass", "Running in virtual environment", sys.prefix)
        else:
            self.print_check("warning", "Not running in virtual environment",
                           "Activate: .venv\\Scripts\\activate (Windows) or source .venv/bin/activate (macOS)")

    # ==================== GITHUB CHECKS ====================

    def check_github_access(self):
        """Check GitHub connectivity"""
        self.print_header("12. GITHUB CONNECTIVITY")

        code, output, err = self.run_command("git ls-remote --heads https://github.com/github/hello-world.git",
                                            shell=True)

        if code == 0:
            self.print_check("pass", "GitHub HTTPS accessible", "Can reach github.com")
        else:
            self.print_check("fail", "GitHub not accessible", "Check network/firewall settings")

    def check_github_credentials(self):
        """Check GitHub authentication setup"""
        self.print_header("13. GITHUB AUTHENTICATION")

        # This is harder to test without actually cloning, so we'll check if credential helper is set
        code, cred_helper, err = self.run_command("git config --global credential.helper", shell=True)

        if code == 0 and cred_helper:
            self.print_check("pass", "Credential helper configured", cred_helper)
        else:
            self.print_check("warning", "Credential helper not configured",
                           "Configure: git config --global credential.helper wincred (Windows) or osxkeychain (macOS)")

    # ==================== NETWORK CHECKS ====================

    def check_network_access(self):
        """Check access to required network resources"""
        self.print_header("14. NETWORK ACCESS")

        domains = [
            ("github.com", "GitHub"),
            ("api.github.com", "GitHub API"),
            ("pypi.org", "PyPI"),
            ("files.pythonhosted.org", "Python Hosted"),
        ]

        try:
            import urllib.request
            for domain, name in domains:
                try:
                    urllib.request.urlopen(f"https://{domain}", timeout=5)
                    self.print_check("pass", f"{name} ({domain})", "Accessible")
                except Exception as e:
                    self.print_check("fail", f"{name} ({domain})", "Not accessible - Check firewall/proxy")
        except ImportError:
            self.print_check("warning", "Network check skipped", "urllib not available")

    # ==================== ENVIRONMENT FILES CHECKS ====================

    def check_env_file(self):
        """Check .env file setup"""
        self.print_header("15. ENVIRONMENT FILES")

        env_path = Path(".env")
        gitignore_path = Path(".gitignore")

        if env_path.exists():
            self.print_check("pass", ".env file exists", "Found")
        else:
            self.print_check("fail", ".env file missing", "Create: .env file with LLM credentials")

        if gitignore_path.exists():
            with open(gitignore_path, 'r') as f:
                content = f.read()
                if ".env" in content:
                    self.print_check("pass", ".env in .gitignore", "Secured from git")
                else:
                    self.print_check("fail", ".env not in .gitignore", "Add .env to .gitignore")
        else:
            self.print_check("warning", ".gitignore file missing", "Create .gitignore with .env entry")

    # ==================== PACKAGE CHECKS ====================

    def check_required_packages(self):
        """Check for commonly required packages"""
        self.print_header("16. PYTHON PACKAGES")

        packages = [
            ("python-dotenv", "python-dotenv"),
            ("requests", "requests"),
            ("pytest", "pytest"),
        ]

        for package_name, import_name in packages:
            code, output, err = self.run_command(f"pip show {package_name}", shell=True)

            if code == 0:
                self.print_check("pass", f"Package: {package_name}", "Installed")
            else:
                self.print_check("warning", f"Package: {package_name}",
                               f"Not installed (run: pip install {package_name})")

    # ==================== SYSTEM TOOLS CHECKS ====================

    def check_system_tools(self):
        """Check for other useful system tools"""
        self.print_header("17. SYSTEM TOOLS")

        tools = [
            ("curl", "curl --version", "curl"),
            ("grep", "grep --version", "grep"),
        ]

        for tool_name, cmd, display_name in tools:
            code, output, err = self.run_command(cmd, shell=True)

            if code == 0:
                self.print_check("pass", f"{display_name} available", "Found")
            else:
                self.print_check("warning", f"{display_name} not found", "Optional tool")

    # ==================== LOCAL APPLICATION CHECKS ====================

    def check_localhost_ports(self):
        """Check availability of common localhost ports"""
        self.print_header("18. LOCAL PORTS AVAILABILITY")

        ports = [8000, 5000, 3000, 8080]

        try:
            import socket
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(('localhost', port))
                sock.close()

                if result != 0:
                    self.print_check("pass", f"Port {port}", "Available")
                else:
                    self.print_check("warning", f"Port {port}", "In use - may need to change")
        except Exception as e:
            self.print_check("warning", "Port check failed", str(e))

    # ==================== SUMMARY ====================

    def print_summary(self):
        """Print validation summary"""
        self.print_header("VALIDATION SUMMARY")

        total_checks = self.checks_passed + self.checks_failed + self.warnings
        pass_pct = (self.checks_passed / total_checks * 100) if total_checks > 0 else 0

        print(f"{Colors.GREEN}✓ Passed: {self.checks_passed}{Colors.ENDC}")
        print(f"{Colors.RED}✗ Failed: {self.checks_failed}{Colors.ENDC}")
        print(f"{Colors.YELLOW}⚠ Warnings: {self.warnings}{Colors.ENDC}")
        print(f"\n{Colors.BOLD}Total Checks: {total_checks}")
        print(f"Success Rate: {pass_pct:.1f}%{Colors.ENDC}\n")

        if self.checks_failed == 0:
            print(f"{Colors.GREEN}{Colors.BOLD}✓ ALL CHECKS PASSED - ENVIRONMENT READY!{Colors.ENDC}\n")
            return True
        else:
            print(f"{Colors.RED}{Colors.BOLD}✗ {self.checks_failed} CHECKS FAILED - SEE ABOVE FOR DETAILS{Colors.ENDC}\n")
            return False

    def save_report(self):
        """Save validation report to file"""
        report_file = Path("environment_validation_report.json")

        report = {
            "timestamp": self.start_time.isoformat(),
            "duration_seconds": (datetime.now() - self.start_time).total_seconds(),
            "summary": {
                "passed": self.checks_passed,
                "failed": self.checks_failed,
                "warnings": self.warnings,
                "total": self.checks_passed + self.checks_failed + self.warnings
            },
            "system": {
                "os": platform.system(),
                "os_version": platform.release(),
                "python_version": platform.python_version(),
                "platform": platform.platform()
            },
            "checks": self.results
        }

        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"{Colors.CYAN}Report saved to: {report_file}{Colors.ENDC}\n")

    def run_all_checks(self):
        """Run all validation checks"""
        print(f"\n{Colors.BOLD}{Colors.HEADER}")
        print("╔════════════════════════════════════════════════════════╗")
        print("║  AI-Augmented Product Engineering Program             ║")
        print("║  Environment Validation & Setup Review                ║")
        print("║  Caliber Training - Prerequisites Check               ║")
        print("╚════════════════════════════════════════════════════════╝")
        print(f"{Colors.ENDC}")

        # Run all checks
        self.check_os()
        self.check_hardware()
        self.check_python()
        self.check_pip()
        self.check_python_in_path()
        self.check_git()
        self.check_git_config()
        self.check_vscode()
        self.check_vscode_extensions()
        self.check_venv()
        self.check_venv_activation()
        self.check_github_access()
        self.check_github_credentials()
        self.check_network_access()
        self.check_env_file()
        self.check_required_packages()
        self.check_system_tools()
        self.check_localhost_ports()

        # Print summary and save report
        success = self.print_summary()
        self.save_report()

        return success


def main():
    """Main entry point"""
    validator = EnvironmentValidator()
    success = validator.run_all_checks()

    print(f"{Colors.BOLD}Next Steps:{Colors.ENDC}")
    if success:
        print("1. ✓ Your environment is ready for training!")
        print("2. Review the documentation in the project folder")
        print("3. Contact your trainer with any remaining questions")
    else:
        print("1. Review failed checks above")
        print("2. Check TROUBLESHOOTING_GUIDE.md for solutions")
        print("3. Contact your trainer if issues persist")

    print(f"\n{Colors.CYAN}Documentation available:{Colors.ENDC}")
    print("  • INSTALLATION_GUIDE.md - Detailed setup instructions")
    print("  • QUICK_REFERENCE_CHECKLIST.md - Quick commands & checklist")
    print("  • TROUBLESHOOTING_GUIDE.md - Problem solving guide")
    print("  • README_SETUP.md - Navigation and overview")
    print()

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
