nama = input('Masukan Nama Anda :' )
umur = int(input('Masukan Umur Anda :'))
punya_sim = input('Apakah Anda mempunyai SIM? (Y/T)')
psikotes = input('apakah anda lulus tes psikologi? (Y/T)')

punya_sim = punya_sim.lower()

if punya_sim == 'y' and psikotes == 'Y' :
    sim_a = input('apakah anda mempunyai SIM A (Y/T) ')
    sim_c = input('apakah anada mempunyai SIM C Y/T) ')
    
    if umur >= 17 and sim_a == 'Y' and sim_c == 'Y'   :
        print ("Anda bole Mengendarai Motor dan Mobil bang")
    elif umur >= 17 and sim_a == 'Y'  and sim_c =='T'  :
        print('anda hanya bisa mengendarai mobil bang')
    elif umur >= 17 and sim_a == 'T' and sim_c == 'Y'  :
        print('anda hanya bisa bawa motor bang')
    else :
        print('anda Gabisa bawa kendaraan bang')

elif umur >= 17 and punya_sim == 'T' and psikotes == 'Y' :
    print('Udah gede, psikotes lulus, tapi gapunya SIM, cih bikin sana')
elif umur < 17 and punya_sim == 'T' and psikotes == 'Y' :
    print('tunggu gede dulu cil')
else:
    print('harap masukan inputan yang valid')


