def sandwich(*args):
    """Imprime los ingredientes ingresados por el usuario para
        preparar un sandwich
    """
    print('\nLos ingedientes de su sandwhich son: ')
    
    for ingrediente in args:
        print(f'\t{ingrediente}')


# El clásico que nunca falla
sandwich_clasico = (
    "pan de molde", 
    "jamón york", 
    "queso gouda", 
    "lechuga romana", 
    "tomate", 
    "mayonesa"
)

# Una opción vegetariana potente
sandwich_veggie = (
    "pan integral de semillas", 
    "aguacate", 
    "espinacas baby", 
    "queso de cabra", 
    "pimientos asados"
)

# El "desayuno de campeones"
sandwich_breakfast = (
    "bagel", 
    "huevo frito", 
    "bacon crujiente", 
    "queso cheddar", 
    "salsa picante"
)


sandwich("pan de molde", "jamón york", 
    "queso gouda", 
    "lechuga romana", 
    "tomate", 
    "mayonesa")

sandwich(sandwich_veggie)

sandwich(sandwich_breakfast)
