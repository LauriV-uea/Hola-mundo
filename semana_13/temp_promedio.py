#desarrollar una función para calcular temperaturas promedio durante un período de tiempo
#crear una matriz 3D para almacenar las temperaturas de cuidades
#primera dimensión ciudades (3 ciudades: Quito, Cuenca, Ambato)
#segunda dimensión semanas ( 4 semanas)
#tercera dimensión días de la semana (7 días )

temperatura = [
    [   #ciudad 1 Quito
       [    #semana 1
            {"day": "lunes" , "temp": 67},
            {"day": "martes" , "temp": 80},
            {"day": "miércoles" , "temp": 44},
            {"day": "jueves" , "temp": 64},
            {"day": "viernes" , "temp": 65},
            {"day": "sábado" , "temp": 78},
            {"day": "domingo" , "temp": 67}
       ],
       [    # semana 2
           {"day": "lunes", "temp": 80},
           {"day": "martes", "temp": 50},
           {"day": "miércoles", "temp": 80},
           {"day": "jueves", "temp": 89},
           {"day": "viernes", "temp": 56},
           {"day": "sábado", "temp": 90},
           {"day": "domingo", "temp": 67}

       ],
       [  # semana 3
           {"day": "lunes", "temp": 55},
           {"day": "martes", "temp": 50},
           {"day": "miércoles", "temp": 88},
           {"day": "jueves", "temp": 89},
           {"day": "viernes", "temp": 76},
           {"day": "sábado", "temp": 98},
           {"day": "domingo", "temp": 127}
       ],
       [     # semana 4
           {"day": "lunes", "temp": 89},
           {"day": "martes", "temp": 50},
           {"day": "miércoles", "temp": 80},
           {"day": "jueves", "temp": 88},
           {"day": "viernes", "temp": 76},
           {"day": "sábado", "temp": 60},
           {"day": "domingo", "temp": 78}
       ]
    ],
    [    # ciudad 2 Cuenca
        [  #semana 1
           {"day": "lunes", "temp": 45},
           {"day": "martes", "temp": 46},
           {"day": "miércoles", "temp": 80},
           {"day": "jueves", "temp": 98},
           {"day": "viernes", "temp": 76},
           {"day": "sábado", "temp": 68},
           {"day": "domingo", "temp": 78}
        ],
        [   # semana 2
           {"day": "lunes", "temp": 99},
           {"day": "martes", "temp": 89},
           {"day": "miércoles", "temp": 56},
           {"day": "jueves", "temp": 80},
           {"day": "viernes", "temp": 66},
           {"day": "sábado", "temp": 98},
           {"day": "domingo", "temp": 68}
        ],
        [   # semana 3
            {"day": "lunes", "temp": 79},
            {"day": "martes", "temp": 89},
            {"day": "miércoles", "temp": 96},
            {"day": "jueves", "temp": 90},
            {"day": "viernes", "temp": 96},
            {"day": "sábado", "temp": 88},
            {"day": "domingo", "temp": 68}
        ],
        [   # semana 4
            {"day": "lunes", "temp": 79},
            {"day": "martes", "temp": 99},
            {"day": "miércoles", "temp": 66},
            {"day": "jueves", "temp": 90},
            {"day": "viernes", "temp": 76},
            {"day": "sábado", "temp": 88},
            {"day": "domingo", "temp": 78}
        ]
    ],
    [   # ciudad 3 Ambato
        [     # semana 1
            {"day": "lunes", "temp": 99},
            {"day": "martes", "temp": 79},
            {"day": "miércoles", "temp": 66},
            {"day": "jueves", "temp": 70},
            {"day": "viernes", "temp": 66},
            {"day": "sábado", "temp": 67},
            {"day": "domingo", "temp": 65}

        ],
        [   # semana 2
            {"day": "lunes", "temp": 90},
            {"day": "martes", "temp": 99},
            {"day": "miércoles", "temp": 56},
            {"day": "jueves", "temp": 40},
            {"day": "viernes", "temp": 43},
            {"day": "sábado", "temp": 98},
            {"day": "domingo", "temp": 67}
        ],
        [    # semana 3
            {"day": "lunes", "temp": 67},
            {"day": "martes", "temp": 89},
            {"day": "miércoles", "temp": 66},
            {"day": "jueves", "temp": 80},
            {"day": "viernes", "temp": 76},
            {"day": "sábado", "temp": 58},
            {"day": "domingo", "temp": 58}
        ],
        [   # semana 4
            {"day": "lunes", "temp": 89},
            {"day": "martes", "temp": 67},
            {"day": "miércoles", "temp": 96},
            {"day": "jueves", "temp": 98},
            {"day": "viernes", "temp": 66},
            {"day": "sábado", "temp": 58},
            {"day": "domingo", "temp": 68}
        ]
    ]
]
#nombres de las 3 ciudades
nombres_ciudades = ("Quito", "Cuenca", "Ambato")

#definición de una función para calcular el promedio de temperaturas de ciudades
def calcular_promedio_temperaturas (temperatur):
    promedio=[]    #lista para almacenar los promedios
    total_semanas= len(temperatur[0])   # numero de semanas
    total_dias_semana= len(temperatur[0][0])   #numero de días en cada semana


    #recorremos la lista de ciudades
    for ciudad in temperatura:
        suma_temperatura = 0
        total_dias = 0   #iniciamos en cero 

        #recorremos la lista de semanas para cada ciudad
        for semana in ciudad:
            #recorremos la lista de cada semana
            for dia in semana:
                suma_temperatura +=dia["temp"]  # sumar las temperaturas de los dias
                total_dias +=1  #contar los dias

         #calculamos el promedio de temperatura para cada ciudad
        promedio_ciudad= suma_temperatura/ total_dias
        promedio.append(promedio_ciudad)    #añadir el promedio a la lista de resultados

        #calculamos el período de tiempo(número total de días)
        periodo_tiempo= total_semanas * total_dias_semana


    return promedio,periodo_tiempo

#llamamos ala función
promedio,periodo_tiempo = calcular_promedio_temperaturas(temperatura)

#mostramos los resultados
for i, promedio_ciudad in enumerate(promedio):
    print(f"La temperatura promedio en {nombres_ciudades[i]} durante el período de {periodo_tiempo} días es: {promedio_ciudad:.2f}ºF")





















