# Scope: Alcance de las variables
# Una variable solo esta disponible dentro de la región donde fue creada

# Local Scope
def my_func():
    y = 5
    print(y)  # output: 5


# Global Scope
x = 5


def my_func2():
    print(x)  # output: 5


def my_other_func2():
    print(x)  # output: 5


# --------------------


def run():
    my_func()
    my_func2()
    my_other_func2()

    # --------------------
    z = 5

    def my_func3():
        z = 3

        def my_other_func3():
            z = 2
            print(z)

        my_other_func3()

        print(z)

    my_func3()
    print(z)
    # output:
    # 2
    # 3
    # 5
    # --------------------


if __name__ == '__main__':
    run()
