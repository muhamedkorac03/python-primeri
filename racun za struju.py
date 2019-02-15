potrosnja = int(input('Unesite broj kwh : '))
if potrosnja <= 350:
    cena = potrosnja * 5.1
elif potrosnja <= 1600 :
    cena = (350 * 5.1) + (potrosnja - 350) * 7.7
else :
    cena = (350 * 5.1) + (1249 * 7.7) + (potrosnja - 1600) * 15.3

print(cena)
    
