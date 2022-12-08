import re

def escribirHistograma(histograma,idioma):
        with open(f"Proyecto Final\Recursos\histogramas\Histograma{idioma}.csv","w",encoding="utf-8") as f:
            for llave, valor in histograma.items():
                f.write(f"{llave},{valor}\n")

def escribirDiccionario(idioma):
    with open(f"Proyecto Final\Recursos\diccionarios\libros\libro{idioma}.txt", "r", encoding="utf-8") as fr:
        texto = fr.read()
        texto = texto.lower()
        result = re.split(r'[^a-z]', texto)
        print(f"Diccionario {result}")
        result = set(result)
        result = list(result)
        result_order = sorted(result)
        with open(f"Proyecto Final\Recursos\diccionarios\Dic{idioma}.txt", "w", encoding="utf-8") as fw:
            fw.write(str(result_order))

def leerDiccionario(idioma):
    with open(f"Proyecto Final\Recursos\diccionarios\Dic{idioma}.txt", "r", encoding="utf-8") as f:
        diccionario = f.read()
        diccionario = diccionario.lower()
        result = re.split(r'[^a-z]', diccionario)
        return result

def cargarLibro(idioma):
    with open(f"Proyecto Final\Recursos\libros\libro{idioma}.txt", "r", encoding="utf-8") as f:
        libro = f.read()
        libro = libro.lower()
        result = re.split(r'[^a-z]', libro)
        return "".join(result)

def cargarTexto(numero):
    with open(f"Proyecto Final\Recursos\encriptado\Texto{numero}.txt", "r", encoding="utf-8") as f:
        texto = f.read()
        texto = texto.lower()
        return texto

def limpiarTexto(texto):
    texto = texto.lower()
    result = re.split(r'[^a-z]', texto)
    return "".join(result)