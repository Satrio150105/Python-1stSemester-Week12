   #Luas Lingkaran
def luas_lingkaran():
    Phi = 3.14
    try:
      jari_jari = int(input("Masukkan panjang jari-jari: "))
      print("Luas lingkaran = ", Phi * jari_jari * jari_jari)
    except:
      print("Hanya boleh masukkan angka")

    #Luas Persegi
def luas_persegi():
    try:
      sisi = int(input('Masukkan panjang sisi: '))
      print("Luas persegi = ", sisi * sisi)
    except:
      print("Hanya boleh masukkan angka")

    #Luas Segitiga
def luas_segitiga():
    try:
       alas = int(input('Masukkan panjang alas: '))
       tinggi = int(input('Masukkan panjang tinggi: '))
       print("Luas segitiga = ", (alas * tinggi) / 2)
    except:
      print("Hanya boleh masukkan angka")


def function():
    while True:
        print("\nPilih luas yang ingin dicari:")
        print("1. Lingkaran")
        print("2. Persegi")
        print("3. Segitiga")
        print("4. Keluar")

        n = input("Masukkan pilihan (1/2/3/4): ")

        if n == '1':
            luas_lingkaran()
        elif n == '2':
            luas_persegi()
        elif n == '3':
            luas_segitiga()
        elif n == '4':
            print("Selesai, terima kasih sudah menggunakan kalkulator")
            break
        else:
            print("Pilihan tidak boleh kosong. Silakan pilih angka yang tertera.")

function()