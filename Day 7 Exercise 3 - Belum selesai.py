print('Selamat Datang di Pasar Buah')
print('List Menu :')
print('1. Menampilkan Daftar Buah\n2.Menambah Buah\n3.Menghapus Buah\n4.Membeli Buah\n5.Exit Program')

Buah = [['Apel',20,10000],['Jeruk',15,15000],['Anggur',25,20000]]

a = input('Masukkan angka Menu yang Ingin dijalankan : ')

if int(a) == 1:
    print('Daftar Buah')
    for i in range(len(Buah)):
        print(Buah[i])

elif int(a) ==  2: #BELUM
    print('Daftar Buah') 

elif int(a) ==  3:
    print('Daftar Buah')
    for i in range(len(Buah)):
        print(Buah[i])
    b = input('Masukkan buah yang ingin di Hapus ')
    del Buah[int(b)]
    print(Buah[i])
    
else :
    print('Ga cukup waktu')
