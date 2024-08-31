#ordenación de arreglo multidimensional
#matriz bidimensional 3x3
from operator import truediv, itruediv, index

from semana_11.programa1 import arre_bi

arre_bi =[
    [12,34,70], # índice 0
    [5,80,10 ], #í ndice 1
    [20,25,40]  # índice 2
]
#matriz desordenada

#booblesort
#implementación de función para ordenar la matriz

def bubble_sort(fila):
   n = len(fila)
   for i in range(n):
       for j in range(0,n-i-1):
           if fila[j] > fila[j+1]:
               #intercambiar si  el valor del elemento encontrado es mayor que el siguiente
               fila[j],fila[j+1] = fila[j+1],fila[j]

def ordenar_fila(arre_bi, fila_index):
    # ordenar la fila en arre_bi
    if 0 <= fila_index < len(arre_bi):
        bubble_sort(arre_bi[fila_index])
    else:
        print("error en el valor ")

#mostrar el valor de la matriz anterior
print("matriz anterior")
for fila in arre_bi:
    print(fila)

#fila a ordenar por ejemplo la fila 1
fila_ordenar = 1

#llamamos a la funcón para ordenar
ordenar_fila(arre_bi, fila_ordenar)

#mostrar matriz con la fila ordenada
print("/n arre_bi con la fila ordenada")
for fila in arre_bi:
    print(fila)







