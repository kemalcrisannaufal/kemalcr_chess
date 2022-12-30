'''
Nama   : Kemal Crisannaufal
Nim    : 1301213133
Soal   : Catur Hula-Hula (34)
'''

#Deklarasi fungsi baca_data
def baca_data(nama_file):
    #Fungsi untuk membaca file dari file teks menjadi sebuah list berisi setiap karakter string
    f = open(nama_file, 'r')
    file = f.readline().replace('\n', '')
    posisi = list(file)
    f.close()
    return posisi

#Deklarasi fungsi ilustrasi_papan
def ilustrasi_papan(posisi):
    #Fungsi untuk meng-ilustrasikan papan catur berdasarkan data list posisi
    strPosisi = ''.join(posisi)
    data_posisi = strPosisi.split('/')
    baris = 1
    #Perulangan setiap data di dalam data_posisi
    for data in data_posisi:
        #data dipecah perhuruf ke dalam list_data
        list_data = list(data)
        #Percabangan berdasarkan jenis elemen data (alphabet/digit/alphanumeric)
        if data.isalpha(): #Jika data alphabet, maka baris ke-n diisi list_data
            print("Baris", baris, "=", list_data)
        elif data.isdigit(): #Jika data digit, maka baris ke-n diisi list yang berisi '_' sebanyak data (menandakan petak kosong)
            print("Baris", baris, "=", (['_'] * int(data)))
        elif data.isalnum(): #Jika data alphanumeric, maka dilakukan pengecekan kembali data alphabet atau numeric
            listData = [] #Assign list kosong untuk ilustrasi baris ke-n yang datanya alphanumeric
            #Perulangan setiap elemen di list_data
            for elemen in list_data:
                if elemen.isdigit(): #Jika elemen data digit, maka listData diisi list yang berisi '_' sebanyak elemen(menandakan petak kosong)
                    listData.extend(['_'] * int(elemen))
                else: #Jika elemen data alphabet, maka listData diisi elemen
                    listData.append(elemen)
            print("Baris", baris, "=", listData)
        baris += 1

#Deklarasi fungsi nilai_buah
def nilai_buah(posisi, pemain):
    #Fungsi untuk menghitung nilai buah catur salah satu pemain (HITAM/PUTIH) dari data list posisi
    nilai = 0
    #Percabangan berdasarkan jenis pemain
    if pemain == "PUTIH":
        #Menghitung nilai bidak pemain putih 
        #Hitung kemunculan masing-masing bidak dengan fungsi count dan dikalikan dengan nilai bidak tersebut
        K = posisi.count('K') * 200
        Q = posisi.count('Q') * 9
        R = posisi.count('R') * 5
        B = posisi.count('B') * 3
        N = posisi.count('N') * 3
        P = posisi.count('P') * 1
        nilai = K + Q + R + B + N + P
    elif pemain == "HITAM":
        #Menghitung nilai bidak pemain hitam 
        #Hitung kemunculan masing-masing bidak dengan fungsi count dan dikalikan dengan nilai bidak tersebut
        k = posisi.count('k') * 200
        q = posisi.count('q') * 9
        r = posisi.count('r') * 5
        b = posisi.count('b') * 3
        n = posisi.count('n') * 3
        p = posisi.count('p') * 1
        nilai = k + q + r + b + n + p
    return nilai

#Deklarasi fungsi jenis_bidak
def jenis_bidak(posisi, pemain):
    #Fungsi untuk menampilkan jenis_bidak dan jumlahnya dari data list posisi
    #Assign dua buah list yang berisi jenis bidak putih dan hitam
    putih = ['K', 'Q', 'R', 'B', 'N', 'P']
    hitam = ['k', 'q', 'r', 'b', 'n', 'p']
    dict_jb = {} #Assign dictionary kosong
    #Percabangan berdasarkan jenis pemain (PUTIH/HITAM) dan perulangan setiap elemen di dalam list posisi
    if pemain == 'PUTIH':
        for elemen in posisi:
            if elemen.isalpha() and elemen in dict_jb: #Jika elemen alphabet dan elemen sudah ada di dalam dict_jb maka valuenya ditambah 1
                dict_jb[elemen] += 1
            elif elemen.isalpha() and elemen in putih : #Jika elemen alphabet dan elemen ada di list putih dan elemen belum ada di dalam dict_jb 
                dict_jb[elemen] = 1                     #maka valuenya di-assign 1
    elif pemain == 'HITAM':
        for elemen in posisi:
            if elemen.isalpha() and elemen in dict_jb: #Jika elemen alphabet dan elemen sudah ada di dalam dict_jb maka valuenya ditambah 1
                dict_jb[elemen] += 1
            elif elemen.isalpha() and elemen in hitam: #Jika elemen alphabet dan elemen ada di list hitam dan elemen belum ada di dalam dict_jb 
                dict_jb[elemen] = 1                    #maka valuenya di-assign 1
    return dict_jb

#Deklarasi fungsi tampil dictionary
def tampil_dict(dict_jb):
    #Fungsi untuk menampilkan jenis bidak dan nilai bidak dari dictionary
    #Assign simbol_bidak, bidak, dan nilai, yang posisi/indexnya saling bersesuaian
    simbol_bidak = ['K', 'Q', 'R', 'B', 'N', 'P', 'k', 'q', 'r', 'b', 'n', 'p']
    bidak = ['King', 'Queen', 'Rook', 'Bishop', 'Knight', 'Pawn', 'King', 'Queen', 'Rook', 'Bishop', 'Knight', 'Pawn']
    nilai = [200, 9, 5, 3, 3, 1, 200, 9, 5, 3, 3, 1]
    #Lakukan perulangan terhadap dictionary
    for key, value in dict_jb.items():
        #Mencari indeks key dictionary di dalam simbol_bidak, bidak, atau nilai (index bersesuaian)
        idx = simbol_bidak.index(key)
        #Mengganti simbol bidak dengan nama lengkap bidak dan mencari nilai bidak berdasarkan index yang telah dicari
        jenis_bidak = bidak[idx]
        nilai_bidak = nilai[idx]
        print("\tBidak", jenis_bidak, "sebanyak", value, "yang setiap bidak bernilai", nilai_bidak ) #Tampilkan bidak, jenis_bidak, dan nilai_bidak

#Deklarasi fungsi jumlah_petak_kosong
def jumlah_petak_kosong(posisi):
    #Fungsi untuk menghitung banyaknya petak kosong di papan catur berdasarkan data list posisi
    petak_kosong = 64 #Jumlah petak dalam papan catur
    #Iterasi setiap elemen list posisi
    for elemen in posisi:
        if elemen.isalpha(): #Jika elemen alphabet maka petak_kosong dikurangi 1
            petak_kosong -= 1
    return petak_kosong


        











