import importlib
import sys

print("\nLOADING STATUS: Loading programs...\n")
print("Checking dependencies:")

modules = ["numpy", "matplotlib", "pandas"]
error = []
for m in modules:
    try:
        mod = importlib.import_module(m)
        print(f"[OK] {mod.__name__} ({mod.__version__}) "
              "- Data manipulation ready")
    except ImportError:
        error.append(m)
if error:
    print("Missing dependencies: ", end="")
    for e in error:
        if len(error) > 1:
            print(", ".join(error))
        else:
            print(e)
    print(
        "Please install with: \n"
        "pip install -r requirements.txt \nor\n"
        "poetry install"
    )
    sys.exit(1)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # type: ignore

print("\nAnalyzing Matrix data...")
matrix_data = np.random.rand(1000)

df = pd.DataFrame(matrix_data, columns=["Matrix_Value"])

print("Processing 1000 data points...")
print("Generating visualization...")


plt.hist(df["Matrix_Value"], bins=30, edgecolor="black", histtype="barstacked")
plt.title("Distribution of 1000 Matrix Data Points")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("matrix_analysis.png")
print("\nAnalysis complete!\nResults saved to: matrix_analysis.png")
