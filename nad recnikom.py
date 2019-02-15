#if 14 < 5:
#    print('dddd')
#else:
#    print('sssss')

proizvodi = {'Hleb':50, 'Mleko':100, 'Jogurt':110}
artikal = input('Unesite naziv proizvoda : ')
if artikal in proizvodi:
    print(proizvodi[artikal])
else :
    print('Nema na stanju. ')
    


    



