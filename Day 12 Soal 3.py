def Sort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
arr = list(map(int,input('masukkan angka ').split(' ')))
Sort(arr) 
print('Hasil Shorting : ',arr)
print('Nilai Terbesar Dari Data Adalah : ',arr[1])
print('Nilai Terkecil dari Data Adalah : ',arr[-1])
