import json

def agregarSalon(nombreSalon, ubicacion, capacidad, telefonos,idSalon):
    """
    Agrega un nuevo salón al archivo salones.json.
    Parámetros:
    - nombreSalon: string con el nombre del salón.
    - ubicacion: string con la ubicación del salón.
    - capacidad: entero con la capacidad del salón.
    - telefonos: lista de strings con los números de teléfono del salón.
    - idSalon: string con el ID del salón.
    """
    try:
        # Abre el archivo salones.json y carga su contenido en un diccionario.
        _salones = open("salones.json", "r", encoding="utf-8")
        salones = json.load(_salones)
        _salones.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)
    
    salones[idSalon] = {
        "activo": True,
        "nombreSalon": nombreSalon,
        "ubicacion": ubicacion,
        "capacidad": capacidad,
        "telefonos": {"telefono1": telefonos[0],
                     "telefono2": telefonos[1],
                     "telefono3": telefonos[2]}
    }

    # Guarda el diccionario actualizado de salones en el archivo salones.json.
    try:
        _salones = open("salones.json", "w", encoding="utf-8")
        json.dump(salones, _salones, ensure_ascii=False, indent=4)
        _salones.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

def modificarSalon(nombreSalon, ubicacion, capacidad, telefonos,idSalon):
    """
    Modifica los datos de un salón existente en el archivo salones.json.
    Parámetros:
    - nombreSalon: string con el nuevo nombre del salón.
    - ubicacion: string con la nueva ubicación del salón.
    - capacidad: entero con la nueva capacidad del salón.
    - telefonos: lista de strings con los nuevos números de teléfono del salón.
    - idSalon: string con el ID del salón a modificar.
    """

    try:
        # Abre el archivo salones.json y carga su contenido en un diccionario.
        _salones = open("salones.json", "r", encoding="utf-8")
        salones = json.load(_salones)
        _salones.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    salones[idSalon] = {
        "activo": True,
        "nombreSalon": nombreSalon,
        "ubicacion": ubicacion,
        "capacidad": capacidad,
        "telefonos": {"telefono1": telefonos[0],
                     "telefono2": telefonos[1],
                     "telefono3": telefonos[2]}
    }

    try:
        # Guarda el diccionario actualizado de salones en el archivo salones.json.
        _salones = open("salones.json", "w", encoding="utf-8")
        json.dump(salones, _salones, ensure_ascii=False, indent=4)
        _salones.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

def inactivarSalon(idSalon):
    """
    Inactiva un salón en el archivo salones.json.
    Parámetros:
    - idSalon: string con el ID del salón a inactivar.
    """

    try:
        # Abre el archivo salones.json y carga su contenido en un diccionario.
        _salones = open("salones.json", "r", encoding="utf-8")
        salones = json.load(_salones)
        _salones.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    salones[idSalon]["activo"] = False

    try:
        # Guarda el diccionario actualizado de salones en el archivo salones.json.
        _salones = open("salones.json", "w", encoding="utf-8")
        json.dump(salones, _salones, ensure_ascii=False, indent=4)
        _salones.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

def listarSalonesActivos():
    """
    Lista los salones activos en el archivo salones.json.
    Retorna:
    - Imprime los salones activos en la consola.
    """
    try:
        _salones = open("salones.json", "r", encoding="utf-8")
        salones = json.load(_salones)
        _salones.close()
    except (FileNotFoundError, OSError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)

    for salon in salones:
        if salones[salon]["activo"] == True:
            print(f"IdSalon: {salon}")
            print(salones[salon])