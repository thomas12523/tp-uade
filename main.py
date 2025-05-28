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
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def agregarSalon(_salones):
    while True:
        IdSalon = input("Ingrese el ID del salón: ")
        if IdSalon in _salones:
            print("El ID del salón ya existe. Intente con otro ID.")
        else:
            break
        
    NombreSalon = input("Ingrese el nombre del salón: ")
    Ubicacion = input("Ingrese la ubicación del salón: ")
    Capacidad = int(input("Ingrese la capacidad del salón: "))
    Telefonos = [input("Ingrese el primer teléfono: "),
                 input("Ingrese el segundo teléfono: "),
                 input("Ingrese el tercer teléfono: ")]
    
    _salones[IdSalon] = {
        "activo": True,
        "NombreSalon": NombreSalon,
        "Ubicacion": Ubicacion,
        "Capacidad": Capacidad,
        "Telefonos": {"telefono1": Telefonos[0],
                     "telefono2": Telefonos[1],
                     "telefono3": Telefonos[2]}
    }

    return _salones

def modificarSalon(_salones):
    while True:
        IdSalon = input("Ingrese el ID del salón a modificar: ")
        if IdSalon not in _salones:
            print("El ID del salón no existe. Intente con otro ID.")
        else:
            break
    
    NombreSalon = input("Ingrese el nuevo nombre del salón: ")
    Ubicacion = input("Ingrese la nueva ubicación del salón: ")
    Capacidad = int(input("Ingrese la nueva capacidad del salón: "))
    Telefonos = [input("Ingrese el nuevo primer teléfono: "),
                 input("Ingrese el nuevo segundo teléfono: "),
                 input("Ingrese el nuevo tercer teléfono: ")]
    _salones[IdSalon] = {
        "NombreSalon": NombreSalon,
        "Ubicacion": Ubicacion,
        "Capacidad": Capacidad,
        "Telefonos": {"telefono1": Telefonos[0],
                     "telefono2": Telefonos[1],
                     "telefono3": Telefonos[2]}
    }

    return _salones

def inactivarSalon(_salones):
    while True:
        IdSalon = input("Ingrese el ID del salón a inactivar: ")
        if IdSalon not in _salones:
            print("El ID del salón no existe. Intente con otro ID.")
        else:
            break

    _salones[IdSalon]["activo"] = False
    return _salones

def listarSalonesActivos(_salones):
    for salon in _salones:
        if _salones[salon]["activo"] == True:
            print(f"IdSalon: {salon}")
            print(_salones[salon])



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    salones =   {'001':{"activo": True,
                     "NombreSalon": "chiquimundo",
                     "Ubicacion": "san martin",
                     "Capacidad" : 30,
                     "Telefonos": {"Telefono1": "1",
                                   "Telefono2": "2",
                                   "Telefono3": "3"
                                   }
                    },
                '002':{"activo": False,
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
                    salones = agregarSalon(salones)
                    print("Salones después de agregar uno nuevo:")
                    print(salones)
                    
                elif opcionSubmenu == "2":   # Opción 2 del submenú
                    salones = modificarSalon(salones)
                    print("Salones después de modificar:")
                    print(salones)
                
                elif opcionSubmenu == "3":   # Opción 3 del submenú
                    salones = inactivarSalon(salones)
                    print("Salones después de inactivar uno:")
                    print(salones)
                
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