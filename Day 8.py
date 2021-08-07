def steponNumber(list_awal):
  jawaban = [] # menampung hasil akhir

  for i in range(len(list_awal)):
    x, y = list_awal[i][0], list_awal[i][1] # ambil nilai x dan y

   

    if x == y: # jika kasus pola angka sama
        total = 0
        for i in range(0, x): # mulai dari 0 sampai x ikut pola pada gambar
          total += addition
          # jika sekarang ditambah 1, next ditambah 3
          # jika sekarang ditambah 3, next ditambah 1 
          addition = 1 if addition == 3 else 3 
    elif x-2 == y: # jika kasus pola angka selisih 2
        total = 2
    for i in range(2, x): # mulai dari 2 sampai x ikut pola pada gambar
          total += addition
          # jika sekarang ditambah 1, next ditambah 3
          # jika sekarang ditambah 3, next ditambah 1 
          addition = 1 if addition == 3 else 3 
      
    jawaban.append(total)

    return jawaban

# pola angka sama: +1, +3, +1, +3, +1, ...
# 0,0 = 0
# 1,1 = 1
# 2,2 = 4
# 3,3 = 5
# 4,4 = 8
# 5,5 = 9

# pola angka selisih 2: +1, +3, +1, +3, +1, ...
# 2,0 = 2
# 3,1 = 3
# 4,2 = 6
# 5,3 = 7
# 6,4 = 10

list_awal = [[4,2],[6,6],[3,4]]
print(steponNumber(list_awal))