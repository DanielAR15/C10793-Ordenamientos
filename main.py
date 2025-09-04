import random
import numpy as np
import matplotlib.pyplot as plt

# -------- Generador de vectores --------
def generar_vectores(n_vectores=10, tam=100, minimo=1, maximo=100):
    return [random.choices(range(minimo, maximo + 1), k=tam) for _ in range(n_vectores)]

# -------- Algoritmos con contadores --------
def Burbuja(arr):
    Array = arr.copy()
    Length = len(Array)
    intercambios = 0
    for i in range(Length):
        for j in range(0, Length - i - 1):
            if Array[j] > Array[j + 1]:
                Array[j], Array[j + 1] = Array[j + 1], Array[j]
                intercambios += 1
    return intercambios

def Insercion(arr):
    Array = arr.copy()
    intercambios = 0
    for i in range(1, len(Array)):
        j = i
        while j > 0 and Array[j] < Array[j - 1]:
            Array[j], Array[j - 1] = Array[j - 1], Array[j]
            intercambios += 1
            j -= 1
    return intercambios

def Seleccion(arr):
    Array = arr.copy()
    Length = len(Array)
    intercambios = 0
    for i in range(Length):
        Minimo = i
        for j in range(i + 1, Length):
            if Array[j] < Array[Minimo]:
                Minimo = j
        if Minimo != i:
            Array[i], Array[Minimo] = Array[Minimo], Array[i]
            intercambios += 1
    return intercambios

# -------- Main --------
if __name__ == "__main__":
    vectores = generar_vectores()

    algoritmos = {
        "Bubble Sort": Burbuja,
        "Insertion Sort": Insercion,
        "Selection Sort": Seleccion,
    }

    resultados = {alg: [] for alg in algoritmos}

    # ejecutar cada algoritmo sobre los 10 vectores
    for vec in vectores:
        for nombre, func in algoritmos.items():
            interc = func(vec)
            resultados[nombre].append(interc)

    # imprimir tabla con promedio y desviación estándar
    print("Algoritmo\t\tPromedio Intercambios\tDesviación Estándar")
    for nombre, valores in resultados.items():
        promedio = np.mean(valores)
        desviacion = np.std(valores, ddof=1)
        print(f"{nombre:15}\t{promedio:20.2f}\t{desviacion:20.2f}")

    # boxplot
    plt.boxplot(resultados.values(), labels=resultados.keys())
    plt.title("Intercambios por algoritmo de ordenamiento")
    plt.ylabel("Número de intercambios")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()