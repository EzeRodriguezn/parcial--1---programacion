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
def cargar_matriz_notas(n, m): # Función para cargar una matriz de n alumnos por m exámenes
    matriz = []  #  lista vacía para guardar la matriz
    for i in range(n): # va por cada fila (alumno)
        fila = []  # Lista vacía donde se almacenan las notas de un alumno
        for j in range(m):# va por cada columna (examen)
            nota_valida = False  # Bandera para repetir la carga en el caso de que no sea valida
            while not nota_valida: 
                nota = input(f"Ingrese la nota del alumno {i+1}, examen {j+1}: ")
                if nota.isdigit():  # Verifica que es un número
                    nota = int(nota)
                    if 1 <= nota <= 10: # Valida que sea un número entero entre 1 y 10
                        nota_valida = True
                        fila.append(nota) # Agrega la nota validada
                    else:
                        print("La nota debe estar entre 1 y 10.")
                else:
                    print("Debe ingresar un número entero.")
        matriz.append(fila)  # Agrega la fila completa a la matriz
    return matriz


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
