from pathlib import Path

path = Path("cap10/pi_dig.txt")
contents = path.read_text(encoding="utf-8")
print(contents)