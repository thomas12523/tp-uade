import time

def gestionarEvento(eventos, idBanda, idSalon):
    """
    Registra un nuevo evento en el diccionario de eventos.

    Parámetros:
    - eventos: diccionario de eventos (clave: fecha/hora de registro, valor: diccionario de datos del evento).
    - idBanda: string con el ID de la banda.
    - idSalon: string con el ID del salón.
    - idEvento: string con el ID del evento.
    - fechaEvento: string con la fecha del evento en formato AAAA.MM.DD.
    - tramosContratados: entero con la cantidad de tramos contratados.
    - fechaHoraRegistro: string con la fecha y hora de registro del evento en formato AAAA.MM.DD HH.MM.SS.
    Retorna:
    - eventos: diccionario actualizado con el nuevo evento.
    """
    fechaEvento = input("Ingrese la fecha del evento (AAAA.MM.DD): ")
    tramosContratados = int(input("Ingrese la cantidad de tramos contratados: "))

    fechaHoraRegistro = time.strftime("%Y.%m.%d %H.%M.%S")

    datosEvento = {
        'IdEvento': len(eventos) + 1,
        'idBanda': idBanda,
        'idSalon': idSalon,
        'FechaEvento': fechaEvento,
        'TramosContratados': tramosContratados
    }

    eventos[fechaHoraRegistro] = datosEvento

    return eventos
