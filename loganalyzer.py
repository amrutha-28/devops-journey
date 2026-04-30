# Simulate reading log file
logs = [
    "INFO: Server started",
    "ERROR: Database connection failed",
    "INFO: User logged in",
    "ERROR: Disk space low",
    "INFO: Backup completed",
    "ERROR: Service crashed"
]

errors = []
infos = []

for log in logs:
    if "ERROR" in log:
        errors.append(log)
    else:
        infos.append(log)

print(f"Total logs: {len(logs)}")
print(f"INFO count: {len(infos)}")
print(f"ERROR count: {len(errors)}")
print("\n--- ERRORS FOUND ---")
for error in errors:
    print(error)
