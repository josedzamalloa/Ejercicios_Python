def run():
    print("Reto 5 - Rangos cambiantes")
    lim_inferior = int(input("Ingrese el limite inferior: "))
    lim_superior = int(input("Ingrese el limite superior: "))
    comparacion = int(input("Ingrese un numero de comparación: "))
    while comparacion < lim_inferior or comparacion > lim_superior:
        print("Número ingresado fuera de los limites: " + str(comparacion))
        comparacion = int(input("Ingrese otro numero de comparación: "))
    print("Número ingresado se encuentra dentro de los limites: " + str(comparacion))


if __name__ == "__main__":
    run()