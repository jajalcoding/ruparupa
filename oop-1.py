class Programku:
    keterangan = 'Belajar OOP-class-1'
    def __init__(self, banner, informasi):
        self.banner = banner
        self.informasi = informasi

    def cetakbanner(self):
        print(self.banner)

    def cetakinformasi(self):
        print(self.informasi)

    def jalankan(self):
        self.cetakbanner()
        self.cetakinformasi()

class ProgramKeren(Programku):
    def __init__(self, tugasnya ):
        self.tugasnya = tugasnya
        self.banner= 'Program Keren'

    def cetaktugas(self):
        print(self.tugasnya)

    def jalankan(self):
        self.cetakbanner()
        self.cetaktugas()

a=Programku("cetak ini","ada ini")
b=Programku("cetak itu","ada itu")
c=ProgramKeren('Cari Rumah')

a.jalankan()
b.jalankan()
c.jalankan()


semuatugas=['cari jodoh','cari sekolah','cari mobil']
tugaslist = []

for tugas in semuatugas :
    z = ProgramKeren(tugas)
    print(z)
    tugaslist.append(z)

for tugas in tugaslist :
    tugas.jalankan()
    
print('Selesai')

