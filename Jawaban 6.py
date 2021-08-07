print('ini adalah program untuk menentukan deret selanjutnya dari Aritmetik atau Geometri')
def APGP():
    while True:
        case=list(map(int,input('Masukkan tinga bilangan : ').split()))
        if case[0]==case[1]==case[2]==0:
            break
        else:
            if case[1]-case[0]==case[2]-case[1]:
                N=2*case[2]-case[1]
                print('AP '+str(N))
            else:
                N=case[2]**2/case[1]
                print("GP "+str(N))
APGP()