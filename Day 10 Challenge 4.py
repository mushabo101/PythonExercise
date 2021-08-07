a = int(input('Input Angka Yang Hendak Dibalik : '))
print('Angka Asli',a)
balik = 0
while a >0:
    b = a %10
    balik =(balik*10) + b
    a = a//10
print('Angka Setelah dibalik',balik)