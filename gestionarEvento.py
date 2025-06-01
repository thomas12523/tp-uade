import time

def gestionarEvento(eventos, id_banda, id_salon):
    """
    Registra un nuevo evento en el diccionario de eventos.

    Parámetros:
    - eventos: diccionario de eventos (clave: fecha/hora, valor: diccionario de datos del evento).
    - id_banda: string con el ID de la banda.
    - id_salon: string con el ID del salón.

    Retorna:
    - eventos: diccionario actualizado con el nuevo evento.
    """

    # Solicitar al usuario la cantidad de tramos contratados
    tramos_contratados_str = input("Ingrese la cantidad de tramos contratados: ")
    tramos_contratados = int(tramos_contratados_str)  # Sin try-except
    
    # Obtener fecha y hora actual
    fecha_hora_actual = time.strftime("%Y.%m.%d %H.%M.%S")
    
    # Crear el subdiccionario con los datos del evento
    datos_evento = {
        'IdEvento': len(eventos),
        'idBanda': id_banda,
        'idSalon': id_salon,
        'TramosContratados': tramos_contratados
    }
    
    # Agregar al diccionario principal
    eventos[fecha_hora_actual] = datos_evento
    return eventos

    
    
    


