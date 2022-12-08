import re
import histograma


def cargarDic(texto):
    with open(f"T6\{texto}.txt", "r", encoding="utf-8") as f:
        diccionario = f.read()
        diccionario = diccionario.lower()
        remplazar = {"'": "", "]": "", "´": "", "á": "a", "à": "a", "â": "a", "ä": "a", "ó": "o", "ò": "o", "ô": "o", "ö": "o", "é": "e", "è": "e", "ê": "e",
                     "ë": "e", "ė": "e", "ú": "u", "ü": "u", "ù": "u", "û": "u", "ç": "c", "č": "c", "ï": "i", "í": "i", "î": "i", "š": "s", "ž": "z", "œ": "ae"}
        for key, value in remplazar.items():
            diccionario = diccionario.replace(key, value)
        #result = re.split(
        #    r'[*+|°©ι=@<>[:;%/…–-•-,·ε’«»¡οτ!"()&?¿.\s\d]\s*', diccionario)
        result = diccionario.split(",")
        print(f"Diccionario {result}")
        # print(len(result))
        result = set(result)
        result = list(result)
        result_order = sorted(result)
        return result_order


def cargarTex(texto):
    with open(f"T6\{texto}.txt", "r", encoding="utf-8") as f:
        diccionario = f.read()
        diccionario = diccionario.lower()
        result = re.split(
            r'[^[a-z]\s\d]\s*', diccionario)
        # print(len(result))
        dic_rep = result
        result = set(result)
        result = list(result)
        return "".join(dic_rep)


def limpiar(texto):
    diccionario = texto.lower()
    remplazar = {"'": "", "]": "", "´": "", "á": "a", "à": "a", "â": "a", "ä": "a", "ó": "o", "ô": "o", "ö": "o", "é": "e", "è": "e", "ê": "e",
                "ë": "e", "ė": "e", "ú": "u", "ü": "u", "ù": "u", "û": "u", "ç": "c", "č": "c", "ï": "i", "í": "i", "î": "i", "š": "s", "ž": "z", "œ": "ae"}
    for key, value in remplazar.items():
        diccionario = diccionario.replace(key, value)
    result = re.split(
        r'[*+|°©ι=<>[:;%/…–-•-,·ε’«»¡!"()&?¿.\s\d]\s*', diccionario)
    dic_rep = result
    return "".join(dic_rep)


def escribir(diccionario, idioma):
    with open(f"T6\Dic{idioma}.txt", "w", encoding="utf-8") as fw:
        fw.write(str(diccionario))


def buscarCoincidencias(word, dic):
    coincidencias = 0
    word = word.lower()
    word2 = ""
    replace1 = {"m":"i","r":"e","u":"o","y":"a","n":"l","i":"r","j":"n","z":"t","v":"c"
    ,"p":"s","q":"p","e":"d","l":"m","o":"g","s":"u","w":"v","b":"f","k":"h","t":"b","c":"q"}
    #words = re.split(r"[\b\W\b]+", word)
    replace2 = {"d":"a","z":"v","w":"e","t":"o","b":"n","c":"r",
    "h":"l","k":"i","q":"b","y":"t","s":"c","f":"s","i":"g","x":"m","a":"u",
    "g":"p","n":"d","o":"f","v":"h","l":"z","p":"q"}
    #print(words)
    for c in word:
        if c in replace2:
            word2 += replace2[c]
        else:
            word2 += c
    print(word2)
    words = re.split(r"[\b\W\b]+", word2)
    w2 = []
    #idyyt
    for palabra in dic:
        if len(palabra) == 5 and palabra[2]==palabra[3]=="t" and palabra[1]=="a":
            w2.append(palabra)
    print(w2)
    #bw
    w3 = []
    for palabra in dic:
        if len(palabra) == 2 and palabra[1]=="e":
            w3.append(palabra)
    print(w3)
    for word in words:
        if word in dic:
            coincidencias += 1
            print(f"coincidencia: {word}")
    print(len(words))
    print(coincidencias)
