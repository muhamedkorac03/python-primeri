def izracunavanje_vremena(s):
    min = (s // 60) % 60
    h = (s // 60) // 60 % 24
    sec = s - h * 3600 - min * 60 
    return h, min, sec

ukupno_sekundi = int(input('Unesite ukupan broj sekundi :  '))
h, min, sec = izracunavanje_vremena(ukupno_sekundi)
print('Casova : ', h, ' Minuta : ', min, ' Sekundi: ', sec)


