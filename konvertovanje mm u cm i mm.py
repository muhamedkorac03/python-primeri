


def mm_u_cm(mm):
    cm = mm // 10
    mm = mm % 10
    return (cm,mm)

mm = int(input('Unesite broj milimetara " '))
(cm,mm1) = mm_u_cm(mm)
print ('Ukupno ste uneli :', mm, ' Imate cintimetara :', cm, ' I milimetara:' , mm1 )








                
    
