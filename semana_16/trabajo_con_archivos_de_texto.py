# realizar operaciones de lectura y escritura con archivos de texto en python


print("x-x-x-x-x-..... archivos de texto x-x-x-x-x.....")
# escritura de archivo de texto
# creando un nuevo archivo llamado "my_notes.txt"
archivo = "my_notes.txt"

#modo de apertura "w" de escritura
archivo_escritura = open(archivo, "w")

# metodo write, escribir una línea a  la vez
archivo_escritura.write("Hola, mi nombre es Lauri.\n")
archivo_escritura.write("Hoy es un nuevo día para aprender algo.\n")
archivo_escritura.write("Hacer ejercicios 3 veces esta semana.\n")
archivo_escritura.write("Me gusta escuchar música y ver series.\n")
archivo_escritura.write("Terminar el informe del trabajo mañana.\n")
archivo_escritura.write("Estudiar para el exámen de inglés.\n")
archivo_escritura.write("Ir a la escuela de la niña.\n")
archivo_escritura.close()

#Lectura de archivo de texto
archivo_lectura = open(archivo, "r")


# usamos seek para reiniciar el cursor al principio del archivo
archivo_lectura.seek(0)

# metodo de lectura de texto  readline, leer una línea a la vez
linea_1 =archivo_lectura.readline()
linea_2 = archivo_lectura.readline()
linea_3 = archivo_lectura.readline()
linea_4 = archivo_lectura.readline()
linea_5 = archivo_lectura.readline()
linea_6 = archivo_lectura.readline()
linea_7 = archivo_lectura.readline()


# imprimimos las lineas de texto linea por linea
# usamos el strip para eliminar los saltos de lineas al final
print("\nmostar el contenido línea por línea ")
print("línea 1:", linea_1.strip())
print("línea 2:", linea_2.strip())
print("línea 3:", linea_3.strip())
print("línea 4:", linea_4.strip())
print("línea 5:", linea_5.strip())
print("línea 6:", linea_6.strip())
archivo_lectura.close()

