import time
import json

def cargarEventos(nombreArchivo):
    """
    Carga los eventos desde un archivo JSON.
    Si el archivo no existe o hay error, retorna un diccionario vacío.
    """
    try:
        archivo = open(nombreArchivo, 'r', encoding='utf-8')
        contenido = archivo.read()
        archivo.close()
        return json.loads(contenido)
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)
        return {}

def guardarEventos(nombreArchivo, eventos):
    """
    Guarda los eventos en un archivo JSON.
    """
    try:
        archivo = open(nombre_archivo, 'w', encoding='utf-8')
        contenido = json.dumps(eventos, ensure_ascii=False, indent=4)
        archivo.write(contenido)
        archivo.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

def gestionarEvento(eventos, idBanda, idSalon):
    """
    Registra un nuevo evento en el diccionario de eventos.

    Parámetros:
    - eventos: diccionario actual de eventos.
    - idBanda: ID de la banda (string).
    - idSalon: ID del salón (string).

    Solicita por input:
    - fechaEvento: string con la fecha del evento en formato AAAA.MM.DD.
    - tramosContratados: entero con la cantidad de tramos contratados.

    Calcula:
    - idEvento: string generado automáticamente como número consecutivo.
    - fechaHoraRegistro: string con la fecha y hora de registro (AAAA.MM.DD HH:MM:SS).

    Retorna:
    - eventos: diccionario actualizado.
    """
    try:
        fechaEvento = input("Ingrese la fecha del evento (AAAA.MM.DD): ")
        tramosContratados = int(input("Ingrese la cantidad de tramos contratados: "))

        fechaHoraRegistro = time.strftime("%Y.%m.%d %H:%M:%S")

        datosEvento = {
            'idEvento': str(len(eventos) + 1),
            'idBanda': idBanda,
            'idSalon': idSalon,
            'fechaEvento': fechaEvento,
            'tramosContratados': tramosContratados
        }

        eventos[fechaHoraRegistro] = datosEvento
        return eventos

    except ValueError:
        return eventos

