# NAMA : Intan sari b
# NIM : D0221071
# KELAS : INFORMATIKA E

class Kubus():
    def __init__(self, sisi):
        self.sisi = sisi

    def volume (self):
        volume_kubus = self.sisi**3
        print("volume kubus adalah : " , volume_kubus)

    def luas (self):
        luas_kubus = 6 * self.sisi**2
        print("luas kubus adalah : " , luas_kubus)

class Balok():
    def __init__(self,panjang,lebar,tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume (self):
        volume_balok = self.panjang * self.lebar * self.tinggi
        print("volume balok adalah : " , volume_balok)

    def luas (self):
        luas_balok = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang)
        print("luas balok adalah : ", luas_balok)

class Tabung():
    def __init__(self, jari, tinggi):
        self.jari = jari
        self.tinggi = tinggi

    def volume (self):
        volume_tabung = 22/7 * self.jari**2 * self.tinggi
        print("volume tabung adalah : " , round(volume_tabung,2))

    def luas (self):
        luas_tabung = 2 * 22/7 * self.jari * self.tinggi + 2 * 22/7 * self.jari**2
        print("luas tabung adalah : ", round(luas_tabung,2))

class LimasSegitiga():
    def __init__(self, alas, tinggiA, tinggi):
        self.alas = alas
        self.tinggiA = tinggiA
        self.tinggi = tinggi

    def volume (self):
        volume_limasSegitiga = 1/3 * 1/2 * self.alas * self.tinggiA * self.tinggi
        print("volume limas segitiga adalah : " , round(volume_limasSegitiga,2))

    def luas (self):
        luas_limasSegitiga = 1/2 * self.alas * self.tinggiA + ( 3 * 1/2 * self.alas * self.tinggiA)
        print("luas limas segitiga adalah : ", round(luas_limasSegitiga,2))
        
class bola():
    def __init__(self, jari):
        self.jari = jari
    def luas_permukaan(self):
        luas_permukaan = 4 * 22/7 * self.jari**2
        print("luas_permukaan bola adalah : ", round(luas_permukaan,2))
    def volume(self):
        volume = 4/3 * 22/7 * self.jari**2
        print("volume bola adalah : ", round(volume,2))
        
        pass
    
class Lingkaran():
    def __init__(self, jari ):
        self.jari = jari
    def luas (self):
        luas = 22/7 * self.jari**2
        print("luas Lingkaran adalah : ", round(luas,2))
    def volume (self):
        volume = 22/7 * self.jari**2
        print("volume lingkaran adalah : ", round(volume,2))        
        
        

while True:
    print()
    print("""plihan menu
        1. Balok, 
        2. Kubus, 
        3. Tabung, 
        4. Limas Segitiga,
        5. bola 
        6. Lingkaran, 
        7. Berhenti""")
    menu = input("Masukkan pilihan anda : ")

    if menu == '1':
        p = float(input("masukkan panjang: "))
        l = float(input("masukkan lebar: "))
        t = float(input("masukkan tinggi: "))
        balok = Balok(p,l,t)
        print()
        balok.volume()
        balok.luas()
    elif menu == '2':
        s = float(input("Masukkan Sisi: "))
        kubus = Kubus (s)
        print()
        kubus.volume()
        kubus.luas()
    elif menu == '3':
        j = float(input("masukkan jari: "))
        t = float(input("masukkan tinggi: "))
        tabung = Tabung (j,t)
        print()
        tabung.volume()
        tabung.luas()
    elif menu == '4':
        a = float(input("masukkan alas: "))
        tA = float(input("masukkan tinggi alas: "))
        t = float(input("masukkan tinggi: "))
        limasSegitiga = LimasSegitiga (a,tA,t)
        print()
        limasSegitiga.volume()
        limasSegitiga.luas()
        
    elif menu == '5':
        j = float(input("masukan jari : "))
        bola = bola (j)
        print()
        bola.luas_permukaan()
        bola.volume()
        
    elif menu == '6':
        j = float(input("masukan jari: "))
        Lingkaran = Lingkaran(j)
        print()
        Lingkaran.luas()
        Lingkaran.volume()
        
    elif menu == '7':
        break
        
    
    else :
        print("pilihan ini kosong")
        
