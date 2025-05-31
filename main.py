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
from checkInputs import checkInt, checkTelefono, checkString

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def gestorIdSalon(case, salones):
    """
    Descripción: Gestiona el ID del salón según el caso, caso 1 es para un nuevo salón, caso 2 para modificar un salon, caso 3 para inactivarlo.
    Input:
        case es del tipo int y salones es un diccionario con los salones existentes.
    Output:
        IdSalon (str): ID del salón ingresado por el usuario.
    
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
                break
            return IdSalon
    
def getInputSalon(case):
    """
    Descripción: Solicita los datos necesarios para agregar o modificar un salón. Si es case 1 entonces es para agregar un salón, si es case 2 entonces es para modificar un salón. Se utiliza un condicional para si es case 1 o 2, así se muestra el texto correspondiente. Además, se valida que los datos ingresados sean correctos.

    Input: case es un entero que indica si es para agregar (1) o modificar (2) un salón.
    Output:
        tupla: (nombreSalon, ubicacion, capacidad, telefonos)
    """
    while True:
        nombreSalon = input(f"Ingrese el {"" if case == 1 else "nuevo "}nombre del salón: ")
        if checkString(nombreSalon):
            break
        print("El nombre del salón no puede estar vacío. Intentelo de nuevo.")

    while True:
        ubicacion = input(f"Ingrese la {"" if case == 1 else "nueva "}ubicación del salón: ")
        if checkString(ubicacion):
            break
        print("La ubicación del salón no puede estar vacía. Intentelo de nuevo.")

    while True:
        capacidad = input(f"Ingrese la {"" if case == 1 else "nueva "}capacidad del salón: ")
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
            telefono = input(f"Ingrese el {"" if case == 1 else "nuevo "}teléfono {i+1} (10 dígitos): ")
            if checkTelefono(telefono):
                telefonos.append(telefono)
            else:
                print("El teléfono debe ser un número de 10 dígitos. Intentelo de nuevo.")
                break
        if len(telefonos) == 3:
            break

    return nombreSalon, ubicacion, capacidad, telefonos



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    salones =   {'1':{"activo": True,
                     "NombreSalon": "chiquimundo",
                     "Ubicacion": "san martin",
                     "Capacidad" : 30,
                     "Telefonos": {"Telefono1": "1",
                                   "Telefono2": "2",
                                   "Telefono3": "3"
                                   }
                    },
                '2':{"activo": False,
                     "NombreSalon": "pepe",
                     "Ubicacion": "pepe",
                     "Capacidad" : 30,
                     "Telefonos": {"Telefono1": "1",
                                   "Telefono2": "2",
                                   "Telefono3": "3"
                                   }
                    }}


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
                    ... #Ingresar bandas
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ... # Modificar bandas
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ... # Eliminar bandas
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ... # Listado de bandas activas

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
                    print("[1] Ingresar salón")
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
                    ... # Registro de eventos
        
        elif opcionMenuPrincipal == "4":   # Opción 4 del menú principal
            while True:
                while True:
                    opciones = 4
                    print()
                    print("---------------------------")
                    print("MENÚ PRINCIPAL > MENÚ DE SALON")
                    print("---------------------------")
                    print("[1] Eventos del Mes")
                    print("[2] Resumen Anual de eventos por salón(Cantidades)")
                    print("[3] Resumen Anual de eventos por salón(Pesos)")
                    print("[4] Banda que más entradas vendió en el mes")
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
                    ... # Eventos del Mes
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    ... # Resumen Anual de eventos por salón(Cantidades)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    ... # Resumen Anual de eventos por salón(Pesos)
                
                elif opcionSubmenu == "4":   # Opción 4 del submenú
                    ... # Banda que más entradas vendió en el mes

                input("\nPresione ENTER para volver al menú.") # Pausa entre opciones
                print("\n\n")

        if opcionSubmenu != "0": # Pausa entre opciones. No la realiza si se vuelve de un submenú
            input("\nPresione ENTER para volver al menú.")
            print("\n\n")


# Punto de entrada al programa
main()