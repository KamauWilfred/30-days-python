import os
from pathlib import Path
import subprocess

print(os.getcwd())
print(os.name)

folder = Path.home()

print(folder)
print("Exists?: ", folder.exists())

commands = subprocess.run(
    ["python3", "--version"],
    capture_output=True,
    text=True
)

print("Output: ", commands.stdout)
print("Errors: ", commands.stderr)
print("Exit code: ", commands.returncode)

directory = input(f"\nEnter directory path: ")
path = Path(directory)

if path.exists():
    if path.is_dir():
        for item in path.iterdir():
            print(item)

    else:
        print("Path exists but is not a directory.")

else:
    print("Directory does not exist!")

home = os.getenv("HOME")
print(f"\nHome environment variable: ", home)

