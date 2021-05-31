import random

score_user = 0
score_ia = 0


def run():
    print("RETO 2 - Piedra, papel o tijera")
    #opcion = input("Escriba su opción: 1:Piedra, (papel) o (tijera): ")
    
    while score_ia < 4 or score_user < 4:
        opcion = input("Escriba su opción: (piedra), (papel) o (tijera): ")
        ia = aleatorio()    
        ganador(ia, opcion)
        print("Score actual: IA - "+str(score_ia)+ ", Tu "+str(score_user))
        if score_ia == 3:
            print("Te ganó la IA, terminó el juego.")
            break
        if score_user == 3:
            print("Felicidades, derrotaste a la IA, terminó el juego.")
            break

def ganador(ia, user):
    global score_ia
    global score_user
    if ia == "papel" and user == "piedra":
        print("Pierdes, la IA eligió " + ia)
        score_ia = score_ia+1
    elif ia == "papel" and user == "tijera":
        print("Tu ganas, la IA eligió " + ia)
        score_user = score_user + 1
    elif ia == "papel" and user == "papel":
        print("Empate, , la IA también eligió " + ia)
    elif ia == "piedra" and user == "piedra":
        print("Empate, , la IA también eligió " + ia)
    elif ia == "piedra" and user == "tijera":
        print("Pierdes, la IA eligió " + ia)
        score_ia = score_ia+1
    elif ia == "piedra" and user == "papel":
        print("Tu ganas, la IA eligió " + ia)
        score_user = score_user + 1
    elif ia == "tijera" and user == "piedra":
        print("Tu ganas, la IA eligió " + ia)
        score_user = score_user + 1
    elif ia == "tijera" and user == "tijera":
        print("Empate, , la IA también eligió " + ia)
    elif ia == "tijera" and user == "papel":
        print("Pierdes, la IA eligió " + ia)
        score_ia = score_ia+1


def aleatorio():
    ia_opcion = random.randint(1, 3)
    if ia_opcion == 1:
        return "piedra"
    elif ia_opcion == 2:
        return "papel"
    else:
        return "tijera"
    


if __name__ == "__main__":
    run()