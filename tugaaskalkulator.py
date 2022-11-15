print("Nama :MOH. SAHAL ASSAHARI")
print("Kelas : TI22J")
print("Nim : 20220040272")

def Main_Menu():
    print("=======================")
    print("Program Kalkulator")
    print("=======================")
    print("1.Ruang Datar")
    print("2.Ruang Bangun")
    
def Menu_Ruang_Datar():
    print("=======================")
    print("Ruang Datar")
    print("=======================")
    print("1.Persegi")
    print("2.Persegi Panjang")
    print("3.Jajar Genjang")
    print("4.Segitiga")
    print("5.Belah Ketumpat")
    print("6.Layang-Layang")
    print("7.Trapesium")
    print("8.Lingkaran")
    
    #Daftar Ruang Datar
    
def Persegi():
    print("=======================")
    print("Luas & keliling Persegi")
    print("=======================")
    s = float(input('Masukan Sisi'))
    print("\n Luas")
    Luas = 4*s
    print('Hasil dari Luas', round(Luas,2))
    print("\nKeliling")
    Keliling = s*s
    print("Hasil dari keliling ',round(Keliling,2")
    
def Persegi_Panjang():
    print("=======================")
    print("Luas & keliling Persegi panjang")
    print("=======================")
    p = float(input("Masukan Panjang"))
    l = float(input("Masukan Luas"))
    print("\nLuas")
    luas = p * l
    print('Hasil Dari Luas', round(luas,2))
    print("\nKeliling")
    keliling = 2*(p + l)
    print('Hasil Dari Keliling ', round (keliling))
    
def Jajar_Genjang():
    print("==================")
    print("Luas & Keliling Jajar Genjang")
    print("==================")
    panjang = int(input("Panjang : "))
    lebar = int(input("Lebar : "))
    tinggi = int(input("Tinggi : "))

    print('\nLuas')
    luas = lebar*tinggi
    print('Hasil Dari Luas ', round(luas,2))
    print("\nKeliling")
    keliling = (2*panjang) + (2*lebar)
    print('Hasil Dari Keliling ', round(keliling,2))
    
def Segitiga():
    print("==================")
    print("Luas & Keliling Segitiga")
    print("==================")
    a = float(input("Masukkan Alas : "))
    t = float(input("Masukkan Tinggi : "))
    l = float(input("Masukkan Lebar : "))
    print("\nLuas")
    luas = a + l + t
    print('Hasil Dari Luas ', round(luas,2))
    print("\nKeliling")
    keliling = 0.5 * a * t
    print('Hasil Dari Keliling ', round(keliling,2))
    
def Belah_Ketupat():
    print("==================")
    print("Luas & Keliling Belah Ketupat")
    print("==================")
    s = float(input("Masukkan Sisi : "))
    d1 = float(input("Masukkan Diagonal 1 : "))
    d2 = float(input("Masukkan Diagonal 2 : "))
    print("\nLuas")
    luas = 0.5 * (d1 * 2) * (d2 * 2)
    print('Hasil Dari Luas ', round(luas,2))
    print("\nKeliling")
    keliling = 4 * s
    print('Hasil Dari Keliling ', round(keliling,2))
    
def Layang_Layang():
    print("==================")
    print("Luas & Keliling Layang-Layang")
    print("==================")
    s = float(input("Masukkan Sisi  : "))
    d1 = float(input("Masukkan Diagonal 1 : "))
    d2 = float(input("Masukkan Diagonal 2 : "))
    print("\nLuas")
    luas = 0.5 * (d1 * d2)
    print('Hasil Dari Luas ', round(luas,2))
    print("\nKeliling")
    keliling = 4 * s
    print('Hasil Dari Keliling ', round(keliling,2))
    
def Trapesium():
    print("==================")
    print("Luas & Keliling Trapesium")
    print("==================")
    t = float(input("Masukkan Tinggi : "))
    s1 = float(input("Masukkan Sisi 1 : "))
    s2 = float(input("Masukkan Sisi 2 : "))
    s3 = float(input("Masukkan Sisi 3 : "))
    print("\nLuas")
    luas = (s1+s2) * t / 2
    print('Hasil Dari Luas ', round(luas,2))
    print("\nKeliling")
    keliling = s1 + s2 + s3 + t
    print('Hasil Dari Keliling ', round(keliling,2))
    
def Lingkaran():
    print("==================")
    print("Luas & Keliling Lingkaran")
    print("==================")
    r = float(input("Masukkan Jari-jari : "))
    d = float(input("Masukkan Diameter : "))
    print("\nLuas")
    luas = 3.14 * r**2
    print('Hasil Dari Luas ', round(luas,2))
    print("\nKeliling")
    keliling = 3.14 * d
    print('Hasil Dari Keliling ', round(keliling,2))
    
#Menu Ruang Bangun

def Menu_Ruang_Bangun():
    print("==================")
    print("Ruang Bangun")
    print("==================")
    print("1. Kubus")
    print("2. Balok")
    print("3. Prisma Segitiga")
    print("4. Limas Segiempat")
    print("5. Limas Segitiga")
    print("6. Tabung")
    print("7. Kerucut")
    print("8. Bola")
    
#Daftar Ruang Bangun

def Kubus():
    print("==================")
    print("Luas & Volume Kubus")
    print("==================")
    s = float(input("Masukkan Sisi : "))
    print("\nLuas")
    luas = 6 * s * s
    print('Hasil Dari Luas ', round(luas,2))
    print("\nVolume")
    Volume = s**3
    print('Hasil Dari Volume ', round(Volume,2))
    
def Balok():
    print("==================")
    print("Luas & Volume Balok")
    print("==================")
    p = float(input("Masukkan Panjang : "))
    l = float(input("Masukkan Lebar : "))
    t = float(input("Masukkan Tinggi : "))
    print("\nLuas")
    luas =  2 * ((p * l) + (p * t) + (l * t))
    print('Hasil Dari Luas ', round(luas,2))
    print("\nVolume")
    Volume = p * l * t
    print('Hasil Dari Volume ', round(Volume,2))
    
def Prisma_SegiTiga():
    print("==================")
    print("Luas & Volume Prisma Segitiga")
    print("==================")
    s1 = float(input("Masukkan Sisi Alas : "))
    s2 = float(input("Masukkan Sisi Alas : "))
    s3 = float(input("Masukkan Sisi Alas : "))
    tPrisma = float(input("Masukkan Tinggi Prisma : "))
    print("\nLuas")
    luas = ( (s1 * s2) / 2 ) * tPrisma
    print('Hasil Dari Luas ', round(luas,2))
    print("\nVolume")
    Volume = (2 * (s1 * s2) / 2) + ((s1 + s2 + s3) * tPrisma)
    print('Hasil Dari Volume ', round(Volume,2))
    
def Limas_SegiEmpat():
    print("==================")
    print("Luas & Volume Limas Segiempat")
    print("==================")
    luas_alas = float(input("Masukkan Luas Alas: "))
    tinggi = float(input("Masukkan Tinggi Limas: "))
    sisi = float(input("Masukkan Sisi Limas: "))
    jumlah_sisi_tegak = float(input("Masukkan Jumlah Sisi Tegak: "))
    print("\nLuas")
    luas = luas_alas + jumlah_sisi_tegak
    print('Hasil Dari Luas ', round(luas,2))
    print("\nVolume")
    Volume = 1/3 * luas_alas * tinggi * sisi
    print('Hasil Dari Volume ', round(Volume,2))
    
def Limas_SegiTiga():
    print("==================")
    print("Luas & Volume Limas Segitiga")
    print("==================")
    As = float(input('Masukkan Alas Segitiga : '))
    Ts = float(input('Masukkan tinggi Segitiga : '))
    t = float(input('Masukkan tinggi Limas : '))
    Ps = float(input('Masukkan Panjang Sisi : '))
    La = 0.5 * As *Ts
    Lt = La * (math.Sqrt(Ts - (Ps/2)))
    Lst = (As * Lt) / 2
    print("\nLuas")
    luas = La + (3 * Lst)
    print('Hasil Dari Luas ', round(luas,2))
    print("\nVolume")
    Volume = (1/3) * La * t
    print('Hasil Dari Volume ', round(Volume,2))
    
def Tabung():
    print("==================")
    print("Luas & Volume Tabung")
    print("==================")
    r = float(input('Masukkan Jari-jari : '))
    t = float(input('Masukkan Tinggi : '))
    print("\nLuas")
    luas = 2 * 3.14 * r * (r + t)
    print('Hasil Dari Luas ', round(luas,2))
    print("\nVolume")
    Volume = 3.14 * r * r * t
    print('Hasil Dari Volume ', round(Volume,2))
    
def Kerucut():
    print("==================")
    print("Luas & Volume Kerucut")
    print("==================")
    r = float(input('Masukkan Jari-jari : '))
    t = float(input('Masukkan Tinggi : '))
    s = float(input('Masukkan Garis Pelukis : '))
    print("\nLuas")
    L1 = 3.14 * r * s
    L2 = 3.14 * r * r
    luas = L1 + L2
    print('Hasil Dari Luas ', round(luas,2))
    print("\nVolume")
    Volume = (1/3) * 3.14 * r * r * t
    print('Hasil Dari Volume ', round(Volume,2))
    
def Bola():
    print("==================")
    print("Luas & Volume Bola")
    print("==================")
    r = float(input("Masukkan Jari-jari : "))
    print("\nLuas")
    luas = 4 * 3.14 * r * r
    print('Hasil Dari Luas ', round(luas,2))
    print("\nVolume")
    Volume = (4/3) * 3.14 * r ** 3
    print('Hasil Dari Volume ', round(Volume,2))
    
while True :
    Main_Menu()
    inputUser = input('Masukkan pilihan anda : ')
    if inputUser == '1' :
        Menu_Ruang_Datar()
        inputPilihan = input('Masukkan pilihan anda : ')
        if inputPilihan == '1':
            Persegi() 
        elif inputPilihan == '2':
            Persegi_Panjang()  
        elif inputPilihan == '3':
            Jajar_Genjang() 
        elif inputPilihan == '4':
            Segitiga()   
        elif inputPilihan == '5':
            Belah_Ketupat()     
        elif inputPilihan == '6':
            Layang_Layang()
        elif inputPilihan == '7':
            Trapesium()
        elif inputPilihan == '8':
            Lingkaran()
        inputUlang = input('Apakah Ingin Mengulang [Y/N]: ')
        if inputUlang == 'n' or inputUlang == 'N':
            print('Terima Kasih Telah Menggunakan Aplikasi ini!')
            break
    elif inputUser == '2' :
        Menu_Ruang_Bangun()
        inputPilihan = input('Masukkan pilihan anda : ')
        if inputPilihan == '1':
            Kubus()
        elif inputPilihan == '2':
            Balok()
        elif inputPilihan == '3':
            Prisma_SegiTiga()
        elif inputPilihan == '4':
            Limas_SegiEmpat()
        elif inputPilihan == '5':
            Limas_SegiTiga()
        elif inputPilihan == '6':
            Tabung()
        elif inputPilihan == '7':
            Kerucut()
        elif inputPilihan == '8':
            Bola()
        inputUlang = input('Apakah Ingin Mengulang [Y/N]: ')
        if inputUlang == 'n' or inputUlang == 'N':
            print('Terimakasih Telah Menggunakan Aplikasi ini!')
            break
    else: 
        print('\ninput yang anda berikan salah!')