from pathlib import Path

directory = Path("/home/rubai/Python/projects/nova")

for entry in directory.iterdir():
    print(entry.name)