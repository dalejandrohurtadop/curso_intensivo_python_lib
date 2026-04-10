favorite_places = {
    'eric': ['sitka', 'death valley', 'grand canyon'],
    'erin': ['hawaii', 'reykjavik'],
    'willie': ['mount vernon'],
}

for k, v in favorite_places.items():
    if len(v)>1:
        print(f'Los Lugares favoritos de {k} son:')
        for place in v:
            print(f'\t{place}')
    else:
        print(f'El lgar favorito de {k} es {" ".join(v)}')