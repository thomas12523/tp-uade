def agregarBanda(bandas, nombreBanda, email, tarifa30Min, telefono, generos, idBanda):
    """
    Agrega una nueva banda al diccionario de bandas.

    Parámetros:
    - bandas (dict): Diccionario que contiene todas las bandas.
    - nombreBanda (str): Nombre de la banda a agregar.
    - email (str): Correo electrónico de contacto de la banda.
    - tarifa30Min (float): Tarifa por 30 minutos de presentación.
    - telefono (str): Número de teléfono de contacto.
    - generos (list): Lista con dos géneros musicales asociados a la banda.
    - idBanda (str/int): Identificador único de la banda.

    Retorna:
    - dict: Diccionario actualizado con la nueva banda agregada.
    """
    bandas[idBanda] = {
        "activo": True,
        "nombreBanda": nombreBanda,
        "email": email,
        "telefono": telefono,
        "tarifa30Min": tarifa30Min,
        "generos": {
            "genero1": generos[0],
            "genero2": generos[1]
        }
    }
    return bandas


def modificarBanda(bandas, nombreBanda, email, tarifa30Min, telefono, generos, idBanda):
    """
    Modifica los datos de una banda existente en el diccionario.

    Parámetros:
    - bandas (dict): Diccionario que contiene todas las bandas.
    - nombreBanda (str): Nuevo nombre de la banda.
    - email (str): Nuevo correo electrónico de contacto.
    - tarifa30Min (float): Nueva tarifa por 30 minutos de presentación.
    - telefono (str): Nuevo número de teléfono de contacto.
    - generos (list): Lista con dos nuevos géneros musicales.
    - idBanda (str/int): Identificador único de la banda a modificar.

    Retorna:
    - dict: Diccionario actualizado con los datos modificados de la banda.
    """
    bandas[idBanda] = {
        "nombreBanda": nombreBanda,
        "email": email,
        "tarifa30Min": tarifa30Min,
        "telefono": telefono,
        "generos": {
            "genero1": generos[0],
            "genero2": generos[1]
        }
    }
    return bandas


def inactivarBanda(bandas, idBanda):
    """
    Marca una banda como inactiva en el diccionario.

    Parámetros:
    - bandas (dict): Diccionario que contiene todas las bandas.
    - idBanda (str/int): Identificador único de la banda a inactivar.

    Retorna:
    - dict: Diccionario actualizado con la banda marcada como inactiva.
    """
    bandas[idBanda]["activo"] = False
    return bandas


def listarBandasActivas(bandas):
    """
    Imprime en consola todas las bandas que están activas.

    Parámetros:
    - bandas (dict): Diccionario que contiene todas las bandas.

    Retorna:
    - None
    """
    for banda in bandas:
        if bandas[banda]["activo"] == True:
            print(f"idBanda: {banda}")
            print(bandas[banda])
