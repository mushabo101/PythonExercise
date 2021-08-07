print('masukkan angka 1, untuk menghitung luas segitiga')
print('masukkan angka 2, untuk menghitung luas persegi')

a = int(input('Pilihan Menu yang Diinginkan : '))

if a == 1:
    b = float(input('Masukkan tinggi Segitiga : '))
    c = float(input('Masukkan Alas segitiga : '))
    d = 0.5*a*b
    print('Luas segitiga tersebut adalah', d)
elif a == 2: 
    e = float(input('Masukkan Sisi dari Persegi: '))
    f = e*e
    print('Luas persegi tersebuh adalah', f)
else:
    print('Masukkan input yang benar')


    

