def run():
    print("Reto 3 - Conversor de millas a kilómetros")
    print("Elige 1: Convertir millas a kilometros")
    print("Elige 2: Convertir kilometros a millas")
    opcion = int(input("Opcion elegida: "))
    if opcion == 1:
        x = int(input("Ingrese la cantidad de millas que desea convertir: "))
        y = mile_to_km(x)
        print(str(x)+" millas equivale a " + str(y) + " kilómetros.")
    elif opcion == 2:
        x = int(input("Ingrese la cantidad de kilómetros que desea convertir: "))
        y = km_to_mile(x)
        print(str(x)+" kilómetros equivale a " + str(y) + " millas.")
    else:
        print("Opción no válida. Programa terminado")

def mile_to_km(x):
    km = x * 1.609344
    return km

def km_to_mile(x):
    mile = x / 1.609344
    return mile

if __name__ == "__main__":
    run()