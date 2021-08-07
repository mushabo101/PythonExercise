def average(data):
    banyakData = 0
    for i in data:
        banyakData += i
    return banyakData/len(data)
    

def variance(data,average):
    banyakData = 0
    for i in data:
        banyakData = (i - average)**2
    return banyakData/(len(data)-1)
    

def stddev(variance):
    return variance**1/2

def inputData():
    n =int(input('masukkan Banyaknya Data : '))
    data =[]
    for i in range(n):
        c = int(input('Data ke - '+str(i+1)+' = '))
        data.append(c)
    average(data)
    variance(data,average)
    stddev(variance)

    print(data)


inputData()