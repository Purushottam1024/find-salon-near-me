#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path


def create_venv(venv_path):
    print(f"🔧 Creating virtual environment at {venv_path}...")
    subprocess.check_call([sys.executable, "-m", "venv", str(venv_path)])


def install_package(venv_path):
    pip_path = venv_path / "bin" / "pip"
    print("📦 Installing the tool inside the virtual environment...")
    subprocess.check_call(
        [pip_path, "install", "--upgrade", "pip", "setuptools", "wheel"]
    )
    subprocess.check_call([pip_path, "install", "."])


def offer_alias(venv_path):
    shell = os.environ.get("SHELL", "")
    rc_file = None
    if "bash" in shell:
        rc_file = Path.home() / ".bashrc"
    elif "zsh" in shell:
        rc_file = Path.home() / ".zshrc"

    if rc_file and rc_file.exists():
        alias_line = f'alias salonenv="source {venv_path}/bin/activate"'
        with open(rc_file, "r") as f:
            if alias_line in f.read():
                print("ℹ️  Alias already added to your shell config.")
                return

        print(f"🧩 Adding alias to your {rc_file}...")
        with open(rc_file, "a") as f:
            f.write(f"\n# Salon CLI virtual environment\n{alias_line}\n")
        print("✅ Alias added! Use it by running:\n  salonenv")
    else:
        print("⚠️  Could not detect .bashrc or .zshrc. Please manually add this line:")
        print(f'  alias salonenv="source {venv_path}/bin/activate"')


def main():
    home = Path.home()
    venv_path = home / "salon"

    if not venv_path.exists():
        create_venv(venv_path)
    else:
        print(f"✅ Virtual environment already exists at {venv_path}")

    install_package(venv_path)

    print("\n🎉 Installation complete!")
    print(
        f"👉 To use the tool, run:\n  source {venv_path}/bin/activate && find-salon --help\n"
    )

    offer_alias(venv_path)


if __name__ == "__main__":
    main()
