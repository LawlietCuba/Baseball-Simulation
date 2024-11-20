import csv
import uuid
import random

# Define all primary baseball positions
primary_positions = ["Pitcher", "Catcher", "First_Base", "Second_Base", 
                     "Third_Base", "Shortstop", "Left_Field", "Center_Field", "Right_Field"]

# Function to generate a team with at least one player per position
def generar_equipo(nombre_equipo, num_jugadores):
    equipo = []

    # Ensure one player per primary position
    for position in primary_positions:
        id_jugador = uuid.uuid4()
        nombre = f"Jugador_{id_jugador.hex[:6]}"
        edad = random.randint(18, 40)
        experiencia = random.randint(1, 20)
        posiciones = [position]
        efectividad_posiciones = {position: round(random.uniform(0.5, 1.0), 2)}
        promedio_bateo = round(random.uniform(0.2, 0.35), 3)

        # Attributes specific for pitchers
        if position == "Pitcher":
            juegos_ganados = random.randint(0, 10)
            juegos_perdidos = random.randint(0, 10)
            zurdo = random.choice([True, False])
            promedio_carreras_limpias = round(random.uniform(1.5, 4.5), 2)
        else:
            juegos_ganados = None
            juegos_perdidos = None
            zurdo = None
            promedio_carreras_limpias = None

        equipo.append({
            "ID": id_jugador,
            "Equipo": nombre_equipo,
            "Nombre": nombre,
            "Edad": edad,
            "Experiencia": experiencia,
            "Posiciones": "; ".join(posiciones),
            "Efectividad_Posiciones": "; ".join([f"{pos}: {efectividad_posiciones[pos]}" for pos in posiciones]),
            "Promedio_Bateo": promedio_bateo,
            "Juegos_Ganados": juegos_ganados,
            "Juegos_Perdidos": juegos_perdidos,
            "Zurdo": zurdo,
            "Promedio_Carreras_Limpias": promedio_carreras_limpias
        })

    # Add additional players to complete the roster up to num_jugadores
    for _ in range(num_jugadores - len(primary_positions)):
        id_jugador = uuid.uuid4()
        nombre = f"Jugador_{id_jugador.hex[:6]}"
        edad = random.randint(18, 40)
        experiencia = random.randint(1, 20)
        posiciones = random.sample(primary_positions, k=random.randint(1, 3))
        efectividad_posiciones = {pos: round(random.uniform(0.5, 1.0), 2) for pos in posiciones}
        promedio_bateo = round(random.uniform(0.2, 0.35), 3)

        # Attributes specific for pitchers if randomly assigned as one
        if "Pitcher" in posiciones:
            juegos_ganados = random.randint(0, 10)
            juegos_perdidos = random.randint(0, 10)
            zurdo = random.choice([True, False])
            promedio_carreras_limpias = round(random.uniform(1.5, 4.5), 2)
        else:
            juegos_ganados = None
            juegos_perdidos = None
            zurdo = None
            promedio_carreras_limpias = None

        equipo.append({
            "ID": id_jugador,
            "Equipo": nombre_equipo,
            "Nombre": nombre,
            "Edad": edad,
            "Experiencia": experiencia,
            "Posiciones": "; ".join(posiciones),
            "Efectividad_Posiciones": "; ".join([f"{pos}: {efectividad_posiciones[pos]}" for pos in posiciones]),
            "Promedio_Bateo": promedio_bateo,
            "Juegos_Ganados": juegos_ganados,
            "Juegos_Perdidos": juegos_perdidos,
            "Zurdo": zurdo,
            "Promedio_Carreras_Limpias": promedio_carreras_limpias
        })
    return equipo

# Generate two teams with at least one player for each position
equipo_1 = generar_equipo("Equipo_A", 15)
equipo_2 = generar_equipo("Equipo_B", 15)

# Save to CSV
with open("equipos.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=[
        "ID", "Equipo", "Nombre", "Edad", "Experiencia", "Posiciones", 
        "Efectividad_Posiciones", "Promedio_Bateo", "Juegos_Ganados", 
        "Juegos_Perdidos", "Zurdo", "Promedio_Carreras_Limpias"
    ])
    writer.writeheader()
    writer.writerows(equipo_1 + equipo_2)
