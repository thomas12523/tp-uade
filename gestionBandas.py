import json

def agregarBanda(nombreBanda, email, tarifa30Min, telefono, generos, idBanda):
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
    
    try:
        # Abre el archivo bandas.json y carga su contenido en un diccionario.
        _bandas = open("bandas.json", "r", encoding="utf-8")
        bandas = json.load(_bandas)
        _bandas.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)
    
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

    # Guarda el diccionario actualizado de bandas en el archivo bandas.json.
    try:
        _bandas = open("bandas.json", "w", encoding="utf-8")
        json.dump(bandas, _bandas, ensure_ascii=False, indent=4)
        _bandas.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)


def modificarBanda(nombreBanda, email, tarifa30Min, telefono, generos, idBanda):
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
    
    try:
        # Abre el archivo bandas.json y carga su contenido en un diccionario.
        _bandas = open("bandas.json", "r", encoding="utf-8")
        bandas = json.load(_bandas)
        _bandas.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)
    
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

    # Guarda el diccionario actualizado de bandas en el archivo bandas.json.
    try:
        _bandas = open("bandas.json", "w", encoding="utf-8")
        json.dump(bandas, _bandas, ensure_ascii=False, indent=4)
        _bandas.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)


def inactivarBanda(idBanda):
    """
    Marca una banda como inactiva en el archivo bandas.json.

    Parámetros:
    - idBanda (str/int): Identificador único de la banda a inactivar.
    """
    try:
        # Abre el archivo bandas.json y carga su contenido en un diccionario.
        _bandas = open("bandas.json", "r", encoding="utf-8")
        bandas = json.load(_bandas)
        _bandas.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    bandas[idBanda]["activo"] = False

    try:
        # Guarda el diccionario actualizado de bandas en el archivo bandas.json.
        _bandas = open("bandas.json", "w", encoding="utf-8")
        json.dump(bandas, _bandas, ensure_ascii=False, indent=4)
        _bandas.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)


def listarBandasActivas():
    """
    Imprime en consola todas las bandas que están activas.

    Parámetros:
    - bandas (dict): Diccionario que contiene todas las bandas.

    Retorna:
    - None
    """
    try:
        _bandas = open("bandas.json", "r", encoding="utf-8")
        bandas = json.load(_bandas)
        _bandas.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    for banda in bandas:
        if bandas[banda]["activo"]:
            print("IdBanda: "      + banda)
            print("NombreBanda: "  + bandas[banda]["nombreBanda"])
            print("Email: "    + bandas[banda]["email"])
            print("Telefono: " + bandas[banda]["telefono"])
            print("Tarifa30Min: "    + str(bandas[banda]["tarifa30Min"]))
            print("Generos: "     + bandas[banda]["generos"]["genero1"]
                                  + ", " + bandas[banda]["generos"]["genero2"])
            print("-------------------------")
