import random



reci = ['ameba', 'alhemija', 'amerika', 'angelina', 'anđeo',

        'aorist', 'argument', 'arsenal', 'aceton', 'balerina'

        'božidar', 'bojler', 'vrata', 'gavran', 'eratosten',

        'etiketa', 'jabuka', 'jagoda', 'kaladont', 'kanarinac',

        'kačamak', 'kuća', 'knjiga', 'mama', 'mačka', 'naocare',

        'nar', 'nebo', 'ontario', 'organizam', 'orkestar',

        'ornament', 'prozor', 'računar', 'slika', 'sto', 'stolica',

        'sunce', 'tavan', 'tata', 'televizor', 'telefon', 'tetka',

        'car', 'carina', 'cvet', 'cena', 'ćao']



# provera da li se

def reciSeNadovezuju(rec1, rec2):

  return rec1[-2:] == rec2[0:2]



def racunarIgra(data_rec):

  moguce_reci = [rec for rec in reci if reciSeNadovezuju(data_rec, rec)]

  if moguce_reci == []:

     return ""

  else:

     return random.choice(moguce_reci)



def covekIgra(data_rec):

   rec = input("Unesi reč (unesi prazno, ako ne znaš): ")

   while rec != "" and \
        (not(reciSeNadovezuju(data_rec, rec)) or not(rec in reci)):

      rec = input("Ta reč nije dobra. Unesi reč: ")

   return rec



rec = random.choice(reci)

print("Početna reč je:", rec)

while True:



   rec = covekIgra(rec)

   if rec == "":

      print("Pošto nisi znao reč, računar je pobedio!")

      break

   print("Odabrao si reč", rec, ". Sada igra računar")



   rec = racunarIgra(rec)

   if rec == "":

      print("Računar nije našao reč! Tvoja pobeda!")

      break

   print("Računar je odabrao reč:", rec)
