#crear una función que calcule el descuento y valor total de una compra
print("Bienvenido al sistema de descuento en compras")
inicio= input("Ingrese: si, si desea incluir el descuento del 20% y no, si desea incluir otro descuento ")


#definir el nombre de la función
def calcular_descuento (monto_total_compra, porcent_desc= 20):
    total_desc= monto_total_compra * porcent_desc/100
    return total_desc

#solicitar el precio del producto
compra= input("por favor ingrese el precio del producto: $ ")
if compra == "":
    print("Esto es un error: ingrese valores númericos ")

else:
    try:
        # si el usuario ingresa un valor que no es válido el programa lanzara un error (value error)
        # convertimos la compra en un valor númerico
        monto= float(compra)

        if inicio == "si":

            # llamamos a la función con el descuento por defecto del 20%
            total_desc = calcular_descuento(monto)
            print(f"el total de descuento es: $ {total_desc:f}")

        else:
            # si el usuario desea otro descuento, pedimos que ingrese el porcentaje
             otro_desc= input("ingrese el porcentaje de descuento que desea aplicar:")
            
            # tambien convertimos ese valor a entero
             total_desc= calcular_descuento(monto,int(otro_desc))
             print(f"el total de descuento es: $ {total_desc:f}")

        # calculamos el total de la compra con el descuento aplicado
        total_compra = monto - total_desc
        print(f"El precio final de su compra aplicando el descuento es: $ {total_compra:f} ")

    except  ValueError:
        # si ocurre un error al hacer la conversión a número el bloque except captura ese error
        # estamos manejando errores tipo valueError
        print("Error: Porfavor ingrese un valor númerico válido ")

print("gracias por su compra")
print("Que tenga un buen día ")