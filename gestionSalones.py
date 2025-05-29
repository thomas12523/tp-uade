def agregarSalon(salones,nombreSalon, ubicacion, capacidad, telefonos,idSalon):
    salones[idSalon] = {
        "activo": True,
        "NombreSalon": nombreSalon,
        "Ubicacion": ubicacion,
        "Capacidad": capacidad,
        "Telefonos": {"telefono1": telefonos[0],
                     "telefono2": telefonos[1],
                     "telefono3": telefonos[2]}
    }
    return salones


def modificarSalon(salones,nombreSalon, ubicacion, capacidad, telefonos,idSalon):
    
    salones[idSalon] = {
        "NombreSalon": nombreSalon,
        "Ubicacion": ubicacion,
        "Capacidad": capacidad,
        "Telefonos": {"telefono1": telefonos[0],
                     "telefono2": telefonos[1],
                     "telefono3": telefonos[2]}
    }

    return salones

def inactivarSalon(salones,idSalo):
    
    salones[idSalo]["activo"] = False
    return salones

def listarSalonesActivos(salones):
    for salon in salones:
        if salones[salon]["activo"] == True:
            print(f"IdSalon: {salon}")
            print(salones[salon])