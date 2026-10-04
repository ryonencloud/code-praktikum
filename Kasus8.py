bayar_tunai = False
bayar_transfer = True

#Model Logika
pembayaran_valid = bayar_tunai ^ bayar_transfer

#Output hasil administrasi
if pembayaran_valid:
    print("metode pembayaran retribusi DITERIMA")
else:
    print("metode pembayaran INVALID (terjadi ganda atau belum memilih)")