def analizar(texto):
        letras ={}
        for letra in texto:
            letras[letra] = 0
        for letra in texto:
            letras[letra] += 1
        for llave,valor in letras.items():
            letras[llave] = (letras[llave]/len(texto)) * 100
        histograma = dict(sorted(letras.items(), key=lambda item:item[1], reverse=True))
        #print(sorted_letras)
        #sorted_letras = OrderedDict(sorted(letras.items()))
        #print(histograma)
        return histograma

def comparar(histo1,histo2):
    similitud = 0
    for llave,valor in histo1.items():
        if llave in histo1 and llave in histo2:
            similitud += histo1[llave] * histo2[llave]
    #print(similitud)
    return similitud/10