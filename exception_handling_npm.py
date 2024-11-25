try:
    n = input("Masukkan NPM: ")
    
    genap = 0
    ganjil = 0

    for angka in n:
        if int(angka) % 2 == 0:
            genap += 1
        else:
            ganjil += 1

    print("Jumlah bilangan genap:", genap)
    print("Jumlah bilangan ganjil:", ganjil)
except:
    print("Masukkan angka NPM")