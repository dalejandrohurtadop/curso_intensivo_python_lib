pizzas = ['pepperoni', 'margherita', 'hawaian']
friend_pizzas = pizzas[:]

pizzas.append('mexicana')
friend_pizzas.append('diavola')

print('Mis pizzas favoritas son: ')
for pizza in pizzas:
    print(pizza)

print('\nLas pizzas favoritas de mi amigo son: ')

for pizza in friend_pizzas:
    print(pizza)
