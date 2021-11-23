# Generadores
# Sugar syntax de los iteradores
import time


def my_gen():
    print("Hello world")
    n = 0
    yield n

    print("Hello heaven!")
    n = 1
    yield n

    print("Hello hell!")
    n = 2
    yield n


def fibo_gen(num_max: int = None):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            if not num_max or aux <= num_max:
                n1, n2 = n2, aux
                counter += 1
                yield aux
            else:
                break


def run():
    a = my_gen()
    print(next(a))  # Hello World
    print(next(a))  # Hello heaven!
    print(next(a))  # Hello hell!
    print("Fin my_gen()")


if __name__ == '__main__':
    run()
    print("¡Comienzo de Fibonacci!")
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(0.4)
