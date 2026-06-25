import random
import string

class Boleto:
    def __init__(self, cant_numeros=5, cant_letras=3):
        self.cant_numeros = cant_numeros
        self.cant_letras = cant_letras

    def impresion_boleto(self):
        letras = list(string.ascii_lowercase)
        numero_boleto = ""
        for i in range(self.cant_letras):
            numero_boleto += random.choice(letras)

        for i in range(self.cant_numeros):
            numero_boleto += str(random.randint(0,9))

        return numero_boleto


mi_boleto = Boleto()

print(mi_boleto.impresion_boleto())

boletos = []

while True:
    boleto = Boleto()
    num_boleto = boleto.impresion_boleto()
    boletos.append(num_boleto)

    if num_boleto == mi_boleto.impresion_boleto():
        print(f'Felicitaciones ha ganado el premio con el boleto {mi_boleto.impresion_boleto()}')
        print(len(boletos))
        break

    if len(boletos) > 1000_000_000_000:
        print(f'No ganastes')
        break