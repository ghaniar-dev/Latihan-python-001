def buat_profil(nama, umur, kota="Jakarta"):
    print(f"Nama: {nama} | Umur: {umur} | Kota: {kota}")

buat_profil("Alice", 25)
buat_profil(kota="Bandung", nama="Bob", umur=30)

def cetak_data(*angka, **info):
    print("Total angka (*args):", sum(angka))
    for k, v in info.items():
        print(f"{k}: {v}")

cetak_data(10, 20, 30, nama="Charlie", peran="Admin")