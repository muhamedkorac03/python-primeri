import math

def obim_i_povrsina_kruga(r):
    O = 2 * r * math.pi
    P = r ** 2 * math.pi
    return (O,P)

poluprecnik = int(input('Unesite iznos poluprecnika : '))
(O,P) = obim_i_povrsina_kruga(poluprecnik)
print('Obim kruga je : ', O, ' Povrsina kruga je :',P)


