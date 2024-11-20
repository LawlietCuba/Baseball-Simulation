import csv

def obtener_elementos_unicos(ruta_csv, columna):
    """
    Obtiene los elementos únicos de una columna en un archivo CSV.
    
    :param ruta_csv: Ruta del archivo CSV.
    :param columna: Nombre de la columna de la cual extraer elementos únicos.
    :return: Conjunto de elementos únicos.
    """
    elementos_unicos = set()

    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)

        for fila in lector_csv:
            valor = fila[columna].strip()
            # Agregar múltiples valores separados por coma como elementos individuales
            if ',' in valor:
                elementos_unicos.update(valor.split(','))
            else:
                elementos_unicos.add(valor)

    return elementos_unicos
