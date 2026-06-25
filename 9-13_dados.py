from random import randint

class Dados:
    def __init__(self, caras=6):
        self.caras = caras
    
    def tirar_dado(self):
        valor_dado = randint(1, self.caras)
        return f'El valor del dado es: {valor_dado}'


caras = [6,10,20]
for cara in caras:
    print(f'\nLos resultados para el dado de {cara} son: \n')
    dado = Dados(cara)
    for i in range(10):
        print(dado.tirar_dado())