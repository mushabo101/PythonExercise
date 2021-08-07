a = int(input('berapa bilangan : '))
for i in range(1,a+1):
    b = int(input('cek prima : '))
    if b>1 : 
        for j in range(2,b): 
            if(b % j) ==0: 
                print("NO")
                break
        else: 
            print("YES") 
