respuestas = {}

encuestando = True

while encuestando:
    name = input('\nComo es su nombre? ')
    respuesta = input('Cual es el destino de las vacaciones de sus sueños? ')

    respuestas[name] = respuesta

    repeat = input('Desea contestar la encuesta (S/N): ')

    if repeat.upper() == 'N':
        encuestando = False

print('\n------------------------\nResultado de encuestas:')

for name, lugar in respuestas.items():
    print(f'{name} tiene como destino de vacionaes ir a {lugar}')