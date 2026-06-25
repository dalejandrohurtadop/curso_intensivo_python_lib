import random
import string

class Boleto:
    def __init__(self, cant_numeros=10, cant_letras=5):
        self.cant_numeros = cant_numeros
        self.cant_letras = cant_letras

    def impresion_boleto(self):
        letras = list(string.ascii_lowercase)
        boleto = ""
        for i in range(self.cant_letras):
            boleto += random.choice(letras)

        for i in range(self.cant_numeros):
            boleto += str(random.randint(0,9))

        return boleto


mi_boleto = Boleto()
mi_boleto_perdedor = Boleto()

print(mi_boleto.impresion_boleto())

boletos = []

for i in range(1000):
    boleto = Boleto()
    boletos.append(boleto.impresion_boleto())

boletos.append(mi_boleto)

if mi_boleto_perdedor in boletos:
    print(f'Felicitaciones ha ganado el premio con el boleto {mi_boleto_perdedor.impresion_boleto()}')
else:
    print(f'Siga intentando')


