def agregarSalon(salones,nombreSalon, ubicacion, capacidad, telefonos,idSalon):
    """
    Agrega un nuevo salón al diccionario de salones.
    Parámetros:
    - salones: diccionario de salones
    - nombreSalon: string con el nombre del salón.
    - ubicacion: string con la ubicación del salón.
    - capacidad: entero con la capacidad del salón.
    - telefonos: lista de strings con los números de teléfono del salón.
    - idSalon: string con el ID del salón.
    Retorna:
    - salones: diccionario actualizado con el nuevo salón.
    """
    salones[idSalon] = {
        "activo": True,
        "nombreSalon": nombreSalon,
        "ubicacion": ubicacion,
        "capacidad": capacidad,
        "telefonos": {"telefono1": telefonos[0],
                     "telefono2": telefonos[1],
                     "telefono3": telefonos[2]}
    }
    return salones


def modificarSalon(salones,nombreSalon, ubicacion, capacidad, telefonos,idSalon):
    """
    Modifica los datos de un salón existente en el diccionario de salones.
    Parámetros:
    - salones: diccionario de salones
    - nombreSalon: string con el nuevo nombre del salón.
    - ubicacion: string con la nueva ubicación del salón.
    - capacidad: entero con la nueva capacidad del salón.
    - telefonos: lista de strings con los nuevos números de teléfono del salón.
    - idSalon: string con el ID del salón a modificar.
    Retorna:
    - salones: diccionario actualizado con los datos modificados del salón.
    """
    
    salones[idSalon] = {
        "nombreSalon": nombreSalon,
        "ubicacion": ubicacion,
        "capacidad": capacidad,
        "telefonos": {"telefono1": telefonos[0],
                     "telefono2": telefonos[1],
                     "telefono3": telefonos[2]}
    }

    return salones

def inactivarSalon(salones,idSalon):
    """
    Inactiva un salón en el diccionario de salones.
    Parámetros:
    - salones: diccionario de salones
    - idSalon: string con el ID del salón a inactivar.
    Retorna:
    - salones: diccionario actualizado con el salón inactivado.
    """
    
    salones[idSalon]["activo"] = False
    return salones

def listarSalonesActivos(salones):
    """
    Lista los salones activos en el diccionario de salones.
    Parámetros:
    - salones: diccionario de salones
    Retorna:
    - Imprime los salones activos en la consola.
    """
    for salon in salones:
        if salones[salon]["activo"] == True:
            print(f"IdSalon: {salon}")
            print(salones[salon])