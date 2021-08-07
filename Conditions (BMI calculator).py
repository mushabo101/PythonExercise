a = int(input('Masukan Massa (kg) :' ))
b = int(input('Masukkan Tingg (cm) :'))

IMT = a/((b/100)**2)

print('Massa',a,'Kg & Tinggi', b/100)
if IMT < 18.5:
    print(IMT,'BERAT BADAN KURANG')
elif IMT >= 18.5 and IMT <= 24.9:
    print(IMT,'BERAT BADAN IDEAL')
elif IMT >= 25 and IMT <= 29.9:
    print(IMT,'BERAT BADAN BERLEBIH')
elif IMT >= 30 and IMT <= 29.9:
    print(IMT,'BERAT BADAN SANGAT BERLEBIH')
else:
    print(IMT,'OBESITAS')