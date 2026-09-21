nama = input("Masukkan nama anda: ")
nama_panggilan = nama[0:7]
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
link_kampus = "https://student.upi.edu/"
path = "C:\\Users\\ghani\\OneDrive\\Documents\\GitHub\\Latihan-python-001"


biodata = f"Nama \t\t\t: {nama}\nNama Panggilan \t\t: {nama_panggilan}\nTTL \t\t\t: {tanggal_lahir}\nJenis Kelamin \t\t: {jenis_kelamin}\nUmur \t\t\t: {umur*2}\n TB \t\t\t: {tinggi}\nBerat \t\t\t: {berat}\nAgama \t\t\t: {agama}\nAlamat \t\t\t: {alamat}\nNo Telepon \t\t: {nomer_telepon}\nEmail \t\t\t: {alamat_email}\nKewarganegaraan \t: {kewarganegaraan}\nStatus Perkawinan \t: {status_perkawinan}\nPekerjaan \t\t: {pekerjaan}\nPendidikan Terakhir \t: {pendidikan_terakhir}\nProgram Studi \t\t: {program_studi}\nBahasa yang Dikuasai \t: {bahasa_yang_dikuasai.upper()}\nSkill yang Dimiliki \t: {skill_yang_dimiliki.replace("Python","Java")}\nHobi \t\t\t: {hobi}\nMinat \t\t\t: {minat}\nCita-cita \t\t: {cita_cita}\nMotto Hidup \t\t: {motto_hidup}\nLink kampus \t\t: {link_kampus}\nPath \t\t\t: {path}"

print(biodata)