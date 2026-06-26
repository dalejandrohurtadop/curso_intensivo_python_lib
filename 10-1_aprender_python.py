from pathlib import Path

path = Path('cap10/apredender_python.txt')
contents = path.read_text(encoding="utf-8")
print(contents)

lines = contents.splitlines()
pi_string = ""

for line in lines:
    pi_string += line.rstrip()

print(pi_string)