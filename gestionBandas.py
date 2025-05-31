def agregarBanda(bandas,nombreBanda, email, tarifa30Min, telefono, idBanda):
    bandas[idBanda] = {
        "activo": True,
        "NombreBanda": nombreBanda,
        "Email": email,
        "Telefono": telefono,
        "Tarifa30Min": tarifa30Min,
        "Generos": {"genero1": genero[0],
                    "genero2": genero[1]}
    }
    return bandas


def modificarBanda(bandas, nombreBanda, email, tarifa30Min, generos, idBanda):
    
    bandas[idBanda] = {
        "NombreBanda": nombreBanda,
        "Email": email,
        "Tarifa30Min": tarifa30Min,
        "Telefono"
        "Generos": {"genero1": generos[0],
                    "genero2": generos[1]}
    }

    return bandas

def inactivarBanda(bandas,idBanda):
    
    bandas[idBanda]["activo"] = False
    return bandas

def listarBandasActivas(bandas):
    for banda in bandas:
        if bandas[banda]["activo"] == True:
            print(f"IdBanda: {banda}")
            print(bandas[banda])
