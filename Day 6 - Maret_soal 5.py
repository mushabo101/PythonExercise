a = int(input('Masukkan Suhu (Dalam Fahrenheit) : '))
b = 5/9*(a-32)
print('Suhu Badan Anda Adalah :',b,'Derajat Celcius')

if b > 36.5 and b < 37.2:
    print('Suhu Badan Normal')
elif b < 36.5:
    print('ANDA HIPOTERMIA, SEGERA BERI PERTOLONGAN PERTAMA')
else:
     print('ANDA HIPERTERMIA, SEGERA LAKUKAN SWAB TEST DAN KARANTINA MANDIRI')

