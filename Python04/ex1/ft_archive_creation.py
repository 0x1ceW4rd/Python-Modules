#!/usr/bin/env python3

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
try:
    f_write = open("new_discovery.txt", "w")

    print(f"Initializing new storage unit: {f_write.name}")
    print("Storage unit created successfully...")
    print()
    print("Inscribing preservation data...")

    f_write.write(
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee"
    )
    f_write.close()
    f_read = open("new_discovery.txt", "r")
    print(f_read.read())
    f_read.close()
    print()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{f_read.name}' ready for long-term preservation.")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
