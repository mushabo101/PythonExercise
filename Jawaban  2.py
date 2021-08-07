def nomorHP(nomor) :
    if len(n) > 13:
        print('Nomor HP hanya maksimal 13 Angka')
    elif n[0:2] != '08':
        print('Nomor HP harus dimulai dengan \'08\'')
    else:
        print('Nomor HP Saya Adalah',n)


n = input('Masukkan Nomor HP : ')
nomorHP(n)

