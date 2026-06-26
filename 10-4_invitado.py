from pathlib import Path

path = 'cap10/invitados.txt'
cant_invitados = int(input("¿Cuántos invitados van a asistir? "))
invitados = ""


for i in range(cant_invitados):
    invitado = input("Ingrese el nombre del invitado: ")
    invitados += invitado
    invitados += "\n"

invitados = invitados.rstrip()
archivo = Path(path)

archivo.write_text(invitados)
