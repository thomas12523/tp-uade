def agregarBanda(bandas,nombreBanda, email, tarifa30Min, telefono,generos, idBanda):
    bandas[idBanda] = {
        "activo": True,
        "nombreBanda": nombreBanda,
        "email": email,
        "telefono": telefono,
        "tarifa30Min": tarifa30Min,
        "generos": {"genero1": generos[0],
                    "genero2": generos[1]}
    }
    return bandas


def modificarBanda(bandas,nombreBanda, email, tarifa30Min, telefono,generos, idBanda):
    
    bandas[idBanda] = {
        "nombreBanda": nombreBanda,
        "email": email,
        "tarifa30Min": tarifa30Min,
        "telefono":telefono,
        "generos": {"genero1": generos[0],
                    "genero2": generos[1]}
    }

    return bandas

def inactivarBanda(bandas,idBanda):
    
    bandas[idBanda]["activo"] = False
    return bandas

def listarBandasActivas(bandas):
    for banda in bandas:
        if bandas[banda]["activo"] == True:
            print(f"idBanda: {banda}")
            print(bandas[banda])
