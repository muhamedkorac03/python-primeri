krenuo_h = int(input('Uneti casove polaska : '))
putovao_h = int(input('Uneti casove putovanja : '))
krenuo_min = int(input('Uneti minute polaska : '))
putovao_min = int(input('Uneti minute putovanja : '))
print('Autobus stize u : ')
print((krenuo_h + putovao_h) + (krenuo_min + putovao_min) // 60 )
print((krenuo_min + putovao_min)  % 60 )







