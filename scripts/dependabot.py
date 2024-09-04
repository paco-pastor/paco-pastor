import json
import subprocess

from termcolor import cprint

output = subprocess.check_output(["pip", "list", "--outdated", "--format", "json"])
outdated_packages = json.loads(output)

with open("requirements.txt", "r") as file:
    requirements = file.readlines()

required_packages = {}
for line in requirements:
    if "==" in line:
        required_packages[line.split("==")[0]] = line.split("==")[1].strip()

print("Outdated packages:\n")
to_update = []
for package in outdated_packages:
    if package["name"] in required_packages:
        to_update.append(package)
        print(package["name"], end=" ")
        cprint(package["version"], "red", end="")
        print(" -> ", end="")
        cprint(package["latest_version"], "green")

if to_update:
    print(f"Please use the following comand to update packages :")
    cprint(f"pip install {" ".join([p["name"] for p in to_update])} --upgrade", "green")
else:
    print("All packages are up to date.")
