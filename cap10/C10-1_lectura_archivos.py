from pathlib import Path

path = Path("pi_dig.txt")
contents = path.read_text(encoding="utf-8")
lines = contents.splitlines()

pi_string = ""

for line in lines:
    pi_string += line

birtday = input("Ingrese su cumpleaños en el formato 'mmddyy': ")

if birtday in pi_string:
    print("Tu cumpleaños esta dentro de los primerosn numeros de pi")
else:
    print("Intenta con mas decimales de pi")