# # #for loop

for i in range (1):
    print("solidd")

nama = 'Ega'

#  for (variable baru) in (variable yang akan di ambil) 
for huruf in nama:
    print(huruf)


#while loop

angka = 1
while angka <= 203:
    angka += 1
    print(angka)


pw =""
while pw != "123456" :
    pw = input('masukan Password anda: ')
    if pw != '123456' :
        print("password anda salah")
print("pw anda benar")



# # #break dan continue

angka_rahasia = 2

while True :
    tebakan = int(input('masukan  tebakan kamu (1-15): '))

    if tebakan == angka_rahasia:
        print('tebakan kamu benar cuy')
        break
    else :
        print('tebakan mu salah cuy, coba lagi')

for i in range (10):
    if i % 2 == 0:
        continue
    print(i)

# # #for else
kata = input('masukan kata : ')
huruf_dicari = input('masukan huruf yang akan dicari : ')

for huruf in kata:
    if huruf == huruf_dicari:
        print('huruf', huruf_dicari, 'telah ditemukan')
        break
else :
    print(f'huruf {huruf_dicari} tidak ditemukan')

#while else

pw_benar = '1234'
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    pw = input("masukan PW anda : ")
    percobaan += 1

    if pw == pw_benar:
        print('welkom')
        break
    else:
        print(f'PW kamu salah, sisa percobaan: {max_percobaan - percobaan}')
else:
    print('kamu mau bajak ya')

# #nested loop

for i in range (1, 11):
    for j in range (1, 11):
        hasil = i * j 
        print(f'{i} x {j} = {hasil}')
    print('-------')

for baris in range(1, 3):
    for kolom in range(1, 3):
        print(f"[{baris},{kolom}]", end=" ")
    print()


for i in range(1, 6):
    if i == 2:
        continue  # Lewatin angka 2
    if i == 4:
        break     # Stop total di angka 4
    print(f"Angka: {i}")