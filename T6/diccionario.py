import re
import histograma

def cargar(texto,idioma):
    with open(f"T6\{texto}.txt","r",encoding="utf-8") as f :
        diccionario = f.read()
        diccionario = diccionario.lower()
        remplazar = {"'": "","]": "","´":"","á": "a","à":"a","â":"a","ä":"a","ó":"o","ô":"o","ö":"o","é":"e","è":"e","ê":"e","ë":"e","ė":"e"
        ,"ú":"u","ü":"u","ù":"u","û":"u","ç":"c","č":"c","ï":"i","í":"i","î":"i","š":"s","ž":"z","œ":"ae"}
        for key, value in remplazar.items():
            diccionario = diccionario.replace(key, value)
        result = re.split(r'[*+|°©ι=<>[:;%/…–-•-,·ε’«»¡οτ!"()&?¿.\s\d]\s*', diccionario)
        dic_rep = result
        result = set(result)
        result = list(result)
        result_order = sorted(result)  
        #print(result_order)
        #print(len(result_order))
        with open(f"T6\Dic{idioma}.txt","w",encoding="utf-8") as fw :
            fw.write(str(result_order))
        return "".join(dic_rep)

def limpiar(texto):
        diccionario = texto.lower()
        remplazar = {"'": "","]": "","´":"","á": "a","à":"a","â":"a","ä":"a","ó":"o","ô":"o","ö":"o","é":"e","è":"e","ê":"e","ë":"e","ė":"e"
        ,"ú":"u","ü":"u","ù":"u","û":"u","ç":"c","č":"c","ï":"i","í":"i","î":"i","š":"s","ž":"z","œ":"ae"}
        for key, value in remplazar.items():
            diccionario = diccionario.replace(key, value)
        result = re.split(r'[*+|°©ι=<>[:;%/…–-•-,·ε’«»¡!"()&?¿.\s\d]\s*', diccionario)
        dic_rep = result
        return "".join(dic_rep)