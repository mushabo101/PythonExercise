a = int(input('Angka Awal : '))
b = int(input('Angka Akhir : '))

for i in range(a, b+1):
    if i>1 : 
        for j in range(2,i): 
            if(i % j) ==0: 
                break
        else: 
            print(i) 
