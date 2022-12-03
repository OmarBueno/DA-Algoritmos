import histograma,diccionario


diccionario_espanol = diccionario.cargar("Libro1","Español")
histo_espanol = histograma.analizar(diccionario_espanol)
histograma.escribir(histo_espanol,"español")
abecedario_espanol = [letra for letra in histo_espanol.keys()]
print(histo_espanol)
print(sorted(abecedario_espanol))
print("_______________________________")

diccionario_frances = diccionario.cargar("Libro2","Frances")
histo_frances = histograma.analizar(diccionario_frances)
histograma.escribir(histo_frances,"frances")
abecedario_frances = [letra for letra in histo_frances.keys()]
print(histo_frances)
print(sorted(abecedario_frances))
print("_______________________________")

diccionario_italiano = diccionario.cargar("Libro4","Italiano")
histo_italiano = histograma.analizar(diccionario_italiano)
histograma.escribir(histo_italiano,"italiano")
abecedario_italiano = [letra for letra in histo_italiano.keys()]
print(histo_italiano)
print(sorted(abecedario_italiano))
print("_______________________________")

diccionario_ingles = diccionario.cargar("Libro5","Ingles")
histo_ingles = histograma.analizar(diccionario_ingles)
histograma.escribir(histo_ingles,"ingles")
abecedario_ingles = [letra for letra in histo_ingles.keys()]
print(histo_ingles)
print(sorted(abecedario_ingles))
print("_______________________________")

texto1 = diccionario.limpiar("""Mn vunuir, pqrppu iuppmvvmu, wy eyn omynnu yn lyiiujr, 
y prvujey eronm mjemwmesm r ernnr iromujm. Ny ouny, mn wrjzir r n'rpzirlmzy ernny vuey puju tmyjvkr; 
csrpz'snzmly r nsjoy r bunzy. Mn lspu r ynnsjoyzu r nr uirvvkmr puju zimyjounyim re rpzirlylrjzr lutmnm. 
Juilynlrjzr wmwr mj vuqqmy, vuj m vsvvmunm, yjvkr pr zynwunzy r quppmtmnr uppriwyijr rprlqnyim punmzyim u mj 
oisqqm em csyzziu u prm yesnzm. Mn lypvkmu lyivkmy mn zriimzuimu mj lueu pmpzrlyzmvu r vulsjmvy vuj m qiuqim 
pmlmnm yzziywripu projynm pujuim, wmpmwm, zyzzmnm r unbyzzmwm. Sjy wunqr qsu imvujupvrir sj ynziu rprlqnyir eynn'ueuir, 
unzir y ervmbiyijr mn iyjou oriyivkmvu r mn nmwrnnu puvmynr. R pmojmbmvyzmwu puzzunmjryir vkr, mj csrpzy pqrvmr, ny vuqqmy zrjer y 
imbuilyipm uojm yjju r vkr mn lypvkmu punmzylrjzr qyizrvmqy yzzmwylrjzr ynny vsiy r ynn'ynnrwylrjzu ernny qiunr, qiuvsiyjeu mn vmtu r 
embrjerjeu m vsvvmunm ey quppmtmnm qireyzuim.""")
histo_texto1 = histograma.analizar(texto1)
abecedario_texto1 = [letra for letra in histo_texto1.keys()]
print(histo_texto1)
print(sorted(abecedario_texto1))
print("_______________________________")

texto2 = diccionario.limpiar(""" Xdcswhht, ab cdidllt svw dzwzd gwc xkihktcw dxkst ab idyyt, xd btb abt padhabpaw. Pawfyt idyyt fw bw 
dbndzd fwxgcw kb ikct stb dnntfft ab gdkt nk fykzdhk, gwcskt Xdcswhht h’dzwzd svkdxdyt “Idyyt stb ihk Fykzdhk K naw wcdbt scwfskayk dffkwxw, 
w kh idyyt fk wcd fwxgcw nkxtfycdyt xthyt oacqt w owhksw nk dkaydcw Xdcswhht, padbnt wcd kb nkooksthyd. Ab iktcbt gdcywskgdctbt dhhd owfyd 
nwh gdwfw, ntzw Xdcswhht stbtqqw Fdbncd, hd okihkd nwh cksst Fkibtctyyt nwh gtfyt. K naw fk yctzdctbt faqkyt fkxgdyksk, xd Fdbncd ikd fdgwzd 
svw btb dzcwqqw gtyayt ocwpawbydcw Xdcswhht gwcsvw fat gdncw btb h’dzcwqqw gwcxwfft. Kbodyyk, kh gdncw nk Fdbncd btb zthwzd svw hd okihkd 
dzwffw dxksk ycd ihk dqkydbyk nwh gdwfw, nd hak ckywbayk nwk fwxghksktyyk.
""")
histo_texto2 = histograma.analizar(texto2)
abecedario_texto2 = [letra for letra in histo_texto2.keys()]
print(histo_texto2)
print(sorted(abecedario_texto2))
print("_______________________________")