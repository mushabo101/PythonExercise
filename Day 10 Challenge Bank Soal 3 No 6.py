print('ini adalah program untuk menentukan deret selanjutnya dari Aritmetik atau Geometri')
b = 1
while b > 0:
    a = input('masukkan deret angka = ').split(' ')
    for i in range(len(a)):
        a[i] = float(a[i])
        
    if len(a) < 2:
        print('masukkan minimal 3 angka')
    elif a[1] - a[0] == a[2] - a[1]:
        hasilAritmetik = a[0] + (len(a))*(a[1] - a[0])
        print('AP', hasilAritmetik)
    elif a[0] > 0 and a[1]/a[0] == a[2]/a[1]:
        ratio = a[1]/a[0]
        deretGeometri = a[0]*ratio**len(a)
        print('GP',deretGeometri)
    elif a[1] - a[0] != a[2] - a[1] or a[1]/a[0] == a[2]/a[1] :
        print('bukan deret aritmetik atau deret geometri')
    elif a[1] == 0:
        break
    
        
    

 



