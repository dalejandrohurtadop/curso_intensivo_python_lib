from urllib.request import ProxyDigestAuthHandler


def hacer_albun(nombre_artista, titulo_albun, numero_canciones=None):
    return {'Nombre artista':nombre_artista, 
            'Titulo albun': titulo_albun, 
            'Numero de canciones': numero_canciones}


print('Ingrese el nombre del artista y el titulo del albun para elaborar el diccionario')

nombre_artista = input('Ingrese el nombre del artista: ')
titulo_albun = input('Ingrese el titulo del albun: ')

pregunta_canciones = input('Desea ingresar el numero e canciones (S/N): ')

if pregunta_canciones.upper() == 'S':
    numero_canciones = input('Ingrese el numero de canciones del albun: ')
    print(hacer_albun(nombre_artista, titulo_albun, numero_canciones))
else:
    print(hacer_albun(nombre_artista, titulo_albun))

