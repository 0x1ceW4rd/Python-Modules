#!/usr/bin/env python3

print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

try:
    file_name = "lost_archive.txt"
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")
except PermissionError:
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")
except Exception as e:
    print(e)

print()

try:
    file_name = "classified_vault.txt"
    with open(file_name, "r") as file:
        file.read()
except FileNotFoundError:
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")
except PermissionError:
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")


print()
try:
    file_name = "standard_archive.txt"
    with open(file_name, "r") as file:
        print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
        print(f"SUCCESS: Archive recovered - ``{file.read()}''")
        print("STATUS: Normal operations resumed")
except FileNotFoundError:
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")
except PermissionError:
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")

print()
print("All crisis scenarios handled successfully. Archives secure.")
