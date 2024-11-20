import random

# My modules
import seleccionar_alineación as sa
import seleccionar_equipos as se
import seleccionar_jugadores as sj
import simular_partido as sp

import csv

# Ruta del archivo CSV
ruta_csv = "equipos.csv"

#Recibe dos equipos (ahora toma dos equipos)
teams = se.obtener_elementos_unicos(ruta_csv, "Equipo")
equipos_enfrentados_aleatorios = random.sample(list(teams), 2)

jugadores_en_casa = sj.seleccionar_jugadores_del_equipo(ruta_csv, equipos_enfrentados_aleatorios[0])
jugadores_visitantes = sj.seleccionar_jugadores_del_equipo(ruta_csv,equipos_enfrentados_aleatorios[1])


alineacion_en_casa = sa.seleccionar_alienación(jugadores_en_casa)
alineacion_visitante = sa.seleccionar_alienación(jugadores_visitantes)

print(alineacion_en_casa)
print(alineacion_visitante)

sp.simular_partido(alineacion_en_casa, alineacion_visitante)