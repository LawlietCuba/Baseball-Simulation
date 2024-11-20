import csv

def seleccionar_jugadores_del_equipo(ruta_csv, nombre_equipo):
    jugadores = []
    keys_to_copy = ['Nombre', 'Posiciones', 'Promedio_Bateo']
    
    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        
        for fila in lector_csv:
            if(fila["Equipo"] == nombre_equipo):
                fila["Posiciones"] = fila["Posiciones"].replace(';', ' ').split()
                jugadores.append({key : fila[key] for key in keys_to_copy})
                
    return jugadores