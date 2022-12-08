from collections import OrderedDict


def analizar(texto):
        letras ={}
        for letra in texto:
            letras[letra] = 0
        for letra in texto:
            letras[letra] += 1
        for llave,valor in letras.items():
            letras[llave] = letras[llave]/len(texto)
        print(len(texto))
        sorted_letras = dict(sorted(letras.items(), key=lambda item:item[1], reverse=True))
        #print(sorted_letras)
        #sorted_letras = OrderedDict(sorted(letras.items()))
        print(sorted_letras)
        return sorted_letras

def analizarTexto(texto):
        letras ={}
        for letra in texto:
            letras[letra] = 0
        for letra in texto:
            letras[letra] += 1        
        print(len(texto))
        sorted_letras = dict(sorted(letras.items(), key=lambda item:item[1], reverse=True))
        #sorted_letras = OrderedDict(sorted(letras.items()))
        print(sorted_letras)
        return sorted_letras

def escribir(diccionario,idioma):
        with open(f"T6\histograma{idioma}.csv","w",encoding="utf-8") as f:
            for llave, valor in diccionario.items():
                #print(f"llave: {llave} valor: {valor}")
                f.write(f"{llave},{valor}\n")

def comparar(histo1,histo2):
    similitud = 0
    for llave,valor in histo1.items():
        #print(f"{histo2[llave]} * {histo1[llave]}")
        if llave in histo1 and llave in histo2:
            similitud += histo1[llave] * histo2[llave]
    print(similitud)

def sustituir(histo1,histo2,texto):
    texto = texto.lower()
    texto2 = ""
    abecedario1 = [key for key in histo1.keys() ]
    abecedario2 = [key for key in histo2.keys()]
    print(abecedario1)
    print("___________________________________")
    print(abecedario2)
    histo3 ={}
    for valor_a, valor_b in zip(histo1.keys(),histo2.keys()):
        histo3[valor_a] = valor_b
    for letra in texto:
        if letra in abecedario1:
            texto2 += histo3[letra]
        else:
            texto2 += letra
    print(histo3)
    print(texto2)