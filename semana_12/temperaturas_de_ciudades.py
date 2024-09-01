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

# calcular el promedio de las temperaturas para una ciudad por cada dia de la semana
for ciudad in temperatura:
    for semana in ciudad :
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)




