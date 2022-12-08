import re

def sustituirHistogramas(histo1,histo2,texto):
    texto = texto.lower()
    texto2 = ""
    abecedario1 = [key for key in histo1.keys() ]
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

def desencriptar(llave,texto):
    texto2 = ""
    for c in texto:
        if c in llave:
            texto2 += llave[c]
        else:
            texto2 += c
    return texto2

def buscarCoincidencias(texto, diccionario):
    coincidencias = 0
    texto = texto.lower()
    #idyyt
    apoyo1 = []
    for palabra in diccionario:
        if len(palabra) == 5 and palabra[2]==palabra[3]=="t" and palabra[1]=="a":
            apoyo1.append(palabra)
    print(apoyo1)
    #bw
    apoyo2 = []
    for palabra in diccionario:
        if len(palabra) == 2 and palabra[1]=="e":
            apoyo2.append(palabra)
    print(apoyo2)
    #llaves de desencriptado
    llave1 = {"m":"i","r":"e","u":"o","y":"a","n":"l","i":"r","j":"n","z":"t","v":"c"
    ,"p":"s","q":"p","e":"d","l":"m","o":"g","s":"u","w":"v","b":"f","k":"h","t":"b","c":"q"}
    llave2 = {"d":"a","z":"v","w":"e","t":"o","b":"n","c":"r",
    "h":"l","k":"i","q":"b","y":"t","s":"c","f":"s","i":"g","x":"m","a":"u",
    "g":"p","n":"d","o":"f","v":"h","l":"z","p":"q"}
    #Texto remplazado con la llave
    texto2 = desencriptar(llave1,texto)
    print(texto2)
    #Busqueda de palabras clave en los diccionarios 
    desencriptado = re.split(r"[\b\W\b]+", texto2)
    #Busqueda de coincidencias con el texto desencriptado
    for palabra in desencriptado:
        if palabra in diccionario:
            coincidencias += 1
            #print(f"coincidencia: {palabra}")
    #palabrras del texto
    print(f"Palabras del texto:{len(desencriptado)}")
    #coincidencias encontradas
    print(f"Coincidencias encontradas:{coincidencias}")

    print(f"similitud {coincidencias/len(desencriptado)*100}")
    return coincidencias/len(desencriptado)