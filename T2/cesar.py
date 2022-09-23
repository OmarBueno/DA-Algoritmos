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


def decifrar(word, key):
    word = word.lower()
    decifrado = ""
    for c in word:
        if c in alfabeto:
            posicion = (alfabeto.find(c) - key) % len(alfabeto)
            decifrado += alfabeto[posicion]
        else:
            decifrado += c
    return decifrado


def buscarCoincidencias(word):
    dic = read("T2\words.txt")
    coincidencias = 0
    words = word.split()
    for word in words:
        if word in dic:
            coincidencias += 1
    return coincidencias


def decifrar_bruto(word):
    word = word.lower()
    mejor_llave = 0
    coincidencias_dic = 0
    for key in range(1, len(alfabeto)+1):
        decifrado = ""
        for c in word:
            if c in alfabeto:
                posicion = (alfabeto.find(c) - key) % len(alfabeto)
                decifrado += alfabeto[posicion]
            elif c == " ":
                decifrado += c
        coincidencias = buscarCoincidencias(decifrado)
        if coincidencias > coincidencias_dic:
            coincidencias_dic = coincidencias
            mejor_llave = key
    print(f"La mejor llave es {mejor_llave}")
    return decifrar(word, mejor_llave)


def run():
    word = """a zsnw dwsjfwv lzsl hwghdw oadd xgjywl ozsl qgm ksav, hwghdw oadd xgjywl ozsl qgm vav, 
        tml hwghdw oadd fwnwj xgjywl zgo qgm esvw lzwe xwwd. - esqs sfywdgm.  a slljatmlw eq kmuuwkk lg lzak: a 
        fwnwj ysnw gj lggc sfq wpumkw. –xdgjwfuw fayzlafysdw.  lzw twkl laew lg hdsfl s ljww osk 20 qwsjk syg. 
        lzw kwugfv twkl laew ak fgo. –uzafwkw hjgnwjt. a se fgl s hjgvmul gx eq uajumeklsfuwk. a se s hjgvmul gx eq vwuakagfk. 
        –klwhzwf ugnwq. uzsfyw qgmj lzgmyzlk sfv qgm uzsfyw qgmj ogjdv. –fgjesf nafuwfl hwsdw"""
    decifrado = decifrar_bruto(word)
    print(f"La palabra cifrada: {word}\nLa palabra decifrada {decifrado}")


if __name__ == "__main__":
    run()
