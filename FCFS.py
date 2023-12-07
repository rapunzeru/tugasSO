def FCFS(que_req, head):
	seek_count = 0
	distance, req_sekarang = 0, 0

	for i in range(size):
		req_sekarang = que_req[i]
		distance = abs(req_sekarang - head) #hitung jarak antar track dan head (absolute)
		seek_count += distance #tambah total count dengan jarak antar track dan head

		#pemanggilan fungsi untuk melihat perpindahan head
		perpindahan_head(req_sekarang, head)
		head = req_sekarang #pindah head ke track berikutnya

	print(f'seek time: {seek_count} head movement') 
	print(f'average seek time {seek_count} dibagi {size}: {round(seek_count / size, 2)}')

#fungsi untuk perpindahan head
def perpindahan_head(req_sekarang, head):
	if req_sekarang > head:
		arah = 'kanan'
	elif req_sekarang < head:
		arah = 'kiri'
	else:
		arah = 'tidak ada pergerakan'
		
	if arah == 'tidak ada pergerakan':
		print(f'{arah} dari head: {head} menuju track: {req_sekarang}')
	else:
		print(f'bergerak ke{arah} dari head: {head} menuju track: {req_sekarang}')

if __name__ == '__main__':
	que_req = [] #list kosong untuk queue request
	head = int(input('masukkan posisi head: '))
	if head > 199:
		print('head melebihi batas track')
		exit() #fungsi exit adalah fungsi built in python yang akan menghentikan code ketika kondisi tidak terpenuhi
	else:
		banyak = int(input('masukkan jumlah request: '))
		for i in range(banyak):
			que = int(input(f'masukkan queue ke-{i + 1}: '))
			if que > 199:
				print('request melebihi batas track')
				exit()
			else:
				que_req.append(que) #masukkan input user ke list kosong
	size = len(que_req)
	FCFS(que_req, head) #panggil fungsi FCFS

#based code dibuat oleh Rajput-Ji dan dimodifikasi oleh:
#Chika Venesa / 71220838
#Cynthia Angeline / 71220858
#Anjelita Haninuna / 71220925
#Dwiyan Bagus Prakosa / 71220935
