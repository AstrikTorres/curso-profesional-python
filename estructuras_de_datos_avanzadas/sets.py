# Sets o conjuntos:
# Una colección desordenada de elementos únicos e inmutables
def run():
    my_set = {3, 4, 5}
    print("my_set =", my_set)

    my_set2 = {"Hola", 23.3, False, True}
    print("my_set2 =", my_set2)

    # Set vacio:
    empty_set = set()
    print(type(empty_set))

    # Casting con sets:
    my_list = [1, 1, 2, 3, 4, 4, 5]
    my_set = set(my_list)
    print(my_set)

    my_tuple = ("Hola", "Hola", "Hola", 1, 7)
    my_set2 = set(my_tuple)
    print(my_set2)

    # Añadir elementos a sets
    my_set = {1, 3, 2}
    print(my_set)

    my_set.add(4)  # Añade un elemento
    print(my_set)

    my_set.update([1, 2, 5])  # Añade multiples elementos
    print(my_set)

    my_set.update(my_tuple, {6, 8})  # Añade multiples elementos
    print(my_set)

    # Borrar elementos a sets
    my_set.discard(1)  # Borra un elemento existente
    print(my_set)

    my_set.remove(2)  # Borra un elemento existente
    print(my_set)

    my_set.discard(10)  # Intenta borrar un elemento inexistente y nos devuelve el mismo set
    print(my_set)

    # my_set.remove(12)  # Nos da un error al intentar borrar un elemento inexistente
    # print(my_set)

    my_set.pop()  # Borra un elemento aleatorio
    print(my_set)

    my_set.clear()  # Limpia el set
    print(my_set)


my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}


def union():
    my_set3 = my_set1 | my_set2
    print(my_set3)


def interseccion():
    my_set3 = my_set1 & my_set2
    print(my_set3)


def diferencia():
    my_set3 = my_set1 - my_set2
    print(my_set3)

    my_set4 = my_set2 - my_set1
    print(my_set4)


def diferencia_simetrica():
    my_set3 = my_set1 ^ my_set2
    print(my_set3)


# Eliminando los repetidos de una lista usando sets
# [1, 1, 2, 2, 4] -> [1, 2, 4]
def remove_duplicates(some_list):
    return list(set(some_list))


if __name__ == '__main__':
    run()
    union()
    interseccion()
    diferencia()
    diferencia_simetrica()
    print("\nEliminando los repetidos de una lista: \n")
    random_list = [1, 1, 2, 2, 4]
    print("Mi lista: ", random_list)
    print("Mi lista sin elementos repetidos: ", remove_duplicates(random_list))
