import csv

# Leer y mostrar los datos desde el archivo CSV
def leer_equipos_csv(nombre_archivo="equipos.csv"):
    equipos = []
    with open(nombre_archivo, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convertir los campos de cada jugador de cadena de texto a sus tipos correspondientes
            row["Edad"] = int(row["Edad"])
            row["Experiencia"] = int(row["Experiencia"])
            row["Promedio_Bateo"] = float(row["Promedio_Bateo"]) if row["Promedio_Bateo"] else None
            row["Juegos_Ganados"] = int(row["Juegos_Ganados"]) if row["Juegos_Ganados"] else None
            row["Juegos_Perdidos"] = int(row["Juegos_Perdidos"]) if row["Juegos_Perdidos"] else None
            row["Zurdo"] = row["Zurdo"] == "True"
            row["Promedio_Carreras_Limpias"] = float(row["Promedio_Carreras_Limpias"]) if row["Promedio_Carreras_Limpias"] else None
            equipos.append(row)
    return equipos
