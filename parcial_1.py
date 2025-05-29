"""
PARTE 2   EJERCICIO PRÁCTICO
Contexto: Una institución educativa necesita registrar las notas de sus
alumnos en distintos exámenes. Cada fila de una matriz representa un
alumno y cada columna un examen.
Requisitos Generales para Todos los Puntos:
- Se deben modularizar todas las operaciones. No se permite resolver
todo en el main.
- No está permitido el uso de funciones propias de Python como max,
min, sum, enumerate, etc.
- La validación debe hacerse en la función de carga, verificando que
cada nota sea un número entero entre 1 y 10.
- Se debe implementar un menú con opciones para ejecutar cada punto
de forma separada.
- Usar estructuras adecuadas, acumuladores, contadores y recorrido
doble.
- Nombrar las funciones tal como se indican a continuación.
1  Función cargar_matriz_notas(): Recibe dos enteros n y m y permite
cargar n x m notas válidas entre 1 y 10 inclusive. La validación debe
hacerse dentro de esta función.
2  Función porcentaje_aprobados(): Calcula el porcentaje de
exámenes aprobados (nota ≥ 6) por cada alumno y muestra un resumen
individual. Usar contadores y acumuladores.


3  Función mejor_promedio(): Calcula el promedio de cada alumno y
determina cuál tiene el mejor promedio. Retorna el índice del alumno y
el valor del promedio.
4  Función buscar_nota(): Recibe la matriz y una nota buscada, y
retorna una lista con todas las posiciones (fila, columna) donde aparece
esa nota exacta.
"""

# Función para cargar una matriz de notas de n alumnos y m exámenes
def cargar_matriz_notas(n,m):
    matriz = []  # Lista donde se va a guardar la matriz de notas
    for i in range(n):  # va por cada alumno
        fila = []  # Lista vacía para guardar las notas del alumno i

        for j in range(m):  # va por cada  examen
            nota = 0  
            while nota < 1 or nota > 10:  # me fijo si el numeor ingresado esta entre el 1 y 10
                nota = int(input("Nota del alumno " + str(i + 1) + ", examen " + str(j + 1) + ": "))
                if nota < 1 or nota > 10:
                    print("Nota inválida. Debe estar entre 1 y 10.")

            fila.append(nota)  # Agregamos la nota válida a la fila del alumno

        matriz.append(fila)  # Agregamos la fila completa a la matriz

    return matriz  # Devolvemos la matriz completa con todas las notas


# Función para calcular el porcentaje de aprobados
def porcentaje_aprobados(matriz):
    for i in range(len(matriz)):
        total_examenes = 0 #contador
        aprobados = 0 #contador
        for j in range(len(matriz[i])):
            nota = matriz[i][j] 
            total_examenes += 1
            if nota >= 6: #se fija si el examen esta aprobado
                aprobados += 1 #incrementa el contador de aprobados
        porcentaje = (aprobados * 100) / total_examenes # Se calcula el porcentaje
        print(f"Alumno {i+1}: {porcentaje}% de exámenes aprobados.")
