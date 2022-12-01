numeros = []
rang = 4000
for a in range(-rang, rang):
    for b in range(-rang, rang):
        c = 6
        d = a + b + c  # 6
        e = b + c + d
        f = c + d + e  # 11
        g = d + e + f
        h = e + f + g
        i = f + g + h
        j = g + h + i
        k = h + i + j  # 14
        l = i + j + k
        if f == 11 and k == 14:
            numeros.append([a,b])
            print(f"{a}_{b}_{c}_{d}_{e}_{f}_{g}_{h}_{i}_{j}_{k}_{l}")
print(numeros)
