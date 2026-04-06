#!/usr/bin/env python3
import os
import sys

py_path = sys.executable
if sys.prefix == sys.base_prefix:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {py_path}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")

    print("Then run this program again.")
else:
    venv_path = sys.prefix
    venv_name = os.path.basename(venv_path)
    print("MATRIX STATUS: Welcome to the construct")
    print(f"\nCurrent Python: {py_path}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting\nthe global system.")
    print("\nPackage installation path:")
    print(sys.path[-1])
