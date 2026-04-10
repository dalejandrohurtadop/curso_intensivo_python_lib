invitados = ['David', 'Angel', 'Angelica']

no_asistencia = invitados.pop(0)
print(f'El invitado {no_asistencia} presento sus excusas por no poder asistir')

invitados.append('Beto')

print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[0]}" al respaldo de la silla')
print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[1]}" al respaldo de la silla')
print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[2]}" al respaldo de la silla')

print(f'\n La cantidad de invitados es {len(invitados)}\n')

print('Se ha encontrado una locación con mas espacio y por lo tanto habran mas invitados a la reunión. ' \
'Este atento a la información')

invitados.insert(0, 'Juan')
invitados.insert(2,'Maria')
invitados.append('Julia')


print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[0]}" al respaldo de la silla')
print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[1]}" al respaldo de la silla')
print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[2]}" al respaldo de la silla')
print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[3]}" al respaldo de la silla')
print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[4]}" al respaldo de la silla')
print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[5]}" al respaldo de la silla')

print(f'\n La cantidad de invitados es {len(invitados)}\n')
