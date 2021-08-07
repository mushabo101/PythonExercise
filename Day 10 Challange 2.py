import random
a = int(input('Masukan Jumlah Angka Maksimal : '))
b = int(input('Masukan Jumlah Angka Pembagi : '))

angka= random.sample(range(1,a+1),13)
print(angka)
hasil = []
for i in angka:
    if i % b == 0:
        hasil.append(i)
print(*hasil, sep='\n')
    