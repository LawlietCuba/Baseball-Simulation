import simular_entrada as sen

def simular_partido(equipo1, equipo2):
    """
    Simula un partido completo de béisbol entre dos equipos.
    Args:
        equipo1: Lista de jugadores del equipo 1.
        equipo2: Lista de jugadores del equipo 2.
    Returns:
        marcador: Diccionario con el resultado del partido.
    """
    entradas = 9
    marcador = {"equipo1": 0, "equipo2": 0}
    hits_totales = {"equipo1": 0, "equipo2": 0}
    
    # Índices de bateadores iniciales para cada equipo
    index_bateador1 = 0
    index_bateador2 = 0
    
    for entrada in range(1, entradas + 1):
        # Equipo 1 batea
        carreras1, hits1, index_bateador1 = sen.simular_entrada(equipo1, index_bateador1)
        marcador["equipo1"] += carreras1
        hits_totales["equipo1"] += hits1
        
        # Equipo 2 batea
        carreras2, hits2, index_bateador2 = sen.simular_entrada(equipo2, index_bateador2)
        marcador["equipo2"] += carreras2
        hits_totales["equipo2"] += hits2

        # Mostrar resultados parciales
        print(f"Entrada {entrada}: Equipo 1: {marcador['equipo1']} carreras, Equipo 2: {marcador['equipo2']} carreras.")
    
    # Determinar el equipo ganador
    if marcador["equipo1"] > marcador["equipo2"]:
        ganador = "Equipo 1"
    elif marcador["equipo2"] > marcador["equipo1"]:
        ganador = "Equipo 2"
    else:
        ganador = "Empate"

    # Resultados finales
    resultado_final = {
        "marcador": marcador,
        "ganador": ganador,
        "hits": hits_totales
    }
    
    return resultado_final
