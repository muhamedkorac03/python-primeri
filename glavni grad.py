glavni_grad = {'Srbija': 'Beograd', 'Crna Gora': 'Podgorica', 'Bosna': 'Sarajevo'}
drzava = input('Unesite naziv drzave: ')
if drzava in glavni_grad:
    print('DA')  
else:
    print('Nije poznat naziv drzave ' + drzava)
