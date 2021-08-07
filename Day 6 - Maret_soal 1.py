a  = int(input('Masukkan angka : '))

if a % 2 == 0 and a != 0 and a > 0:
    print('Bilangan',a,'tergolong bilangan genap')
elif a % 2 == 1 and a!= 0 and a > 0: 
    print('Bilangan',a,'tergolong bilangan ganjil')
elif a < 1 and a != 0:
    print('Masukkan Bilangan bulat positif')
else :
    print(a,'Bukanlah bilangan ganjil maupun genap')
