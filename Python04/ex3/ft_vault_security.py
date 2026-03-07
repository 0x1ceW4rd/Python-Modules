#!/usr/bin/env python3

print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

with open("classified_data.txt", "r") as f1:
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    print(f1.read())
print()
with open("security_protocols.txt", "w") as f2:
    print("SECURE PRESERVATION:")
    f2.write("Hi Bob")
print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")
