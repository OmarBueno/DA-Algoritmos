import re

def escribirHistograma(histograma,idioma):
        with open(f"Proyecto Final\Recursos\histogramas\Histograma{idioma}.csv","w",encoding="utf-8") as f:
            for llave, valor in histograma.items():
                f.write(f"{llave},{valor}\n")

def escribirDiccionario(idioma):
    with open(f"Proyecto Final\Recursos\diccionarios\libros\libro{idioma}.txt", "r", encoding="utf-8") as fr:
        texto = fr.read()
        texto = texto.lower()
        #remplazar = {"'": "", "]": "", "´": "", "á": "a", "à": "a", "â": "a", "ä": "a", "ó": "o", "ò": "o", "ô": "o", "ö": "o", "é": "e", "è": "e", "ê": "e",
        #             "ë": "e", "ė": "e", "ú": "u", "ü": "u", "ù": "u", "û": "u", "ç": "c", "č": "c", "ï": "i", "í": "i", "î": "i", "š": "s", "ž": "z", "œ": "ae"}
        #for key, value in remplazar.items():
        #    diccionario = diccionario.replace(key, value)
        #result = re.split(
        #    r'[*+|°©ι=@<>[:;%/…–-•-,·ε’«»¡οτ!"()&?¿.\s\d]\s*', diccionario)
        result = re.split(r'[^[a-z]\s\d]\s*', texto)
        print(f"Diccionario {result}")
        # print(len(result))
        result = set(result)
        result = list(result)
        result_order = sorted(result)
        with open(f"Proyecto Final\Recursos\diccionarios\Dic{idioma}.txt", "w", encoding="utf-8") as fw:
            fw.write(str(result_order))

def leerDiccionario(idioma):
    with open(f"Proyecto Final\Recursos\diccionarios\Dic{idioma}.txt", "r", encoding="utf-8") as f:
        diccionario = f.read()
        diccionario = diccionario.lower()
        result = diccionario.split(",")
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
        result = re.split(r'[^[a-z]\s\d]\s*', texto)
        return "".join(result)

def limpiarTexto(texto):
    diccionario = texto.lower()
    remplazar = {"'": "", "]": "", "´": "", "á": "a", "à": "a", "â": "a", "ä": "a", "ó": "o", "ô": "o", "ö": "o", "é": "e", "è": "e", "ê": "e",
                "ë": "e", "ė": "e", "ú": "u", "ü": "u", "ù": "u", "û": "u", "ç": "c", "č": "c", "ï": "i", "í": "i", "î": "i", "š": "s", "ž": "z", "œ": "ae"}
    for key, value in remplazar.items():
        diccionario = diccionario.replace(key, value)
    result = re.split(
        r'[*+|°©ι=<>[:;%/…–-•-,·ε’«»¡!"()&?¿.\s\d]\s*', diccionario)
    dic_rep = result
    return "".join(dic_rep)