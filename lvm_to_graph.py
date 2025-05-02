import pandas as pd
import matplotlib.pyplot as plt

def lvm_to_graph(ruta_lvm, nombre_imagen_salida):
    """
    Lee un archivo .lvm, genera una gráfica y la guarda como imagen.
    """
    # Leer el archivo
    with open(ruta_lvm, 'r') as file:
        lines = file.readlines()

    # Detectar el inicio de los datos
    data_start = 0
    for idx, line in enumerate(lines):
        if line.strip() == '[DATA]':
            data_start = idx + 1
            break

    # Leer datos
    data = pd.read_csv(ruta_lvm, sep='\t', skiprows=data_start)

    # Asumir que las dos primeras columnas son tiempo y valor
    time = data.iloc[:, 0]
    std_value = data.iloc[:, 1]

    # Crear gráfica
    plt.figure(figsize=(6.4, 6.4))
    plt.plot(time, std_value)
    plt.xlabel('Time (s)')
    plt.ylabel('Standardization Value')
    plt.title('230609 Aqua 415')
    plt.tight_layout()
    plt.savefig(nombre_imagen_salida, dpi=100)
    plt.close()
