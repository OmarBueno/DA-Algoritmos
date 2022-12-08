import histograma,diccionario

diccionario_espanol = diccionario.cargarDic("Libro1")
texto_espanol = diccionario.cargarTex("Libro1")
histo_espanol = histograma.analizar(texto_espanol)
histograma.escribir(histo_espanol,"español")
abecedario_espanol = [letra for letra in histo_espanol.keys()]
print(histo_espanol)
print(sorted(abecedario_espanol))
print("_______________________________")

diccionario_frances = diccionario.cargarDic("Libro2")
print("--------------------------")
print(len(diccionario_frances))
print("--------------------------")
texto_frances = diccionario.cargarTex("Libro2")
histo_frances = histograma.analizar(texto_frances)
histograma.escribir(histo_frances,"frances")
abecedario_frances = [letra for letra in histo_frances.keys()]
print(histo_frances)
print(sorted(abecedario_frances))
print("_______________________________")

diccionario_italiano = diccionario.cargarDic("Libro4")
texto_italiano = diccionario.cargarTex("Libro4")
histo_italiano = histograma.analizar(texto_italiano)
histograma.escribir(histo_italiano,"italiano")
abecedario_italiano = [letra for letra in histo_italiano.keys()]
print(histo_italiano)
print(sorted(abecedario_italiano))
print("_______________________________")

diccionario_ingles = diccionario.cargarDic("Libro6")
texto_ingles = diccionario.cargarTex("Libro6")
histo_ingles = histograma.analizar(texto_ingles)
histograma.escribir(histo_ingles,"ingles")
abecedario_ingles = [letra for letra in histo_ingles.keys()]
print(histo_ingles)
print(sorted(abecedario_ingles))
print("_______________________________")


t1= ("""Mn vunuir, pqrppu iuppmvvmu, wy eyn omynnu yn lyiiujr, 
y prvujey eronm mjemwmesm r ernnr iromujm. Ny ouny, mn wrjzir r n'rpzirlmzy ernny vuey puju tmyjvkr; 
csrpz'snzmly r nsjoy r bunzy. Mn lspu r ynnsjoyzu r nr uirvvkmr puju zimyjounyim re rpzirlylrjzr lutmnm. 
Juilynlrjzr wmwr mj vuqqmy, vuj m vsvvmunm, yjvkr pr zynwunzy r quppmtmnr uppriwyijr rprlqnyim punmzyim u mj 
oisqqm em csyzziu u prm yesnzm. Mn lypvkmu lyivkmy mn zriimzuimu mj lueu pmpzrlyzmvu r vulsjmvy vuj m qiuqim 
pmlmnm yzziywripu projynm pujuim, wmpmwm, zyzzmnm r unbyzzmwm. Sjy wunqr qsu imvujupvrir sj ynziu rprlqnyir eynn'ueuir, 
unzir y ervmbiyijr mn iyjou oriyivkmvu r mn nmwrnnu puvmynr. R pmojmbmvyzmwu puzzunmjryir vkr, mj csrpzy pqrvmr, ny vuqqmy zrjer y 
imbuilyipm uojm yjju r vkr mn lypvkmu punmzylrjzr qyizrvmqy yzzmwylrjzr ynny vsiy r ynn'ynnrwylrjzu ernny qiunr, qiuvsiyjeu mn vmtu r 
embrjerjeu m vsvvmunm ey quppmtmnm qireyzuim.""")
palabras_clave1 = ["Mn","pqrppu","omynnu","ernnr","n'rpzirlmzy","lutmnm","wmwr","vuqqmy","vsvvmunm","oisqqm",
"csyzziu","zyzzmnm","nmwrnnu","ynny","ynn'ynnrwylrjzu"]
probados = "ynny,ynn,ernnr,mn"
texto1 = diccionario.limpiar("""Mn vunuir, pqrppu iuppmvvmu, wy eyn omynnu yn lyiiujr, 
y prvujey eronm mjemwmesm r ernnr iromujm. Ny ouny, mn wrjzir r n'rpzirlmzy ernny vuey puju tmyjvkr; 
csrpz'snzmly r nsjoy r bunzy. Mn lspu r ynnsjoyzu r nr uirvvkmr puju zimyjounyim re rpzirlylrjzr lutmnm. 
Juilynlrjzr wmwr mj vuqqmy, vuj m vsvvmunm, yjvkr pr zynwunzy r quppmtmnr uppriwyijr rprlqnyim punmzyim u mj 
oisqqm em csyzziu u prm yesnzm. Mn lypvkmu lyivkmy mn zriimzuimu mj lueu pmpzrlyzmvu r vulsjmvy vuj m qiuqim 
pmlmnm yzziywripu projynm pujuim, wmpmwm, zyzzmnm r unbyzzmwm. Sjy wunqr qsu imvujupvrir sj ynziu rprlqnyir eynn'ueuir, 
unzir y ervmbiyijr mn iyjou oriyivkmvu r mn nmwrnnu puvmynr. R pmojmbmvyzmwu puzzunmjryir vkr, mj csrpzy pqrvmr, ny vuqqmy zrjer y 
imbuilyipm uojm yjju r vkr mn lypvkmu punmzylrjzr qyizrvmqy yzzmwylrjzr ynny vsiy r ynn'ynnrwylrjzu ernny qiunr, qiuvsiyjeu mn vmtu r 
embrjerjeu m vsvvmunm ey quppmtmnm qireyzuim.""")
histo_texto1 = histograma.analizarTexto(texto1)
histograma.escribir(histo_texto1,"texto1")
abecedario_texto1 = [letra for letra in histo_texto1.keys()]
print(histo_texto1)
print(sorted(abecedario_texto1))
print("_______________________________")


t2=("""Xdcswhht, ab cdidllt svw dzwzd gwc xkihktcw dxkst ab idyyt, xd btb abt padhabpaw. Pawfyt idyyt fw bw 
dbndzd fwxgcw kb ikct stb dnntfft ab gdkt nk fykzdhk, gwcskt Xdcswhht h’dzwzd svkdxdyt “Idyyt stb ihk Fykzdhk 
K naw wcdbt scwfskayk dffkwxw, w kh idyyt fk wcd fwxgcw nkxtfycdyt xthyt oacqt w owhksw nk dkaydcw Xdcswhht, 
padbnt wcd kb nkooksthyd. Ab iktcbt gdcywskgdctbt dhhd owfyd nwh gdwfw, ntzw Xdcswhht stbtqqw Fdbncd, hd okihkd 
nwh cksst Fkibtctyyt nwh gtfyt. K naw fk yctzdctbt faqkyt fkxgdyksk, xd Fdbncd ikd fdgwzd svw btb dzcwqqw gtyayt 
ocwpawbydcw Xdcswhht gwcsvw fat gdncw btb h’dzcwqqw gwcxwfft. Kbodyyk, kh gdncw nk Fdbncd btb zthwzd svw hd okihkd 
dzwffw dxksk ycd ihk dqkydbyk nwh gdwfw, nd hak ckywbayk nwk fwxghksktyyk.
""")
palabras_clave2 = ["dzwzd","idyyt","gdwfw","h’dz","Kbodyyk","fw","bw","btb","h’dzcwqqw"]
probadas = []
texto2 = diccionario.limpiar("""Xdcswhht, ab cdidllt svw dzwzd gwc xkihktcw dxkst ab idyyt, xd btb abt padhabpaw. Pawfyt idyyt fw bw 
dbndzd fwxgcw kb ikct stb dnntfft ab gdkt nk fykzdhk, gwcskt Xdcswhht h’dzwzd svkdxdyt “Idyyt stb ihk Fykzdhk K naw wcdbt scwfskayk dffkwxw, 
w kh idyyt fk wcd fwxgcw nkxtfycdyt xthyt oacqt w owhksw nk dkaydcw Xdcswhht, padbnt wcd kb nkooksthyd. Ab iktcbt gdcywskgdctbt dhhd owfyd 
nwh gdwfw, ntzw Xdcswhht stbtqqw Fdbncd, hd okihkd nwh cksst Fkibtctyyt nwh gtfyt. K naw fk yctzdctbt faqkyt fkxgdyksk, xd Fdbncd ikd fdgwzd 
svw btb dzcwqqw gtyayt ocwpawbydcw Xdcswhht gwcsvw fat gdncw btb h’dzcwqqw gwcxwfft. Kbodyyk, kh gdncw nk Fdbncd btb zthwzd svw hd okihkd 
dzwffw dxksk ycd ihk dqkydbyk nwh gdwfw, nd hak ckywbayk nwk fwxghksktyyk.
""")
histo_texto2 = histograma.analizarTexto(texto2)
histograma.escribir(histo_texto2,"texto2")
abecedario_texto2 = [letra for letra in histo_texto2.keys()]
print(histo_texto2)
print(sorted(abecedario_texto2))
print("_______________________________")

histograma.comparar(histo_texto1,histo_espanol)
histograma.comparar(histo_texto1,histo_frances)
histograma.comparar(histo_texto1,histo_italiano)
histograma.comparar(histo_texto1,histo_ingles)
print("_______________________________")

histograma.comparar(histo_texto2,histo_espanol)
histograma.comparar(histo_texto2,histo_frances)
histograma.comparar(histo_texto2,histo_italiano)
histograma.comparar(histo_texto2,histo_ingles)
print("_______________________________")

#histograma.sustituir(histo_texto1,histo_italiano,t1)
diccionario.buscarCoincidencias(t2,diccionario_italiano)