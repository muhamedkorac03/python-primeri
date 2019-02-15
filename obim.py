


def mm_u_cm(mm):
    cm = mm // 10
    mm = mm % 10
    return (cm,mm)

mm = int(input('Unesite broj milimetara " '))
(cm,mm) = mm_u_cm(mm)
print ('broj cm :',cm)
print ('broj mm : ', mm)






                
    
