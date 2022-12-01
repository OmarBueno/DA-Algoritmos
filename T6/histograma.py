def run():
    def escribir(diccionario):
        with open("histograma.csv","w") as f:
            for llave, valor in diccionario.items():
                print(f"llave: {llave} valor: {valor}")
                f.write(f"{llave},{valor}\n")

    def analizar(alfabeto,texto):
        letras ={}
        for letra in texto:
            if letra in alfabeto:
                letras[letra] = 0
        for letra in texto:
            if letra in alfabeto:
                letras[letra] += 1
        print(letras)
        escribir(letras)

    analizar("abcdfghijklmnopqrstuvwxyz","""Todavía tengo casi todos mis dientes
casi todos mis cabellos y poquísimas canas
puedo hacer y deshacer el amor
trepar una escalera de dos en dos
y correr cuarenta metros detrás del ómnibus
o sea que no debería sentirme viejo
pero el grave problema es que antes
no me fijaba en estos detalles.""")     

if __name__ == "__main__":
    run()