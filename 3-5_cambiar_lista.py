invitados = ['David', 'Angel', 'Angelica']

print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[0]}" al respaldo de la silla')
print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[1]}" al respaldo de la silla')
print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[2]}" al respaldo de la silla')


no_asistencia = invitados.pop(0)
print(f'El invitado {no_asistencia} presento sus excusas por no poder asistir')

invitados.append('Beto')

print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[0]}" al respaldo de la silla')
print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[1]}" al respaldo de la silla')
print(f'Bienvenido a la cena, Como invitado busque su nombre "{invitados[2]}" al respaldo de la silla')

print(f'La cantidad de invitados es {len(invitados)}')