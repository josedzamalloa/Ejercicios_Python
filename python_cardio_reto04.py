import math 

def run():
    print("Reto 4 - Calculadora de volúmenes")
    radio = int(input("Ingrese el radio: "))
    altura = int(input("Ingrese la altura: "))
    print("El volumen del cilindro es: " + str(cilindro(radio, altura)))

def cilindro(radio, altura):
    return math.pi*radio*radio*altura

if __name__ == "__main__":
    run()
