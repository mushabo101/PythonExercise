number = list(map(int,input().split(',')))

def ganjil(number):
    if number % 2 == 1:
        return 'odd'
    else:
        return 'even'

print(list(map(ganjil,number)))