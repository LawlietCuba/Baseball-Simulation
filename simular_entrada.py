import random

def turno_al_bate(jugador, promedio_bateo):
    # Determinar el resultado del turno basado en probabilidades
    resultado = random.random()
    if resultado < promedio_bateo:  # Si el jugador obtiene un hit
        tipo_hit = random.choices(["sencillo", "doble", "triple", "cuadrangular"], weights=[60, 25, 10, 5])[0]
        return f"Hit ({tipo_hit})", 1 if tipo_hit == "sencillo" else 2 if tipo_hit == "doble" else 3 if tipo_hit == "triple" else 4
    elif resultado < promedio_bateo + 0.1:  # Aproximadamente 10% probabilidad de base por bolas
        return "Base por bolas", 1
    else:
        return "Out", 0
    

# Función para simular una entrada de béisbol con tres outs
def simular_entrada(equipo_bateando, index_bateador):
    """Simula una entrada, gestionando los outs, hits y bases por bolas."""
    outs = 0
    carreras = 0
    hits = 0
    turno = index_bateador
    bases_ocupadas = [False, False, False]
    
    while outs < 3:  # Tres outs por entrada
        jugador = equipo_bateando[turno % len(equipo_bateando)]  # Ciclo sobre los jugadores del equipo
        resultado, bases_avanzadas = turno_al_bate(jugador, float(jugador["Promedio_Bateo"]))
        
        print(f"Turno {turno + 1}: {jugador['Nombre']} - {resultado}")
        
        if resultado == "Out":
            outs += 1  # Si el resultado es un out, incrementamos el contador de outs
        elif resultado == "Base por bolas":
            bases_ocupadas, carreras = carreras_anotadas(bases_ocupadas, 1, carreras)
        else:
            hits+=1
            # Si es hit, avanzamos en bases y contamos al jugador en base
            print("----------------------------------")
            print("There was a hit!")
            print(bases_ocupadas)
            print("Ö: ", outs)
            print("C: ", carreras)
            print("----------------------------------")
            
            bases_ocupadas, carreras = carreras_anotadas(bases_ocupadas, bases_avanzadas, carreras)
            
            print("----------------------------------")
            print("After the hit!")
            print(bases_ocupadas)
            print("O: ", outs)
            print("C: ", carreras)
            print("----------------------------------")
        
        turno += 1  # El siguiente turno

    return (carreras, hits, turno)


def carreras_anotadas(bases_ocupadas, bases_avanzadas, carreras):
    nuevas_bases_ocupadas = [False,False,False]
    
    #Simulación de la corrida de bases después de conocer cuál fue el tipo de hit
    for i in range(len(bases_ocupadas)):
        if(bases_ocupadas[i]):
            if(i + bases_avanzadas >= 3):
                carreras+=1
                bases_ocupadas[i] = False
            else:
                nuevas_bases_ocupadas[i + bases_avanzadas] = True
               
    if(bases_avanzadas <=3):
        nuevas_bases_ocupadas[bases_avanzadas-1] = True
                
    return nuevas_bases_ocupadas, carreras