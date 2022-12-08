from Archivos import Archivos 
from Utilerias import histograma,decifrador

#Cargar Diccionarios
diccionario_espanol = Archivos.leerDiccionario("Español")
diccionario_frances = Archivos.leerDiccionario("Frances")
diccionario_italiano = Archivos.leerDiccionario("italiano")
diccionario_ingles = Archivos.leerDiccionario("Ingles")
#Escribir diccionarios
"""Archivos.escribirDiccionario("Español")
Archivos.escribirDiccionario("Frances")
Archivos.escribirDiccionario("Italiano")
Archivos.escribirDiccionario("Ingles")"""
#Cargar Texto y limpiarlo
texto1 = Archivos.cargarTexto("1")
texto2 = Archivos.cargarTexto("2")
#Cargar Histogramas
histo_espanol = histograma.analizar(Archivos.cargarLibro("Español"))
histo_frances = histograma.analizar(Archivos.cargarLibro("Frances"))
histo_italiano = histograma.analizar(Archivos.cargarLibro("Italiano"))
histo_ingles = histograma.analizar(Archivos.cargarLibro("Ingles"))
histo_texto1 = histograma.analizar(Archivos.limpiarTexto(texto1))
histo_texto2 = histograma.analizar(Archivos.limpiarTexto(texto2))
#Escribir histogramas
"""Archivos.escribirHistograma(histo_espanol,"Español")
Archivos.escribirHistograma(histo_espanol,"Frances")
Archivos.escribirHistograma(histo_espanol,"Italiano")
Archivos.escribirHistograma(histo_espanol,"Ingles")
Archivos.escribirHistograma(histo_texto1,"Texto1")
Archivos.escribirHistograma(histo_texto2,"Texto2")"""

print(f"Histograma Español {histo_espanol}")
print("_"*30)

print(f"Histograma Frances {histo_frances}")
print("_"*30)

print(f"Histograma Italiano {histo_italiano}")
print("_"*30)

print(f"Histograma Ingles {histo_ingles}")
print("_"*30)

print(f"Histograma Texto1 {histo_texto1}")
print("_"*30)

print(f"Histograma Texto2 {histo_texto2}")
print("_"*30)

#Se probaron palabras clave de cada texto para decifrar las llaves
#palabras_clavet1 = ["Mn","pqrppu","omynnu","ernnr","n'rpzirlmzy","lutmnm","wmwr","vuqqmy","vsvvmunm","oisqqm",
#"csyzziu","zyzzmnm","nmwrnnu","ynny","ynn'ynnrwylrjzu"]
#probadas1 = "ynny,ynn,ernnr,mn"
#palabras_clave2 = ["dzwzd","idyyt","gdwfw","h’dz","Kbodyyk","fw","bw","btb","h’dzcwqqw"]
#probadas2 = ["dzwzd","Kbodyyk","btb","gdwfw"]

#Similitud entre texto e idiomas
print(f"Similitud entre texto 1 y español {histograma.comparar(histo_texto1,histo_espanol)}")
print(f"Similitud entre texto 1 y frances {histograma.comparar(histo_texto1,histo_frances)}")
print(f"Similitud entre texto 1 y italiano {histograma.comparar(histo_texto1,histo_italiano)}")
print(f"Similitud entre texto 1 y ingles {histograma.comparar(histo_texto1,histo_ingles)}")
print("_"*30)

print(f"Similitud entre texto 2 y español {histograma.comparar(histo_texto2,histo_espanol)}")
print(f"Similitud entre texto 2 y frances {histograma.comparar(histo_texto2,histo_frances)}")
print(f"Similitud entre texto 2 y italiano {histograma.comparar(histo_texto2,histo_italiano)}")
print(f"Similitud entre texto 2 y ingles {histograma.comparar(histo_texto2,histo_ingles)}")
print("_"*30)

#print(diccionario_italiano)
llave1 = {"m":"i","r":"e","u":"o","y":"a","n":"l","i":"r","j":"n","z":"t","v":"c"
    ,"p":"s","q":"p","e":"d","l":"m","o":"g","s":"u","w":"v","b":"f","k":"h","t":"b","c":"q"}
llave2 = {"d":"a","z":"v","w":"e","t":"o","b":"n","c":"r",
    "h":"l","k":"i","q":"b","y":"t","s":"c","f":"s","i":"g","x":"m","a":"u",
    "g":"p","n":"d","o":"f","v":"h","l":"z","p":"q"}
print(decifrador.desencriptar(llave1,texto1))
print("_"*30)
print(decifrador.desencriptar(llave2,texto2))
#decifrador.buscarCoincidencias(texto1,diccionario_italiano)
#decifrador.buscarCoincidencias(texto2,diccionario_italiano)