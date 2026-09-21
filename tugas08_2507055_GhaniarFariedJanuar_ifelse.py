
while True :
    garis = "=" * 20

    print(garis)
    print("kalkulator Sederhana")
    print(garis)
    pilihan_aritmatika = input("1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4.Pembagian\n5. Modulus\nMasukan Pilihan Anda: ")
    


    if pilihan_aritmatika == "1" :
        print("Anda Memilih Penjumlahan")
        print(garis)
        angka1 = int(input("Masukan Angka Pertama \t: "))
        angka2 = int(input("Masukan Angka Kedua \t: "))
        angka3 = int(input("Masukan Angka Ketiga \t: "))
        print("\n")
        hasil = angka1 + angka2 + angka3
        print(f"Hasil Dari Ketiga Angka Tersebut adalah : {hasil}")
        print("\n")
        
        ulang =input("Apakah Anda Mau Menghitung lagi (Y/T) :")
        print("\n")
        print(garis)
        if ulang.lower() != "y":
            print("Program Selesai!!!")
            break

    elif pilihan_aritmatika == "2" :
        print("Anda Memilih Pengurangan")
        print(garis)
        angka1 = int(input("Masukan Angka Pertama \t: "))
        angka2 = int(input("Masukan Angka Kedua \t: "))
        angka3 = int(input("Masukan Angka Ketiga \t: "))
        print("\n")
        hasil = angka1 - angka2 - angka3
        print(f"Hasil Dari Ketiga Angka Tersebut adalah : {hasil}")
        print("\n")
        
        ulang =input("Apakah Anda Mau Menghitung lagi (Y/T) :")
        print("\n")
        if ulang.lower() != "y":
                    print("Program Selesai!!!")
                    break

    elif pilihan_aritmatika == "3" :
        print("Anda Memilih Perkalian")
        print(garis)

        angka1 = int(input("Masukan Angka Pertama \t: "))
        angka2 = int(input("Masukan Angka Kedua \t: "))
        angka3 = int(input("Masukan Angka Ketiga \t: "))
        print("\n")
        hasil = angka1 * angka2 * angka3
        print(f"Hasil Dari Ketiga Angka Tersebut adalah : {hasil}")
        print("\n")
        
        ulang =input("Apakah Anda Mau Menghitung lagi (Y/T) :")
        print("\n")
        if ulang.lower() != "y":
                    print("Program Selesai!!!")
                    break

    elif pilihan_aritmatika == "4" :
        print("Anda Memilih Pembagian")
        print(garis)
        
        angka1 = int(input("Masukan Angka Pertama \t: "))
        angka2 = int(input("Masukan Angka Kedua \t: "))
        angka3 = int(input("Masukan Angka Ketiga \t: "))
        print("\n")
        hasil = angka1 / angka2 / angka3
        print(f"Hasil Dari Ketiga Angka Tersebut adalah : {hasil}")
        print("\n")
       
        ulang =input("Apakah Anda Mau Menghitung lagi (Y/T) :")
        print("\n")
        if ulang.lower() != "y":
                    print("Program Selesai!!!")
                    break

    elif pilihan_aritmatika == "5" :
        print("Anda Memilih Modulus")
        print(garis)
        
        angka1 = int(input("Masukan Angka Pertama \t: "))
        angka2 = int(input("Masukan Angka Kedua \t: "))
        angka3 = int(input("Masukan Angka Ketiga \t: "))
        print("\n")
        hasil = angka1 % angka2 % angka3
        print(f"Hasil Dari Ketiga Angka Tersebut adalah : {hasil}")
        print("\n")
        ulang =input("Apakah Anda Mau Menghitung lagi (Y/T) :")
        print("\n")
        if ulang.lower() != "y":
                    print("Program Selesai!!!")
                    break

    else :
        print("Pilihan Anda Tidak Valid")
        print("\n")
        ulang =input("Apakah Anda Mau Mengulang lagi (Y/T) :")

        if ulang.lower() != "y":
                print("Program Selesai!!!")
                break


