# Tipado estático en Python

# De esta manera se declara una variable con tipado estático:
# <variable> : <tipo_de_dato> = <valor_asignado>
a: int = 5
print(a)

b: str = "Hola"
print(b)

c: bool = True
print(c)


# Con el modulo mypy se pueden ver errores de tipado en Python:
# mypy palindrome.py --check-untyped-def

def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]


def run():
    print(is_palindrome(1000))


if __name__ == '__main__':
    run()
