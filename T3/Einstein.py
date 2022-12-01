import itertools
x = ["Rojo","Amarillo","Verde"]
y = ["Mexicano","Coreano","Espanol"]
products = list(itertools.product(x, y,))
#print(products)
i=0
for elemento in products:
    print(f"{elemento} , {products[i+3]}")
    i+=1