from datetime import datetime
import json

def listarEventosDelMes():
    """
    Lista todos los eventos programados para un mes específico.
    
    Muestra una tabla formateada con la información de todos los eventos
    que ocurren en el mes indicado, incluyendo fecha/hora, IDs y tramos contratados.
    
    Args:
        eventos (dict): Diccionario con información de eventos donde la clave es el ID
                        y el valor contiene datos del evento (idEvento, idBanda, idSalon,
                        fechaEvento, tramosContratados).
        mes (int): Número del mes (1-12) para filtrar los eventos.
    
    Returns:
        None: La función imprime directamente los resultados en consola.
    """
    print(f"{'Fecha/Hora':<20} {'idEvento':<10} {'idBanda':<10} {'idSalon':<10} {'fechaEvento':<15} {'tramosContratados':<18}")
    print('-' * 85)

    try:
        eventos=open('eventos.json',mode="r", encoding="utf-8")
        eventosJson=json.load(eventos)
        eventos.close()
    except (FileNotFoundError, OSError, json.JSONDecodeError) as detalle:
        print("Error al intentar abrir archivoo:", detalle)
        return {}
     
    for id_evento, evento in eventosJson.items():

        eventDate= datetime.strptime(evento["fechaEvento"],"%Y.%m.%d")
            
        if eventDate.month == datetime.now().month:
            fecha_hora = id_evento
            idEvento = evento['idEvento']
            idBanda = evento['idBanda']
            idSalon = evento['idSalon']
            fechaEvento = evento['fechaEvento']
            tramosContratados = evento['tramosContratados']

            print(f"{fecha_hora:<20} {idEvento:<10} {idBanda:<10} {idSalon:<10} {fechaEvento:<15} {tramosContratados:<18}")

    return

def resumenCantidadEventosPorBanda():
    """
    Genera un resumen de la cantidad total de eventos mensuales por banda.
    
    Crea una tabla que muestra cuántos eventos tiene programada cada banda
    por mes durante el año 2025, organizando la información en columnas
    por mes y filas por banda.
    
    Args:
        eventos (dict): Diccionario con información de eventos donde cada evento
                        contiene idBanda, fechaEvento y otros datos.
        bandas (dict): Diccionario con información de bandas donde la clave
                        es el idBanda.
    
    Returns:
        None: La función imprime directamente el resumen en consola.
    """
    
    meses = ["ENE.25", "FEB.25", "MAR.25", "ABR.25", "MAY.25", "JUN.25",
            "JUL.25", "AGO.25", "SEP.25", "OCT.25", "NOV.25", "DIC.25"]
    
    print("-" * 150)
    print("CANTIDAD TOTAL DE EVENTOS MENSUALES POR BANDA")
    print("-" * 150)
    print(f"{'idBanda':<25}", end="")
    for mes in meses:
        print(f"{mes:>8}", end="")
    print()
    print("-" * 150)
    
    try: 
        bandas=open('bandas.json',mode="r", encoding="utf-8")
        bandasJson=json.load(bandas)
        bandas.close()

        eventos=open('eventos.json',mode="r", encoding="utf-8")
        eventosJson=json.load(eventos)
        eventos.close()
    except (FileNotFoundError, OSError, json.JSONDecodeError) as detalle:
        print("Error al intentar abrir archivo:", detalle)
        return {}
    
    for idBanda, banda in bandasJson.items():
        recuentoEventos = {month: 0 for month in range(1, 13)}
        for idEvento, evento in eventosJson.items():
            if str(idBanda)==evento["idBanda"]:
                eventDate= datetime.strptime(evento["fechaEvento"],"%Y.%m.%d")
                recuentoEventos[eventDate.month]+=1
                
        print(f"{idBanda:<25}", end="")
        for recuentoMensual in recuentoEventos.items():
            print(f"{recuentoMensual[1]:>8}", end="")
        print()

    return

def resumenMontoEventosPorBanda():
    """
    Calcula y muestra el monto total mensual generado por cada banda.
    
    Genera una tabla que presenta los ingresos mensuales de cada banda,
    calculados multiplicando los tramos contratados por la tarifa de 30 minutos
    de cada banda para todos sus eventos del mes.
    
    Args:
        eventos (dict): Diccionario con eventos que contiene idBanda, fechaEvento,
                        tramosContratados y otros datos del evento.
        bandas (dict): Diccionario con información de bandas que incluye
                        tarifa30Min para cada banda.
    
    Returns:
        None: La función imprime directamente el resumen financiero en consola.
    """
    
    meses = ["ENE.25", "FEB.25", "MAR.25", "ABR.25", "MAY.25", "JUN.25",
            "JUL.25", "AGO.25", "SEP.25", "OCT.25", "NOV.25", "DIC.25"]
    
    print("-" * 150)
    print("MONTO TOTAL MENSUAL POR BANDA")
    print("-" * 150)
    print(f"{'idBanda':<10}", end="")
    for mes in meses:
        print(f"{mes:>11}", end="")
    print()
    print("-" * 150)

    try:
        bandas=open('bandas.json',mode="r", encoding="utf-8")
        bandasJson=json.load(bandas)
        bandas.close()

        eventos=open('eventos.json',mode="r", encoding="utf-8")
        eventosJson=json.load(eventos)
        eventos.close()
    except (FileNotFoundError, OSError, json.JSONDecodeError) as detalle:
        print("Error al intentar abrir archivo:", detalle)
        return {}
    
    for idBanda, banda in bandasJson.items():
        recuentoEventos = {month: 0 for month in range(1, 13)}
        for idEvento, evento in eventosJson.items():
            if str(idBanda) == evento["idBanda"]:
                eventDate = datetime.strptime(evento["fechaEvento"], "%Y.%m.%d")
                recuentoEventos[eventDate.month] += evento["tramosContratados"] * banda["Tarifa30Min"]
                
        print(f"{idBanda:<10}", end="")
        for i in range(1, 13):
            print(f"{recuentoEventos[i]:>10}$", end="")
        print()


    return

def claveOrden(evento):
    return evento[1]['tramosContratados']

def topDuracionEventosDelMes():
    """
    Muestra los 3 eventos con mayor duración de un mes específico.
    
    Filtra los eventos del mes indicado, los ordena por cantidad de tramos
    contratados (duración) de menor a mayor, y muestra los 3 eventos de
    mayor duración. Si hay menos de 3 eventos, informa que no hay suficientes.
    
    Args:
        eventos (dict): Diccionario con información de eventos que incluye
                        fechaEvento, tramosContratados, idEvento y otros datos.
        mes (int): Número del mes (1-12) para filtrar los eventos.
    
    Returns:
        None: La función imprime directamente el top 3 en consola.
    
    Note:
        La función contiene un error en el algoritmo de ordenamiento 
        (variable 'j' no está definida correctamente).
    """
    try:
        eventos=open('eventos.json',mode="r", encoding="utf-8")
        eventosJson=json.load(eventos)
        eventos.close()
    except (FileNotFoundError, OSError, json.JSONDecodeError) as detalle:
        print("Error al intentar abrir archivo(s):", detalle)
        return {}
    
    eventosDelMes={}

    for id_evento, evento in eventosJson.items():
        eventDate= datetime.strptime(evento["fechaEvento"],"%Y.%m.%d")

        if eventDate.month == datetime.now().month:
            eventosDelMes[id_evento]=evento
    
    eventosOrdenados=list(sorted(eventosDelMes.items(), key=claveOrden))
        
    print("-" * 150)
    print("TOP 3 EVENTOS CON MAYOR DURACION DEL MES")
    print("-" * 150)
    print("EVENTOS")
    print("-" * 150)
    if len(eventosOrdenados) >=3:
        print(f"Evento {eventosOrdenados[-1][1]['idEvento']} {eventosOrdenados[-1][1]['tramosContratados']:>8} tramos contratados.")
        print(f"Evento {eventosOrdenados[-2][1]['idEvento']} {eventosOrdenados[-2][1]['tramosContratados']:>8} tramos contratados.")
        print(f"Evento {eventosOrdenados[-3][1]['idEvento']} {eventosOrdenados[-3][1]['tramosContratados']:>8} tramos contratados.")
    else: 
        print("No hay sufientes eventos en el mes para generar un top.")
    return