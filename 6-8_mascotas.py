pet_0 = {'kind': 'perro', 'owner': 'eric'}
pet_1 = {'kind': 'gato', 'owner': 'sarah'}
pet_2 = {'kind': 'hámster', 'owner': 'phil'}
pet_3 = {'kind': 'tortuga', 'owner': 'jen'}
pet_4 = {'kind': 'loro', 'owner': 'willie'}
pet_5 = {'kind': 'conejo', 'owner': 'ever'}
pet_6 = {'kind': 'pez dorado', 'owner': 'marie'}


mascotas = [pet_0, pet_1, pet_2, pet_3, pet_4, pet_5, pet_6]

for mascota in mascotas:
    print(f' El dueño de la mascota {mascota['kind']} es {mascota['owner']}' )