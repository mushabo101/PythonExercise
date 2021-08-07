a = int(input('Masukkan jumlah hari : '))

if a > 0:
    tahun = a/360
    hari = a%360
    bulan = hari/30
    hari = a%30
    minggu = hari/7
    hari = a%7
    print(a,'Hari =',int(tahun),'tahun',int(bulan),'bulan',int(minggu),'minggu',hari,'hari')
else:
    print('Masukkan jumlah Hari yang benar')