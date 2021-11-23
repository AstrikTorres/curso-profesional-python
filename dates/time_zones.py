# Para trabajar con zonas horarias se usa el modulo pytz
from datetime import datetime
import pytz


def run():
    format_latam_date = '%d/%m/%y, %H:%M:%S'
    bogota_timezone = pytz.timezone("America/Bogota")
    bogota_date = datetime.now(bogota_timezone)
    print("Bogotá: ", bogota_date.strftime(format_latam_date))

    mexico_timezone = pytz.timezone("America/Mexico_City")
    mexico_date = datetime.now(mexico_timezone)
    print("México: ", mexico_date.strftime(format_latam_date))


if __name__ == '__main__':
    run()
