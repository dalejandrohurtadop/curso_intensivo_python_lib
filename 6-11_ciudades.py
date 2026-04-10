cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_158_080,
        'fact': 'está rodeada por la cordillera de los andes',
    },
    'tokio': {
        'country': 'japón',
        'population': 37_400_068,
        'fact': 'es la zona metropolitana más poblada del mundo',
    },
    'parís': {
        'country': 'francia',
        'population': 2_148_271,
        'fact': 'es conocida como la ciudad de la luz',
    },
}

for city, dates in cities.items():
    print(f'La ciudad de {city} tiene los siguientes datos: ')
    for k, v in dates.items():
        print(f'{k}: {v}')
    print('\t')