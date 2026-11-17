import time

# Catat waktu dimulai
waktu_mulai = time.perf_counter()

# --- KODE YANG INGIN DIUKUR ---
# Contoh: Proses perulangan hingga 10 juta kali
total = 0
for i in range(100_000):
    total += i
    #print(i)
# ---------------------------------

# Catat waktu selesai
waktu_selesai = time.perf_counter()

# Hitung selisih waktu
lama_eksekusi = waktu_selesai - waktu_mulai

print(f"hasil perhitungan: {total}")
print(f"lama waktu eksekusi: {lama_eksekusi:.6f} detik")


