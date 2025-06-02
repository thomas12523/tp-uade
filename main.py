"""
-----------------------------------------------------------------------------------------------
Título:
Fecha:
Autor:

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
from gestionSalones import agregarSalon, modificarSalon, inactivarSalon, listarSalonesActivos
from checkInputs import checkInt, checkTelefono, checkString, checkDireccion, checkEmail
from gestionBandas import agregarBanda, modificarBanda, inactivarBanda, listarBandasActivas
from gestionInformes import listarEventosDelMes, resumenCantidadEventosPorBanda, topDuracionEventosDelMes, resumenMontoEventosPorBanda
from gestionarEvento import gestionarEvento
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def gestorIdSalon(case, salones):
    """
    Descripción: Gestiona el ID del salón según el caso, caso 1 es para un nuevo salón, caso 2 para modificar un salon, caso 3 para inactivarlo.
    Input: case es del tipo int y salones es un diccionario con los salones existentes.
    Output: IdSalon (str): ID del salón ingresado por el usuario.
    
    """
    if case == 1:
        while True:
            IdSalon = input("Ingrese el ID del salón: ")
            if IdSalon in salones:
                print("El ID del salón ya existe. Intente con otro ID.")
            else:
                return IdSalon
    elif case == 2:
        while True:
            IdSalon = input("Ingrese el ID del salón a modificar: ")
            if IdSalon not in salones:
                print("El ID del salón no existe. Intente con otro ID.")
            else:
                return IdSalon
    elif case == 3:
        while True:
            IdSalon = input("Ingrese el ID del salón a inactivar: ")
            if IdSalon not in salones:
                print("El ID del salón no existe. Intente con otro ID.")
            else:
                return IdSalon
    
def getInputSalon(case):
    """
    Descripción: Solicita los datos necesarios para agregar o modificar un salón. Si es case 1 entonces es para agregar un salón, si es case 2 entonces es para modificar un salón. Se utiliza un condicional para si es case 1 o 2, así se muestra el texto correspondiente. Además, se valida que los datos ingresados sean correctos.
    Input: case es un entero que indica si es para agregar (1) o modificar (2) un salón.
    Output: tupla (nombreSalon, ubicacion, capacidad, telefonos)
    """
    while True:
        nombreSalon = input(f"Ingrese el {'' if case == 1 else 'nuevo '}nombre del salón: ")
        if checkString(nombreSalon):
            break
        print("El nombre del salón no puede estar vacío. Intentelo de nuevo.")

    while True:
        ubicacion = input(f"Ingrese la {'' if case == 1 else 'nueva '}ubicación del salón: ")
        if checkDireccion(ubicacion):
            break
        print("Escriba correctamente, dirección espacio numero.")

    while True:
        capacidad = input(f"Ingrese la {'' if case == 1 else 'nueva '}capacidad del salón: ")
        if checkInt(capacidad):
            capacidad = int(capacidad)
            if capacidad > 0:
                break
            print("La capacidad debe ser un número entero positivo. Intentelo de nuevo.")
        else:
            print("La capacidad debe ser un número entero. Intentelo de nuevo.")

    while True:
        telefonos = []
        for i in range(3):
            telefono = input(f"Ingrese el {'' if case == 1 else 'nuevo '}teléfono {i+1} (10 dígitos): ")
            if checkTelefono(telefono):
                telefonos.append(telefono)
            else:
                print("El teléfono debe ser un número de 10 dígitos. Intentelo de nuevo.")
                break
        if len(telefonos) == 3:
            break

    return nombreSalon, ubicacion, capacidad, telefonos

def gestorIdBanda(case, bandas):
    """
    Descripción: Gestiona el ID del banda según el caso, caso 1 es para un nuevo banda, caso 2 para modificar un banda, caso 3 para inactivarlo.
    Input: case es del tipo int y bandas es un diccionario con los bandas existentes.
    Output: Idbanda (str): ID del banda ingresado por el usuario.
    
    """
    if case == 1:
        while True:
            idBanda = input("Ingrese el ID de la banda: ")
            if idBanda in bandas:
                print("El ID del banda ya existe. Intente con otro ID.")
            else:
                return idBanda
    elif case == 2:
        while True:
            idBanda = input("Ingrese el ID de la banda a modificar: ")
            if idBanda not in bandas:
                print("El ID del banda no existe. Intente con otro ID.")
            else:
                return idBanda
    elif case == 3:
        while True:
            idBanda = input("Ingrese el ID de la banda a inactivar: ")
            if idBanda not in bandas:
                print("El ID del banda no existe. Intente con otro ID.")
            else:
                return idBanda
    
def getInputBanda(case):
    """
    Descripción: Solicita los datos necesarios para agregar o modificar un salón. Si es case 1 entonces es para agregar un salón, si es case 2 entonces es para modificar un salón. Se utiliza un condicional para si es case 1 o 2, así se muestra el texto correspondiente. Además, se valida que los datos ingresados sean correctos.
    Input: case es un entero que indica si es para agregar (1) o modificar (2) un salón.
    Output: tupla (nombreSalon, ubicacion, capacidad, telefonos)
    """
    while True:
        nombreBanda = input(f"Ingrese el {'' if case == 1 else 'nuevo '}nombre de la banda: ")
        if checkString(nombreBanda):
            break
        print("El nombre del banda no puede estar vacío. Intentelo de nuevo.")

    while True:
        email = input(f"Ingrese el {'' if case == 1 else 'nueva '}email del la banda: ")
        if checkEmail(email):
            break
        print("Escriba correctamente, test@test.com o test@test.org")

    while True:
        telefono = input(f"Ingrese el {'' if case == 1 else 'nuevo '}telefono de la banda: ")
        if checkTelefono(telefono):
            break
        else:
            print("Introducir un telefono valido.")

    while True:
        tarifa30Min = input(f"Ingrese la {'' if case == 1 else 'nueva '}tarifa de 30 minutos de la banda: ")
        if tarifa30Min.isdigit() and int(tarifa30Min) > 0:
            break
        else:
            print("Introducir una tarifa valida.")

    while True:
        generos = []
        for i in range(2):
            genero = input(f"Ingrese el {'' if case == 1 else 'nuevo '}genero {i+1}: ")
            if checkString(genero):
                generos.append(genero)
            else:
                print("Solo se permite caracteres no numericos. Intentelo de nuevo.")
                break
        if len(generos) == 2:
            break

    return nombreBanda, email, telefono,tarifa30Min, generos

def getInputMes():
    """
    Descripción: Verifica si un mes es válido.
    Input: mes es del tipo int que representa el mes a verificar (1-12).
    Output: Devuelve el mes si es válido, solicita al usuario que ingrese un mes válido en caso contrario.
    """
    while True:
        
        mes = input("Eligir un mes: ")
        if mes.isdigit() and 1 <= int(mes) <= 12:
            mes = int(mes)
            break
        else:
            print("Mes inválido. Debe ser un número entre 1 y 12.") 
    
    return mes
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    salones = {
                '1': {
                    "activo": True,
                    "nombreSalon": "Chiquimundo",
                    "ubicacion": "San Martín",
                    "capacidad": 30,
                    "telefonos": {
                        "telefono1": "1145678901",
                        "telefono2": "1145678902",
                        "telefono3": "1145678903"
                    }
                },
                '2': {
                    "activo": False,
                    "nombreSalon": "El Peperón",
                    "ubicacion": "Pepe León",
                    "capacidad": 45,
                    "telefonos": {
                        "telefono1": "1167890123",
                        "telefono2": "1167890124",
                        "telefono3": "1167890125"
                    }
                },
                '3': {
                    "activo": True,
                    "nombreSalon": "La Cúpula",
                    "ubicacion": "Belgrano",
                    "capacidad": 60,
                    "telefonos": {
                        "telefono1": "1178901234",
                        "telefono2": "1178901235",
                        "telefono3": "1178901236"
                    }
                },
                '4': {
                    "activo": True,
                    "nombreSalon": "Versalles Hall",
                    "ubicacion": "Versalles",
                    "capacidad": 80,
                    "telefonos": {
                        "telefono1": "1189012345",
                        "telefono2": "1189012346",
                        "telefono3": "1189012347"
                    }
                },
                '5': {
                    "activo": False,
                    "nombreSalon": "Sala Luna",
                    "ubicacion": "Palermo",
                    "capacidad": 50,
                    "telefonos": {
                        "telefono1": "1190123456",
                        "telefono2": "1190123457",
                        "telefono3": "1190123458"
                    }
                },
                '6': {
                    "activo": True,
                    "nombreSalon": "El Rincón",
                    "ubicacion": "Recoleta",
                    "capacidad": 40,
                    "telefonos": {
                        "telefono1": "1123456789",
                        "telefono2": "1123456790",
                        "telefono3": "1123456791"
                    }
                },
                '7': {
                    "activo": True,
                    "nombreSalon": "Sala Oasis",
                    "ubicacion": "Caballito",
                    "capacidad": 35,
                    "telefonos": {
                        "telefono1": "1134567890",
                        "telefono2": "1134567891",
                        "telefono3": "1134567892"
                    }
                },
                '8': {
                    "activo": False,
                    "nombreSalon": "La Estación",
                    "ubicacion": "San Telmo",
                    "capacidad": 70,
                    "telefonos": {
                        "telefono1": "1156789012",
                        "telefono2": "1156789013",
                        "telefono3": "1156789014"
                    }
                },
                '9': {
                    "activo": True,
                    "nombreSalon": "El Paraiso",
                    "ubicacion": "Villa Crespo",
                    "capacidad": 55,
                    "telefonos": {
                        "telefono1": "1167890234",
                        "telefono2": "1167890235",
                        "telefono3": "1167890236"
                    }
                },
                '10': {
                    "activo": True,
                    "nombreSalon": "Sala Tango",
                    "ubicacion": "San Nicolás",
                    "capacidad": 65,
                    "telefonos": {
                        "telefono1": "1178902345",
                        "telefono2": "1178902346",
                        "telefono3": "1178902347"
                    }
                }
            }
    bandas = {
                '1': {
                    "activo": True,
                    "nombreBanda": "Soda Estéreo",
                    "email": "sodaestereo1@example.com",
                    "telefono": "1234567890",
                    "tarifa30Min": 40000,
                    "generos": {
                        "genero1": "rock",
                        "genero2": "pop"
                    }
                },
                '2': {
                    "activo": False,
                    "nombreBanda": "Los Fabulosos",
                    "email": "fabulosos2@example.com",
                    "telefono": "1234567890",
                    "tarifa30Min": 35000,
                    "generos": {
                        "genero1": "punk",
                        "genero2": "ska"
                    }
                },
                '3': {
                    "activo": True,
                    "nombreBanda": "Jazz Masters",
                    "email": "jazzmasters3@example.com",
                    "telefono": "1234567890",
                    "tarifa30Min": 50000,
                    "generos": {
                        "genero1": "jazz",
                        "genero2": "blues"
                    }
                },
                '4': {
                    "activo": True,
                    "nombreBanda": "Metallica Cover",
                    "email": "metallicacover4@example.com",
                    "telefono": "1234567890",
                    "tarifa30Min": 45000,
                    "generos": {
                        "genero1": "metal",
                        "genero2": "hard rock"
                    }
                },
                '5': {
                    "activo": False,
                    "nombreBanda": "Pop Revolution",
                    "email": "poprev5@example.com",
                    "telefono": "1234567890",
                    "tarifa30Min": 30000,
                    "generos": {
                        "genero1": "pop",
                        "genero2": "electropop"
                    }
                },
                '6': {
                    "activo": True,
                    "nombreBanda": "Folklore Unido",
                    "email": "folklore6@example.com",
                    "telefono": "1234567890",
                    "tarifa30Min": 32000,
                    "generos": {
                        "genero1": "folklore",
                        "genero2": "música tradicional"
                    }
                },
                '7': {
                    "activo": True,
                    "nombreBanda": "Reggae Roots",
                    "email": "reggaeroots7@example.com",
                    "telefono": "1234567890",
                    "tarifa30Min": 38000,
                    "generos": {
                        "genero1": "reggae",
                        "genero2": "ska"
                    }
                },
                '8': {
                    "activo": False,
                    "nombreBanda": "Indie Vibes",
                    "email": "indievibes8@example.com",
                    "telefono": "1234567890",
                    "tarifa30Min": 29000,
                    "generos": {
                        "genero1": "indie",
                        "genero2": "alternativo"
                    }
                },
                '9': {
                    "activo": True,
                    "nombreBanda": "Latina Sonrisa",
                    "email": "latinasonrisa9@example.com",
                    "telefono": "1234567890",
                    "tarifa30Min": 36000,
                    "generos": {
                        "genero1": "latino",
                        "genero2": "salsa"
                    }
                },
                '10': {
                    "activo": True,
                    "nombreBanda": "Electro Beats",
                    "email": "electrobeats10@example.com",
                    "telefono": "1234567890",
                    "tarifa30Min": 41000,
                    "generos": {
                        "genero1": "electrónica",
                        "genero2": "dance"
                    }
                }
            }

    eventos = {
                "2025.07.01 00:00:01": {
                    "idEvento": "1",
                    "idBanda": "1",
                    "idSalon": "1",
                    "fechaEvento": "2025.07.01",
                    "tramosContratados": 5
                },
                "2025.07.02 00:00:02": {
                    "idEvento": "2",
                    "idBanda": "2",
                    "idSalon": "2",
                    "fechaEvento": "2025.07.02",
                    "tramosContratados": 6
                },
                "2025.07.03 00:00:03": {
                    "idEvento": "3",
                    "idBanda": "3",
                    "idSalon": "3",
                    "fechaEvento": "2025.07.03",
                    "tramosContratados": 7
                },
                "2025.07.04 00:00:04": {
                    "idEvento": "4",
                    "idBanda": "4",
                    "idSalon": "4",
                    "fechaEvento": "2025.07.04",
                    "tramosContratados": 8
                },
                "2025.07.05 00:00:05": {
                    "idEvento": "5",
                    "idBanda": "5",
                    "idSalon": "5",
                    "fechaEvento": "2025.07.05",
                    "tramosContratados": 9
                },
                "2025.07.06 00:00:06": {
                    "idEvento": "6",
                    "idBanda": "6",
                    "idSalon": "6",
                    "fechaEvento": "2025.07.06",
                    "tramosContratados": 10
                },
                "2025.07.07 00:00:07": {
                    "idEvento": "7",
                    "idBanda": "7",
                    "idSalon": "7",
                    "fechaEvento": "2025.07.07",
                    "tramosContratados": 11
                },
                "2025.07.08 00:00:08": {
                    "idEvento": "8",
                    "idBanda": "8",
                    "idSalon": "8",
                    "fechaEvento": "2025.07.08",
                    "tramosContratados": 12
                },
                "2025.07.09 00:00:09": {
                    "idEvento": "9",
                    "idBanda": "9",
                    "idSalon": "9",
                    "fechaEvento": "2025.07.09",
                    "tramosContratados": 13
                },
                "2025.07.10 00:00:10": {
                    "idEvento": "10",
                    "idBanda": "10",
                    "idSalon": "10",
                    "fechaEvento": "2025.07.10",
                    "tramosContratados": 14
                }
            }
    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 4
            print()
            print("---------------------------")
            print("MENÚ PRINCIPAL")
            print("---------------------------")
            print("[1] Gestión de Bandas")
            print("[2] Gestión de Salón")
            print("[3] Gestión de Eventos")
            print("[4] Informes")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcionSubmenu = ""
            opcionMenuPrincipal = input("Seleccione una opción: ")
            if opcionMenuPrincipal in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcionMenuPrincipal == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcionMenuPrincipal == "1":   # Opción 1 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE BANDAS")
                    print("---------------------------")
                    print("[1] Ingresar bandas")
                    print("[2] Modificar bandas")
                    print("[3] Eliminar bandas")
                    print("[4] Listado de bandas activas")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    idBanda = gestorIdBanda(1, bandas)
                    nombreBanda, email, telefono,tarifa30Min, generos = getInputBanda(1)
                    bandas = agregarBanda(bandas,nombreBanda, email, tarifa30Min, telefono,generos, idBanda)
                    print(f"Se ha ingresado la banda satisfactoriamente.")
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    idBanda = gestorIdBanda(2, bandas)
                    nombreBanda, email, telefono,tarifa30Min, generos = getInputBanda(2)
                    bandas = modificarBanda(bandas,nombreBanda, email, tarifa30Min, telefono,generos, idBanda)
                    print(f"Se ha modificado la banda satisfactoriamente.")
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    idBanda = gestorIdBanda(3, bandas)
                    bandas = inactivarBanda(bandas,idBanda)
                    print(f"Se ha inactivado la banda con ID {idBanda} satisfactoriamente.")
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("Listado de bandas activas:")
                    listarBandasActivas(bandas)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")


        elif opcionMenuPrincipal == "2":   # Opción 2 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE SALON")
                    print("---------------------------")
                    print("[1] Ingresar salón")
                    print("[2] Modificar salón")
                    print("[3] Eliminar salón")
                    print("[4] Listado de salones activos")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    nombreSalon, ubicacion, capacidad, telefonos = getInputSalon(1)
                    IdSalon = gestorIdSalon(1, salones)
                    salones = agregarSalon(salones,nombreSalon, ubicacion, capacidad, telefonos, IdSalon)
                    print(f"Se ha creado el salón satisfactoriamente.")
                    
                elif opcionSubmenu == "2": # Opción 2 del submenú
                    nombreSalon, ubicacion, capacidad, telefonos = getInputSalon(2)
                    idSalon = gestorIdSalon(2, salones)
                    salones = modificarSalon(salones,nombreSalon, ubicacion, capacidad, telefonos, IdSalon)
                    print(f"Se ha modificado el salón satisfactoriamente.")
                
                elif opcionSubmenu == "3": # Opción 3 del submenú
                    idSalon = gestorIdSalon(3,salones)   
                    salones = inactivarSalon(salones,idSalon)
                    print(f"Se ha inactivado el salón con ID {idSalon} satisfactoriamente.")
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("Listado de salones activos:")
                    listarSalonesActivos(salones)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")
        
        elif opcionMenuPrincipal == "3":   # Opción 3 del menú principal
            while True:
                while True:
                    opciones = 1
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE GESTIÓN DE EVENTOS")
                    print("---------------------------")
                    print("[1] Registrar de Evento")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break # No sale del programa, sino que vuelve al menú anterior
                
                elif opcionSubmenu == "1":   # Opción 1 del submenú
                    
                    while True:
                        idBanda = input("Ingrese el ID de la Banda: ")
                        idSalon = input("Ingrese el ID del Salón: ")
                        if idBanda in bandas and idSalon in salones:
                            eventos = gestionarEvento(eventos, idBanda, idSalon)
                            print(f"Se ha registrado el evento satisfactoriamente.")
                            for evento in eventos:
                                print(f"FechaIngreso: {evento}")
                                print(eventos[evento])
                            break
                        else:
                            print("El ID de la Banda o del Salón no existe. Por favor, verifique los IDs ingresados.")
        
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE INFORMES")
                    print("---------------------------")
                    print("[1] Eventos del Mes")
                    print("[2] Resumen Anual de eventos por banda(Cantidades)")
                    print("[3] Resumen Anual de eventos por banda(Pesos)")
                    print("[4] Top 3 eventos con más duración del mes")
                    print("---------------------------")
                    print("[0] Volver al menú anterior")
                    print("---------------------------")
                    print()
                    
                    opcionSubmenu = input("Seleccione una opción: ")
                    if opcionSubmenu in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                        break
                    else:
                        input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

                if opcionSubmenu == "0": # Opción salir del submenú
                    break
      
                elif opcionSubmenu == "1": # Opción 1 del submenú
                    mes = getInputMes()
                    listarEventosDelMes(eventos,mes)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    resumenCantidadEventosPorBanda(eventos)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    resumenMontoEventosPorBanda(eventos, bandas)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    topDuracionEventosDelMes(eventos)

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()