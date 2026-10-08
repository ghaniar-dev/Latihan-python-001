siswa = {
    "nama": "Alice",
    "umur": 20,
    "kelas": "12A"
}

print("Nama siswa:", siswa["nama"])
siswa["umur"] = 21
del siswa["kelas"]

for key, value in siswa.items():
    print(f"{key} : {value}")