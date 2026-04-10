favorite_numbers = {
    'mandy': [4, 5],
    'micah': [4, 6, 7],
    'gus': [8, 9],
    'hank': [1_000_000, 0],
    'maggie': [9, 10],
}

for name, numbers in favorite_numbers.items():
    if len(numbers)>1:
        print(f'Los números favoritos de {name} son:')
        for number in numbers:
            print(f'\t{number}')
    else:
        print(f'El número favorito de {name} es {numbers}')