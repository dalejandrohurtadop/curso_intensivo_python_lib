sandwich_orders = ['atún', 'pastrami', 'jamón y queso', 'pastrami', 'vegetariano', 'pollo asado', 'pastrami']
finished_sandwiches = []


print('Lo sentmos ya no queda pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'Su sandwich de {sandwich} esta listo!')
    finished_sandwiches.append(sandwich)

print('Los Sandwich se han preparado en el siguiente orden: ')

i = 1
for sandwich in finished_sandwiches:
    print(f'\t{i}. {sandwich.title()}')
    i += 1
