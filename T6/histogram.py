def genHistoByText(textArr):
    histo = {}
    total = 0
    for i in abc:
        histo[i] = 0
    for text in textArr:
        for i in text:
            histo[i] += 1
            total += 1
    for i in abc:
        histo[i] /= total
    return histo

print(genHistoByText(["ijgfhoishaduief", "asjknfdjiashbuidhusa", "sahuhdyuiashdu"]))