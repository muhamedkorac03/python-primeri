cene_proizvoda = [560, 130, 420, 415.5, 65.99, 78.99, 325.55]
sortirana_lista = sorted(cene_proizvoda)
print(sortirana_lista)
tri_najjeftinija = sortirana_lista[0:3]
tri_najskuplja = sortirana_lista[-3:]
print('Tri najskuplja su : ', tri_najskuplja, ' Tri najjeftinija su: ',tri_najjeftinija)

