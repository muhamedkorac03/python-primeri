def godina_je_prestupna(g):
    if (g % 4 == 0 and g % 100 != 0) or (g % 400 == 0):
        return True
    else :
        return False

godine = int(input('Unesite broj godina'))

if godina_je_prestupna(godine):
    print('prestupna')
else:
    print('nije prestupna')

    
 

    
