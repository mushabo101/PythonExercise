c = int(input('Masukan Jumlah Apel :'))
d = int(input('Masukan Jumlah Jeruk :'))
e = int(input('Masukan Jumlah Anggur :'))

print('Detail Belanja')
print('Apel :', c,'x','=',c*10000)
print('Jeruk :', d,'x','=',d*15000)
print('Anggur :', e,'x','=',e*20000)
total = c*10000 + d*15000 + e*20000
print('Total',total)

uang = int(input('Masukan Jumah uang :'))

if uang < total:
    print('Transaksi anda Dibatalkan')
    print('Uangnya kurang sebesar', abs(uang - total))
elif uang == total:
    print('Terima Kasih')
else:
    print('Terika Kasih')
    print('Uang Kembalian', uang-total)
