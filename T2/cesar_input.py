alfabeto = "abcdefghijklmnopqrstuvwxyz"


def read(file):
    dic = []
    with open(file, "r", encoding="utf-8") as f:
        dic = f.read().split()
    return dic


def cifrar(word, key):
    word = word.lower()
    cifrado = ""
    for c in word:
        if c in alfabeto:
            posicion = (alfabeto.find(c) + key) % len(alfabeto)
            cifrado += alfabeto[posicion]
        else:
            cifrado += c
    return cifrado


def descifrar(word, key):
    word = word.lower()
    descifrado = ""
    for c in word:
        if c in alfabeto:
            posicion = (alfabeto.find(c) - key) % len(alfabeto)
            descifrado += alfabeto[posicion]
        else:
            descifrado += c
    return descifrado


def buscarCoincidencias(word,dic):
    coincidencias = 0
    words = word.split()
    for word in words:
        if word in dic:
            coincidencias += 1
    return coincidencias


def descifrar_bruto(word):
    dic = read("T2\words.txt")
    word = word.lower()
    mejor_llave = 0
    coincidencias_dic = 0
    for key in range(1, len(alfabeto)+1):
        descifrado = ""
        for c in word:
            if c in alfabeto:
                posicion = (alfabeto.find(c) - key) % len(alfabeto)
                descifrado += alfabeto[posicion]
            elif c == " ":
                descifrado += c
        coincidencias = buscarCoincidencias(descifrado,dic)
        if coincidencias > coincidencias_dic:
            coincidencias_dic = coincidencias
            mejor_llave = key
    print(f"\nLa mejor llave es {mejor_llave}, se encontraron: {coincidencias_dic} coincidencias de palabras")
    return descifrar(word, mejor_llave)


def run():
    opcion = 0
    while opcion != 4:
        opcion = int(input("""¿Qué desea hacer?
        1. cifrar palabra
        2. decifrar palabra con llave
        3. decifrar palabra sin llave
        4. salir
        """))
        if opcion == 1:
            word = input("Ingrese la palabra a cifrar: ")
            key = int(input("Ingrese la llave: "))
            cifrado = cifrar(word, key)
            print(f"\nUsted Ingreso: {word}\nLa palabra cifrada: {cifrado}")
            print("--------------------------------------")
        elif opcion == 2:
            word = input("Ingrese la palabra a decifrar: ")
            key = int(input("Ingrese la llave: "))
            descifrado = descifrar(word, key)
            print(
                f"\nUsted Ingreso: {word}\nLa palabra descifrada: {descifrado}")
            print("--------------------------------------")
        elif opcion == 3:
            word = input("Ingrese la palabra a decifrar: ")
            descifrado = descifrar_bruto(word)
            print(
                f"\nUsted Ingreso: {word}\nLa palabra descifrada: {descifrado}")
            print("--------------------------------------")
        else:
            print("Ingrese una opción valida")


if __name__ == "__main__":
    run()
