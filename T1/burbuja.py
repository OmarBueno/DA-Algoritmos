import random
import time


def burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if (lista[j] > lista[j+1]):
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista


def run():
    for i in range(1, 11):
        n = 2900
        n = n * i
        numeros = []
        while (len(numeros) < n):
            ale = random.randint(1, n)
            if not (ale in numeros):
                numeros.append(ale)
        inicio = time.time()
        lista2 = burbuja(numeros)
        print("------------")
        fin = time.time()
        print(f"El tiempo para {n} : {fin-inicio}")


if __name__ == "__main__":
    run()
