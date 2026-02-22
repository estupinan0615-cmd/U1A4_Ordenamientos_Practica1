import random
import timeit
import statistics
import csv


# ==============================
# Bubble Sort
# ==============================
def bubble_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ==============================
# QuickSort (recursivo)
# ==============================
def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]

    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return quicksort(menores) + iguales + quicksort(mayores)


# ==============================
# Generadores de datos
# ==============================
def generar_lista_aleatoria(n):
    return [random.randint(0, 10000) for _ in range(n)]


def generar_lista_invertida(n):
    return list(range(n, 0, -1))


# ==============================
# Medición de tiempo
# ==============================
def medir_tiempo(funcion, lista, repeticiones=5):

    tiempos = []

    for _ in range(repeticiones):

        tiempo = timeit.timeit(
            lambda: funcion(lista),
            number=1
        )

        tiempos.append(tiempo)

    promedio = statistics.mean(tiempos)
    desviacion = statistics.stdev(tiempos)

    return tiempos, promedio, desviacion


# ==============================
# Programa principal
# ==============================
def main():

    tamanos = [100, 1000, 5000, 10000]

    repeticiones = 5

    resultados = []

    print("Evaluando algoritmos...\n")

    for n in tamanos:

        print(f"Probando tamaño: {n}")

        lista_aleatoria = generar_lista_aleatoria(n)
        lista_invertida = generar_lista_invertida(n)

        # Bubble Sort - Aleatoria
        tiempos, prom, desv = medir_tiempo(
            bubble_sort, lista_aleatoria, repeticiones
        )

        resultados.append([
            n,
            "Bubble Sort",
            "Aleatoria",
            repeticiones,
            prom,
            desv
        ])

        # Bubble Sort - Invertida
        tiempos, prom, desv = medir_tiempo(
            bubble_sort, lista_invertida, repeticiones
        )

        resultados.append([
            n,
            "Bubble Sort",
            "Invertida",
            repeticiones,
            prom,
            desv
        ])

        # QuickSort - Aleatoria
        tiempos, prom, desv = medir_tiempo(
            quicksort, lista_aleatoria, repeticiones
        )

        resultados.append([
            n,
            "QuickSort",
            "Aleatoria",
            repeticiones,
            prom,
            desv
        ])

        # QuickSort - Invertida
        tiempos, prom, desv = medir_tiempo(
            quicksort, lista_invertida, repeticiones
        )

        resultados.append([
            n,
            "QuickSort",
            "Invertida",
            repeticiones,
            prom,
            desv
        ])

    # ==========================
    # Guardar CSV
    # ==========================

    with open("resultados_ordenamiento.csv", "w", newline="") as archivo:

        writer = csv.writer(archivo)

        writer.writerow([
            "Tamano",
            "Algoritmo",
            "Tipo Lista",
            "Repeticiones",
            "Promedio (s)",
            "Desviacion Std (s)"
        ])

        writer.writerows(resultados)

    print("\nResultados guardados en resultados_ordenamiento.csv")


# Ejecutar programa
if __name__ == "__main__":
    main()
