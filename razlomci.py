razlomak = input('Unesite razlomak : ')
k = razlomak.find('/')
brojilac = int(razlomak[0:k])
imenilac = int(razlomak[k+1:])
print(brojilac / imenilac)

