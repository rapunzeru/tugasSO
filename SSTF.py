def sstf(req, head):
    req_urut = []
    total = 0
    while len(req) > 0:
        #menghitung semua jarak request dari head
        jarak = []
        for i in req:
            jarak.append((i, abs(i - head))) 
        jarak_urut = sorted(jarak, key=elemen) #urutkan jarak berdasarkan selisih head dengan track lainnya
        req_terdekat, _ = jarak_urut[0] #mengambil elemen pertama pada tuple

        seek_time = abs(req_terdekat - head)
        total += seek_time
        
        #pemanggilan fungsi untuk memperlihatkan kemana arah head 
        perpindahan_head(req_terdekat, head)

        head = req_terdekat
        #mengupdate request sesuai dengan jarak terdekat ke terjauh
        req_urut.append(req_terdekat)
        req.remove(req_terdekat)
    hasil_req_urut = ', '.join(map(str, req_urut)) #ubah tipe data pada req_urut dari list menjadi string dengan pemisah koma
    print(f'request yang telah diurutkan: {hasil_req_urut}')
    print(f'total seek time: {total} head movement')
    print(f'average seek time {total} dibagi {len(req_urut)}: {round(total / len(req_urut), 2)}')

#karena jarak merupakan tuple maka kita ambil elemen kedua dari tuple tersebut
def elemen(jarak):
    return jarak[1]

#fungsi kemana arah head berjalan
def perpindahan_head(req_terdekat, head):
    if req_terdekat > head:
        arah = 'kanan'
    elif req_terdekat < head:
        arah = 'kiri'
    else:
        arah = 'tidak ada perpindahan'
        
    if arah == 'tidak ada perpindahan':
        print(f'{arah} dari head: {head} menuju track: {req_terdekat}')
    else:
        print(f'bergerak ke{arah} dari head: {head} menuju track: {(req_terdekat)}')    

if __name__ == '__main__':
    req = []
    head = int(input('masukkan posisi head: '))
    #percabangan apabila input melebihi 199 maka itu diluar kapasitas track
    if head > 199:
        print('melebihi kapasitas track')
        exit() #fungsi exit adalaah fungsi built in python yang akan menghentikan code ketika kondisi tidak terpenuhi
    else:
        jumlah = int(input('masukkan jumlah request: '))
        for i in range(jumlah):
            que = int(input(f'masukkan queue ke-{i + 1}: '))
            #percabangan apabila input melebihi 199 maka itu diluar kapasitas track
            if que > 199:
                print('melebihi kapasitas track')
                exit()
            else:
                req.append(que)

    sstf(req, head)


#based code dari website geeksforgeeks dimodifikasi oleh
#Chika Venesa / 71220838
#Cynthia Angeline / 71220858
#Anjelita Haninuna / 71220925
#Dwiyan Bagus Prakosa / 71220935
