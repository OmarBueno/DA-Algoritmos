import re
import histograma

def cargar():
    with open("T6\Libro2.txt","r",encoding="utf-8") as f :
        diccionario = f.read()
        diccionario = diccionario.lower()
        diccionario = diccionario.replace("]","")
        result = re.split(r'[*+|°©ι=<>[:;%/…–-•-,·ε’«»¡!"()&?¿.\s\d]\s*', diccionario)
        dic_rep = result
        result = set(result)
        result = list(result)
        result_order = sorted(result)  
        #print(result_order)
        #print(len(result_order))
        with open("T6\DicIta2.txt","w",encoding="utf-8") as fw :
            fw.write(str(result_order))
        return "".join(dic_rep)

diccionario = cargar()
#print(diccionario)
histo = histograma.analizar(diccionario)
histograma.escribir(histo,"frances")