def run():
    print("RETO 1 - Área de un triángulo")
    base = int(input("Ingrese la base del triángulo: "))
    altura = int(input("Ingrese la altura del triángulo: "))
    area = (base * altura)/2
    print("El área del triángulo es: " + str(area))
    opcion = input("¿Desea saber el tipo de triángulo? Escriba (y) para continuar: ")
    if opcion.lower() =="y":
        lado1 = int(input("Ingrese el primer lado del triángulo: "))
        lado2 = int(input("Ingrese el segundo lado del triángulo: "))
        tipo_triangulo(lado1, lado2, base)
    else:
        print("Terminó el programa. Gracias.")

def tipo_triangulo(a, b, c):
    if a==b and b==c:
        print("El triángulo es Equilatero.")
    elif a==b or a==c or b==c:
        print("El triángulo es Isóceles.")
    else:
        print("El triángulo es Escaleno.")

if __name__ == "__main__":
    run()