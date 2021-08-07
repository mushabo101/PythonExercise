num = int(input('Masukkan angka : '))
factorial = 1

if num < 0:
    print('tidak ada factorial ')
elif num == 0:
    print('factorial dari 0 adalah 1')
else:
    for i in range(1,num +1):
        factorial = factorial*i
print('Nilai Faktorial dari',num,'Adalah',factorial)