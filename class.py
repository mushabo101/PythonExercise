class Siswa:
    def __init__(self,nama,nis,umur):
        self.name = nama
        self.id = nis
        self.age = umur

    def muncul(self):
        print("Nama Siswa ini Adalah "+ self.name +"Nomor Induk Siswanya Yaitu "+ str(self.id) +", Dan Umurnya Adalah "+ str(self.age) +" Tahun")


    
siswa1 = Siswa("Arief", 10001, 21)
siswa2 = Siswa("Aryanda", 10002, 23)
siswa3 = Siswa("Raihan", 10003, 20)
siswa4 = Siswa("Prisilla", 99999, 22)
siswa5 = Siswa("Farhan", 10004, 21)

siswa1.muncul()