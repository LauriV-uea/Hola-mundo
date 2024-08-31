#busqueda de un arreglo bidimensional
#matriz bidimensional 3x3
arre_bi= [
    [25,39,40],
    [10,23,15],
    [10,50,15]
]
#valor que estamos buscando
vlr_buscando = 23

#inicializar una variable para buscar el valor
fil_encontrada= [-1]
colum_encontrada= [-1]

#recorrer la matriz para buscar el valor
for fil in range (len(arre_bi)):
    for colum in range (len(arre_bi[fil])):
        if arre_bi[fil][colum]== vlr_buscando:
            fil_encontrada = fil
            colum_encontrada = colum
            break
#salir del bucle si se encuentra el valor que estamos buscando

# verificar si se ha encontrado el valor y mostrar la posición del valor

if fil_encontrada != -1:
    print(f"se encontro el valor{vlr_buscando} en la fila {fil_encontrada}y columna {colum_encontrada}")

else:
    print("no se ha encontrado el valor en la matriz")
