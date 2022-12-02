def analizar(texto):
        letras ={}
        for letra in texto:
            letras[letra] = 0
        for letra in texto:
            letras[letra] += 1
        sorted_letras = dict(sorted(letras.items(), key=lambda item:item[1], reverse=True))
        print(sorted_letras)
        return sorted_letras

def escribir(diccionario,idioma):
        with open(f"T6\histograma{idioma}.csv","w",encoding="utf-8") as f:
            for llave, valor in diccionario.items():
                print(f"llave: {llave} valor: {valor}")
                f.write(f"{llave},{valor}\n")