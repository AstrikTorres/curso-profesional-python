# Closures:
# - Debemos tener una nested function
# - La nested function debe referenciar a un valor de un scope superior
# - La función que enevuelve a la nested function debe retornarla también.

# Ejemplo 1:
def make_multiplier(x):

    def multiplier(n):
        return x * n

    return multiplier


# Ejemplo 2:
def make_reapeter_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar texto"
        return string * n
    return repeater


def run():
    print("    Ejemplo 1:")
    # times10 contiene la función make_multiplier() con 10 en el parametro "x"
    times10 = make_multiplier(10)
    times4 = make_multiplier(4)
    # times10 se le pasa un 3 como parametro que guardara en "n" de la función multiplier()
    print(times10(3))
    print(times4(5))
    print(times10(times4(2)))
    print("""
    Ejemplo 2:""")
    repeat_5 = make_reapeter_of(5)
    print(repeat_5("Hola"))
    repeat_10 = make_reapeter_of(10)
    print(repeat_10("Platzi"))


if __name__ == '__main__':
    run()
