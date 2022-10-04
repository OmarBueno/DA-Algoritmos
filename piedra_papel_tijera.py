import random
opciones = ["piedra", "papel", "tijera"]


def jugar(jugador, oponente):
    print("*"*10)
    print(
        f"El jugador eligio: {opciones[jugador-1]} \nEl oponente eligio: {opciones[oponente-1]}")
    if ((jugador - oponente) % 3) == 0:
        print("Empate")
    elif ((jugador - oponente) % 3) == 1:
        print("Ganaste")
    else:
        print("perdiste")


def run():
    for i in range(10):
        jugar(random.randint(1, 3), random.randint(1, 3))


if __name__ == "__main__":
    run()
