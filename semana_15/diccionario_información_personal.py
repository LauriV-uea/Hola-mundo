# crear un diccionario con información ficticia sobre una persona

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("****** sistema de información personal  ****** ")

# definimos una función para que imprima los valores de forma vertical
def diccionario_vertical (diccionario):
    for clave, valor in diccionario.items():
        if isinstance(valor, dict):        # esto es para saber si es un diccionario
            print(f"{clave}:")
            for subclave, subvalor in valor.items():
                print(f"{subclave}: {subvalor}")     # imprimimos cada subclave y subvalor

        elif isinstance(valor, list):    # para comprobar si el valor de la clave es una lista
            print(f"{clave}:")
            for item in valor:          # recorremos cada item de la clave
                print(f" -{item}")       # se imprime cada elemento de la lista con -
        else:
            print(f"{clave}: {valor}")

# definimos un nombre a nuestro diccionario
# le añadimos la información correspondiente
information_personal = {
    "Nombre": "Fernando Perez",
    "Edad": 45 ,
    "Ciudad": "Buenos Aires" ,
    "Peso": 70 ,     # el peso de la persona es en kilogramos
    "Altura": 1.70 ,      # la altura de la persona es en metros
    "Email": "fer_1989@gmail.com" ,
    "Dirección": {
        "calle": "avenida 10 de octubre"
    },
    "Estado civil": "Casado"  ,
    "Hijos": 1  ,
    "Profesión": "Abogado"  ,   # se indica que la persona es abogado
    "Experiencia laboral": {
        "Empresa": "Bufete Legal Whasington ",    # se indica el nombre del bufete
        "Cargo": "Abogado asociado"        # se indica que es un abogado empleado
    },
    "Pasatiempos": [
        "Hacer ejercicio",    # lo que hace en su tiempo libre
        "Ver películas" ,
        "Leer"  ,
    ],
    "Idioma": [
        "español",
        "italiano",
        "inglés"
    ]
}

# llamamos a la función para que imprima el diccionario original  de forma vertical
print("***** diccionario original *****")
diccionario_vertical(information_personal)  # llamamos a la función

print("\n modificando el diccionario ......")
# accedemos al valor clave ciudad y le modificamos por otra ciudad
information_personal["Ciudad"] = "España"


# le agregamos una nueva clave-valor al diccionario profesión
information_personal["segunda_profesión"] = "Doctor"


# verificar si existe la clave telefono en el diccionario
if "telefono" in information_personal:
    print(information_personal["telefono"])
else:
    print("\nno existe la clave telefono  en el diccionario, agregando número.......")


# agregamos la clave telefono en el diccionario
information_personal["telefono"] = 9567578348


#eliminar la clave edad
del information_personal["Edad"]


#imprimir el diccionario modificado
print("******  diccionario modificado  ******")
diccionario_vertical(information_personal)     # llamamos de nuevo a al función para que imprima el diccionario modificado





