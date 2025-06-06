import time

#Comenzamos creando el Insertion Sort, necesario para que funcione la búsqueda binaria mas adelante
def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

#Búsqueda Lineal, funciona directamente en listas desordenadas
def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

#Búsqueda Binaria, requiere que la lista esté ordenada previamente, como lo hicimos con insertion sort
def busqueda_binaria(lista, valor):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

#Lista desordenada
numeros = [17, 3, 25, 9, 30, 8, 41, 6, 22, 14, 12, 19, 5, 27, 11]

#Valor a buscar
objetivo = 12

#Aplicacion de búsqueda lineal, no hace falta ordenar la lista, medimos el tiempo con time
inicio_lineal = time.time()
pos_lineal = busqueda_lineal(numeros, objetivo)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Búsqueda Lineal: Elemento {objetivo} encontrado en la posición:", pos_lineal if pos_lineal != -1 else "No encontrado")
print(f"Tiempo de búsqueda lineal: {tiempo_lineal:.6f} segundos")

#Aplicacion de búsqueda binaria, medimos el tiempo nuevamente
#Primero ordenando la lista
lista_ordenada = numeros.copy()
insertion_sort(lista_ordenada)
print("Lista ordenada para búsqueda binaria:", lista_ordenada)
inicio_binaria = time.time()
pos_binaria = busqueda_binaria(lista_ordenada, objetivo)
fin_binaria = time.time()
tiempo_binaria = fin_binaria - inicio_binaria
print(f"Búsqueda Binaria: Elemento {objetivo} encontrado en la posición:", pos_binaria if pos_binaria != -1 else "No encontrado")
print(f"Tiempo de búsqueda binaria: {tiempo_binaria:.6f} segundos")
