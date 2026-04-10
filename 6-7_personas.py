'''
Empiece con el programa que ha escrito para el ejercicio 6-1. Cree dos 
diccionarios nuevos que representen a distintas personas y guarde los 
tres diccionarios en una lista llamada personas. Pase el bucle por la lista. 
al hacerlo, imprima todo lo que sabe sobre cada persona
'''
persona1= {
    'nombre': 'David',
    'apelido': 'Hurtado',
    'edad': 34,
    'ciudad': 'Bogota'
        }


persona2= {
    'nombre': 'Angelica',
    'apelido': 'Mora',
    'edad': 33,
    'ciudad': 'Bogota'
        }

persona3= { 
    'nombre': 'Angel',
    'apelido': 'Latorre',
    'edad': 8,
    'ciudad': 'Santiago'
        }


personas = [persona1, persona2, persona3]

for persona in personas:
    print(persona)
    print(f'\tNombre: {persona["nombre"].title()} {persona["apelido"]}')
    print(f'\t\tEdad: {persona["edad"]}')
    print(f'\t\tCiudad: {persona["ciudad"]}')


