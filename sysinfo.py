import os
import datetime

print("========== SYSTEM INFO ==========")
print(f"Date: {datetime.datetime.now()}")
print(f"User: {os.getenv('USER')}")
print(f"Home: {os.getenv('HOME')}")
print("=================================")
