#deksripsi variabel biodata
nama = input("Masukkan nama anda: ")
nama_panggilan = input("Masukkan nama panggilan anda: ")
tanggal_lahir = input("Masukkan tanggal lahir anda (dd/mm/yyyy): ")
jenis_kelamin = input("Masukkan jenis kelamin anda (L/P): ")
umur = int(input("Masukkan umur anda: "))
tinggi = float(input("Masukkan tinggi badan anda (dalam cm): "))
berat = float(input("Masukkan berat badan anda (dalam kg): "))
agama = input("Masukkan agama anda: ")
alamat = input("Masukkan alamat anda: ")
nomer_telepon = input("Masukkan nomor telepon anda: ")
alamat_email = input("Masukkan alamat email anda: ")
kewarganegaraan = input("Masukkan kewarganegaraan anda: ")
status_perkawinan = input("Masukkan status perkawinan anda (Y/T): ")
pekerjaan = input("Masukkan pekerjaan anda: ")
pendidikan_terakhir = input("Masukkan pendidikan terakhir anda: ")
program_studi = input("Masukkan program studi anda: ")
bahasa_yang_dikuasai = input("Masukkan bahasa yang dikuasai (pisahkan dengan koma): ")
skill_yang_dimiliki = input("Masukkan skill yang dimiliki (pisahkan dengan koma): ")
hobi = input("Masukkan hobi anda (pisahkan dengan koma): ")
minat = input("Masukkan minat anda (pisahkan dengan koma): ")
cita_cita = input("Masukkan cita-cita anda: ")
motto_hidup = input("Masukkan motto hidup anda: ")


# Mengubah input status perkawinan menjadi boolean

status_perkawinan_input = status_perkawinan.lower()  # Mengubah input menjadi huruf kecil untuk memudahkan perbandingan
if status_perkawinan_input == "y":
    status_perkawinan = True
elif status_perkawinan_input == "t":
    status_perkawinan = False

#menampilkan biodata yang telah diinputkan

print("===============================================================")
print("                        Biodata Anda                           ")
print("===============================================================")

print("Nama: ", nama)   
print("Nama Panggilan: ", nama_panggilan)
print("Tanggal Lahir: ", tanggal_lahir)
print("Jenis Kelamin: ", jenis_kelamin)
print("Umur: ", umur)
print("Tinggi Badan: ", tinggi, "cm")
print("Berat Badan: ", berat, "kg")
print("Agama: ", agama)
print("Alamat: ", alamat)
print("Nomor Telepon: ", nomer_telepon)
print("Alamat Email: ", alamat_email)
print("Kewarganegaraan: ", kewarganegaraan)
print("Status Perkawinan: ", status_perkawinan)
print("Pekerjaan: ", pekerjaan)
print("Pendidikan Terakhir: ", pendidikan_terakhir)
print("Program Studi: ", program_studi)
print("Bahasa yang Dikuasai: ", bahasa_yang_dikuasai)
print("Skill yang Dimiliki: ", skill_yang_dimiliki)
print("Hobi: ", hobi)
print("Minat: ", minat)
print("Cita-cita: ", cita_cita)
print("Motto Hidup: ", motto_hidup)

print("===============================================================")

print("Terima kasih telah mengisi biodata ini. Semoga hari Anda menyenangkan!")


#mengetahui tipe data dari setiap variabel yang telah diinputkan
print("===============================================================")
print("Tipe Data dari Setiap Variabel:")
print("Nama: ", type(nama))
print("Nama Panggilan: ", type(nama_panggilan))
print("Tanggal Lahir: ", type(tanggal_lahir))
print("Jenis Kelamin: ", type(jenis_kelamin))
print("Umur: ", type(umur))
print("Tinggi Badan: ", type(tinggi))
print("Berat Badan: ", type(berat))
print("Agama: ", type(agama))
print("Alamat: ", type(alamat))
print("Nomor Telepon: ", type(nomer_telepon))
print("Alamat Email: ", type(alamat_email))
print("Kewarganegaraan: ", type(kewarganegaraan))
print("Status Perkawinan: ", type(status_perkawinan))
print("Pekerjaan: ", type(pekerjaan))
print("Pendidikan Terakhir: ", type(pendidikan_terakhir))
print("Program Studi: ", type(program_studi))
print("Bahasa yang Dikuasai: ", type(bahasa_yang_dikuasai))
print("Skill yang Dimiliki: ", type(skill_yang_dimiliki))
print("Hobi: ", type(hobi))
print("Minat: ", type(minat))
print("Cita-cita: ", type(cita_cita))
print("Motto Hidup: ", type(motto_hidup))
print("===============================================================")