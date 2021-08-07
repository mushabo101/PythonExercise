bintang = ''
size = 5

for i in range(size*2):
    for j in range(size-i):
        bintang += '* '
    bintang +='\n'
print(bintang)
