#if

# angka = int(input("masukan angka :"))

# if angka > 0 :
#     print("angka yang anda masukan bernilai positif")

# if angka < 0 :
#     print("angka yang anda masukan bernilai negatif")

# if angka == 0 :
#     print("angka yang anda masukan berniali 0")


#if-else

# nilai = int(input("masukan nilai : "))

# if nilai >= 50 :
#     print("anda lulus")
# else :
#     print("anda tidak lulus")


#elif

# nilai = int(input("masukan nilai anda : "))

# if nilai >= 92 :
#     print("Grade A")
# elif nilai >= 76 :
#     print("Grade B")
# elif nilai >= 60 :
#     print("Grade C")
# elif nilai >= 55 :
#     print("Grade D")
# else:
#     print("Grade E")

#dengan operator logika

# umur = int(input("Masukan Umur anda: "))
# punya_sim = input("Apakah anda mempunyai SIM? (y/t)")

# SIM = punya_sim.lower()

# if umur >= 18 and SIM == "y" :
#     print("anda boleh pake motor")

# else:
#     print('anda gabole bawa motor bang')


#nested if 

# username = input('masukan username : ')

# if username == 'ajril ganteng 25':
#     pw = input('masukan pw kamu jril : ')
#     if pw == 'aku suka merpati' :
#         print ('welkom to the jekes')
#     else :
#         print('kamu bukan ajril ya, kamu heker ya')
# else:
#     print('kalo bukan ajril daftar dulu bang')


#macth - case

# hari = input('masukan nama hari : ').lower()

# match hari :
#     case 'senin' | 'selasa' | 'rabu' | 'kamis' | 'jumat' :
#         print('hari kerja')
#     case 'sabtu' | 'minggu' :
#         print('hari libur')
#     case _:
#         print('yang bener bang masukin harinya')

#conditional expression

angka = int(input('masukan angka : '))

hasil = 'positif' if angka > 0 else 'non-positif'

print(f'angka tersebut : {hasil}')







