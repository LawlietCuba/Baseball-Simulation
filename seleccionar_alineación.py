def seleccionar_alienación(jugadores):
    """
    Selecciona exactamente 9 jugadores asegurándose de cubrir todas las posiciones básicas del béisbol.
    """
    posiciones_necesarias = {
        "Pitcher": False,
        "Catcher": False,
        "First_Base": False,
        "Second_Base": False,
        "Shortstop": False,
        "Third_Base": False,
        "Left_Field": False,
        "Center_Field": False,
        "Right_Field": False
    }
    
    equipo = []
    
    for jugador in jugadores:
        for posicion in jugador["Posiciones"]:
            if posicion in posiciones_necesarias and not posiciones_necesarias[posicion]:
                equipo.append({
                    "Nombre": jugador["Nombre"],
                    "Posición": posicion,
                    "Promedio_Bateo": jugador["Promedio_Bateo"]
                })
                posiciones_necesarias[posicion] = True
                break  # Pasamos al siguiente jugador una vez que cubrió una posición
    
        # Si ya seleccionamos 9 jugadores, terminamos
        if len(equipo) == 9:
            break
    
    # Validación: Asegurarse de que todas las posiciones estén cubiertas
    if not all(posiciones_necesarias.values()):
        raise ValueError("No se pudieron cubrir todas las posiciones necesarias con los jugadores disponibles.")
    
    return equipo

