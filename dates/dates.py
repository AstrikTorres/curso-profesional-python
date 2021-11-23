# Manejo de fechas
# Nota: Es importante evitar usar datetime.now() porque toma la hora local.
# Mejor usar datetime.utcnow() para usar la hora universal.
import datetime


def run():
    my_time = datetime.datetime.now()
    print("datetime.datetime.now(): ", my_time)

    my_day = datetime.date.today()
    print("datetime.date.today():", my_day)

    print(f'my_day.year: {my_day.year}')
    print(f'my_day.month: {my_day.month}')
    print(f'my_day.day: {my_day.day}')

    # Formateo de fechas
    my_str = my_time.strftime('%d/%m/%Y')
    print(f'Formato LATAM: {my_str}')

    my_str = my_time.strftime('%m/%d/%Y')
    print(f'Formato USA: {my_str}')

    my_str = my_time.strftime('Estamos en el año %Y')
    print(f'Formato Random: {my_str}')


if __name__ == '__main__':
    run()
