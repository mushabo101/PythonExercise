def nomorHP(nomor) :
    
    if len(a) <= 13 and a[0] == 0 and a[1] == 8:
        print('Nomor HP saya adalah',a)
    elif len(a) <= 13 and a[0] != 0 and a[1 !=8]:
        print('Nomor HP harus dimulai angka "08"')
    else:
        print('Nomor HP hanya maksimal 13 angka')

a = list(input('Masukkan Nomor HP : '))
nomorHP(a)

