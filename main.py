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
from checkInputs import checkInt, checkTelefono, checkString, checkDireccion, checkEmail, checkGenero
from gestionBandas import agregarBanda, modificarBanda, inactivarBanda, listarBandasActivas
from gestionInformes import listarEventosDelMes, resumenCantidadEventosPorBanda, topDuracionEventosDelMes, resumenMontoEventosPorBanda
from gestionarEvento import gestionarEvento
import json
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def gestorIdSalon(case):
    """
    Descripción: Gestiona el ID del salón según el caso, caso 1 es para un nuevo salón, caso 2 para modificar un salon, caso 3 para inactivarlo.
    Input: case es del tipo int y salones es un diccionario con los salones existentes.
    Output: IdSalon (str): ID del salón ingresado por el usuario.
    
    """
    # Abre el archivo salones.json y carga su contenido en un diccionario.
    _salones = open("salones.json", "r", encoding="utf-8")
    salones = json.load(_salones)
    _salones.close()

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
    
def getInputSalon(case, datos=None):
    """
    Descripción: Solicita los datos necesarios para agregar o modificar un salón. Si es case 1 entonces es para agregar un salón, si es case 2 entonces es para modificar un salón. Se utiliza un condicional para si es case 1 o 2, así se muestra el texto correspondiente. Además, se valida que los datos ingresados sean correctos.
    Input: case es un entero que indica si es para agregar (1) o modificar (2) un salón. datos es un diccionario con los datos del salón a modificar (opcional, solo si case es 2).
    Output: tupla (nombreSalon, ubicacion, capacidad, telefonos)
    """
    while True:
        if case == 1:
            nombreSalon = input(f"Ingrese el nombre del salón: ")
            if checkString(nombreSalon):
                break
            print("El nombre del salón no puede estar vacío. Intentelo de nuevo.")
        else:
            nombreSalon = input(f"Ingrese el nuevo nombre del salón o enter para dejar el dato actual [actualmente: {datos['nombreSalon']}]: ").strip()
            if nombreSalon == "":
                nombreSalon = datos['nombreSalon']
                break
            if checkString(nombreSalon):
                break

    while True:
        if case == 1:
            ubicacion = input(f"Ingrese la ubicación del salón: ")
            if checkDireccion(ubicacion):
                break
            print("Escriba correctamente, dirección espacio numero.")
        else:
            ubicacion = input(f"Ingrese la nueva ubicación del salón o enter para dejar el dato actual [actualmente: {datos['ubicacion']}]: ").strip()
            if ubicacion == "":
                ubicacion = datos['ubicacion']
                break
            if checkDireccion(ubicacion):
                break
            print("Escriba correctamente, dirección espacio numero.")

    while True:
        if case == 1:
            capacidad = input(f"Ingrese la capacidad del salón: ")
            if checkInt(capacidad):
                capacidad = int(capacidad)
                if capacidad > 0:
                    break
                print("La capacidad debe ser un número entero positivo. Intentelo de nuevo.")
            else:
                print("La capacidad debe ser un número entero. Intentelo de nuevo.")
        else:
            capacidad = input(f"Ingrese la nueva capacidad del salón o enter para dejar el dato actual [actualmente: {datos['capacidad']}]: ").strip()
            if capacidad == "":
                capacidad = datos['capacidad']
                break
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
            if case == 1:
                telefono = input(f"Ingrese el {'' if case == 1 else 'nuevo '}teléfono {i+1} (10 dígitos): ")
                if checkTelefono(telefono):
                    telefonos.append(telefono)
                else:
                    print("El teléfono debe ser un número de 10 dígitos. Intentelo de nuevo.")
                    break
            else:
                telefono = input(f"Ingrese el nuevo teléfono {i+1} o enter para dejar el dato actual [actualmente: {datos['telefonos']['telefono' + str(i+1)]}]: ").strip()
                if telefono == "":
                    telefonos.append(datos['telefonos']['telefono' + str(i+1)])
                elif checkTelefono(telefono):
                    telefonos.append(telefono)
                else:
                    print("El teléfono debe ser un número de 10 dígitos. Intentelo de nuevo.")
                    break
        if len(telefonos) == 3:
            break

    return nombreSalon, ubicacion, capacidad, telefonos

def gestorIdBanda(case):
    """
    Descripción: Gestiona el ID del banda según el caso, caso 1 es para un nuevo banda, caso 2 para modificar un banda, caso 3 para inactivarlo.
    Input: case es del tipo int y bandas es un diccionario con los bandas existentes.
    Output: Idbanda (str): ID del banda ingresado por el usuario.
    
    """
    archivo = open("bandas.json", "r", encoding="utf-8")
    bandas = json.load(archivo)
    archivo.close()
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
            if checkGenero(genero):
                generos.append(genero)
            else:
                print("Solo se permite caracteres no numericos. Intentelo de nuevo.")
                break
        if len(generos) == 2:
            break

    return nombreBanda, email, telefono,tarifa30Min, generos

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    
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
                    idBanda = gestorIdBanda(1)
                    nombreBanda, email, telefono,tarifa30Min, generos = getInputBanda(1)
                    bandas = agregarBanda(nombreBanda, email, tarifa30Min, telefono,generos, idBanda)
                    print(f"Se ha ingresado la banda satisfactoriamente.")
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    idBanda = gestorIdBanda(2)
                    nombreBanda, email, telefono,tarifa30Min, generos = getInputBanda(2)
                    bandas = modificarBanda(nombreBanda, email, tarifa30Min, telefono,generos, idBanda)
                    print(f"Se ha modificado la banda satisfactoriamente.")
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    idBanda = gestorIdBanda(3)
                    bandas = inactivarBanda(idBanda)
                    print(f"Se ha inactivado la banda con ID {idBanda} satisfactoriamente.")
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("Listado de bandas activas:")
                    listarBandasActivas()

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
                    idSalon = gestorIdSalon(1)
                    agregarSalon(nombreSalon, ubicacion, capacidad, telefonos, idSalon)
                    print(f"Se ha creado el salón con ID {idSalon} satisfactoriamente.")
                    
                elif opcionSubmenu == "2": # Opción 2 del submenú
                    try:
                        # Abre el archivo salones.json y carga su contenido en un diccionario.
                        _salones = open("salones.json", "r", encoding="utf-8")
                        salones = json.load(_salones)
                        _salones.close()
                    except (FileNotFoundError, OSError) as detalle:
                        print("Error al intentar abrir archivo(s):", detalle)

                    idSalon = gestorIdSalon(2)
                    datos = salones[idSalon]
                    nombreSalon, ubicacion, capacidad, telefonos = getInputSalon(2, datos)
                    
                    modificarSalon(nombreSalon, ubicacion, capacidad, telefonos, idSalon)
                    print(f"Se ha modificado el salón con ID {idSalon} satisfactoriamente.")
                
                elif opcionSubmenu == "3": # Opción 3 del submenú
                    idSalon = gestorIdSalon(3)   
                    inactivarSalon(idSalon)
                    print(f"Se ha inactivado el salón con ID {idSalon} satisfactoriamente.")
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    print("Listado de salones activos:")
                    listarSalonesActivos()

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
                            eventos = gestionarEvento(idBanda, idSalon)
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
                    resumenMontoEventosPorBanda(bandas)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    topDuracionEventosDelMes()

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()