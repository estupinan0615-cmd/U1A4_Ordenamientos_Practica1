# U1A4 - Evaluación de Métodos de Ordenamiento

##  Descripción

En esta práctica se implementaron y evaluaron dos algoritmos de ordenamiento en Python:

- Bubble Sort
- QuickSort (recursivo)

Se realizaron pruebas de rendimiento utilizando diferentes tamaños de entrada y se analizaron los tiempos de ejecución.

---

##  Objetivo

Comparar el rendimiento de Bubble Sort y QuickSort mediante pruebas controladas, midiendo tiempos de ejecución y analizando su eficiencia computacional.

---

## Tecnologías utilizadas

- Python 3
- timeit
- pandas
- Excel
- GitHub

---

## Metodología

Se generaron listas de los siguientes tamaños:

- 100
- 1000
- 5000
- 10000

Para cada tamaño se realizaron:

- 5 repeticiones por algoritmo
- Lista Aleatoria
- Lista Invertida

Se calcularon:

- Tiempo promedio
- Desviación estándar

---

## 📈 Resultados

### 🔹 Tabla de resultados (lista aleatoria)

| Tamaño | Bubble Sort (s) | QuickSort (s) |
|--------|------------------|---------------|
| 100    | 0.00042984       | 0.0000671     |
| 1000   | 0.03214292       | 0.00090948    |
| 5000   | 0.82571382       | 0.00688954    |
| 10000  | 3.4371196        | 0.0168524     |

---

### 📊 Gráfica comparativa

![Grafica](Practica%201/Evidencias/grafica_comparativa.png)

---

## Análisis

Los resultados muestran que QuickSort tiene un mejor desempeño conforme aumenta el tamaño de la entrada. Esto se debe a su complejidad promedio de **O(n log n)**, mientras que Bubble Sort presenta una complejidad de **O(n²)**.

Se observa que Bubble Sort incrementa su tiempo de ejecución de manera acelerada cuando el tamaño de los datos crece, mientras que QuickSort mantiene un crecimiento mucho más controlado.

En aplicaciones de robótica y procesamiento de datos en tiempo real, QuickSort resulta más adecuado debido a su eficiencia.

---

## Estructura del repositorio
