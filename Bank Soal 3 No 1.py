def kalimat(kata) :
    
    if len(a) != 0 and len(a) < 200:
        print('*'+a.replace(' ','').upper()+'*')
    elif len(a) > 200:
        print('Batas Karakter Maksimal Hanya 200 ')
    else :
        input('Masukkan Sebuah Inputan')

a = input('Masukan Sebuah Kalimat : ')
kalimat(a)
    