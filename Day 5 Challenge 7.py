angka = [] 
x = int(input('jumlah bilangan 3'))
for i in range(x):
    b = int(input('masukkan angka '))
    angka.append(b)


ans = [] 
for j in angka: 
    sum = 0
    for k in str(j): 
        sum += int(k) 
    ans.append(sum) 

for k in range(len(ans)):
    print('jawaban',ans[k])
