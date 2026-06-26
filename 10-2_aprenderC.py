from pathlib import Path

path = Path('cap10/apredender_python.txt')
contents = path.read_text(encoding="utf-8")
mensage = ""

for line in contents.splitlines():
    mensage += line.rstrip()

mensage = mensage.replace('python', 'C')

print(mensage)