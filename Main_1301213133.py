'''
Nama   : Kemal Crisannaufal
Nim    : 1301213133
Soal   : Catur Hula-Hula (34)
'''

import Catur
#Main Program
print("="*25, "CATUR HULA-HULA", "="*25)

print("File teks 1 = CaturHula.txt")
print("File teks 2 = HulaCatur.txt")
#Membaca data posisi
nama_file = input("Nama File = ")
posisi = Catur.baca_data(nama_file)        
print("Data Posisi =", posisi)

#Ilustrasi papan catur
print("="*20, "ILUSTRASI POSISI BIDAK CATUR", "="*20)
Catur.ilustrasi_papan(posisi)

print("="*25, "STATISTIK CATUR", "="*25)
#Menghitung nilai buah pemain
pemain = input("Masukkan Pemain (PUTIH/HITAM) = ")
nilai_buah = Catur.nilai_buah(posisi, pemain)
print("Nilai buah pemain", pemain, "=", nilai_buah)
print("Terdiri dari:")
persebaran_bidak = Catur.jenis_bidak(posisi, pemain)
Catur.tampil_dict(persebaran_bidak)

#Menghitung jumlah petak kosong berdasarkan posisi
petak_kosong = Catur.jumlah_petak_kosong(posisi)
print("\nJumlah petak kosong papan catur  =", petak_kosong, "petak")
print("="*70)

