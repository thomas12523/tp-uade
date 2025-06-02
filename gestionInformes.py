from datetime import datetime, date

# items hace que el diccionario sea una tupla(clave, valor)

def listarEventosDelMes(eventos: dict, mes:int):
    print("Los eventos del mes son:")
    for id_evento, evento in eventos.items():
        eventDate= datetime.strptime(evento["fechaEvento"],"%Y.%m.%d")
        if eventDate.month==mes:
            print("\n",f"Evento ID: {evento['idEvento']}")
            print(f"   Fecha: {evento['fechaEvento']}")
            print(f"   Banda ID: {evento['idBanda']}")
            print(f"   Salón ID: {evento['idSalon']}")
            print(f"   Tramos contratados: {evento['tramosContratados']}")
    return

def resumenCantidadEventosPorBanda(eventos: dict):
    diccionarioEventos={}
    for idEvento, evento in eventos.items():
        if evento["idBanda"] in diccionarioEventos:
            diccionarioEventos[evento["idBanda"]]+=1
        else:
            diccionarioEventos[evento["idBanda"]]=1
    for idBanda, cantidad in diccionarioEventos.items():
        print(f"Banda {idBanda}: {cantidad} evento(s)")
    return

def resumenMontoEventosPorBanda(eventos: dict, bandas: dict):
    diccionarioEventos={}
    for idEvento, evento in eventos.items():
        if evento["idBanda"] in diccionarioEventos:
            diccionarioEventos[evento["idBanda"]]+=evento["tramosContratados"]
        else:
            diccionarioEventos[evento["idBanda"]]=evento["tramosContratados"]
    for idBanda, banda in bandas.items():
        if idBanda in diccionarioEventos:
            print(f"Banda {idBanda}: ${diccionarioEventos[idBanda]*banda['tarifa30Min']}")
    return

def topDuracionEventosDelMes(eventos: dict): # primero ordeno de menor a mayor y despues imprimo los ultimos 
    #use insertion sort transformando al diccionario de diccionarios en una lista de tuplas con list y con items
    listaEventos = list(eventos.items())
    
    for i in range(1,len(listaEventos)):
        idActual, datosActuales = listaEventos[i] # aca guardo el id del evento actual y los datos del evento actual
        j = i - 1
        while j >= 0 and listaEventos[j][1]["tramosContratados"] > datosActuales["tramosContratados"]:
            listaEventos[j + 1] = listaEventos[j]
            j -= 1
        listaEventos[j + 1] = (idActual, datosActuales)
        
    print("\nTop 3 de los eventos con mayor duración del mes:") # aca imprimo usando indice negativo los top 3
    print(f"Evento {listaEventos[-1][1]['idEvento']}: {listaEventos[-1][1]['tramosContratados']} tramos contratados.") #el primer indice es el de la lista, el segundo el de la tupla(id, valores), y el tercer indice para el valor de tramos contratados 
    print(f"Evento {listaEventos[-2][1]['idEvento']}: {listaEventos[-2][1]['tramosContratados']} tramos contratados.")
    print(f"Evento {listaEventos[-3][1]['idEvento']}: {listaEventos[-3][1]['tramosContratados']} tramos contratados.")
    return