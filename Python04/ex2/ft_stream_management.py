#!/usr/bin/env python3

import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

input1 = str(input("Input Stream active. Enter archivist ID: "))

input2 = str(input("Input Stream active. Enter status report: "))

print()

sys.stdout.write(f"[STANDARD] Archive status from {input1}: {input2}\n")

sys.stderr.write("[ALERT] System diagnostic: "
                 "Communication channels verified\n")

sys.stdout.write("[STANDARD] Data transmission complete\n")


print("Three-channel communication test successful.")
