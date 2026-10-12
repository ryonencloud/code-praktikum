bayar_tunai = True
bayar_transfer = False

#Model Logika
transaksi_valid = bayar_tunai ^ bayar_transfer

#Output hasil administrasi
if transaksi_valid:
	print("Transaksi valid:", transaksi_valid)
else:
	print("Transaksi Tidak valid:", transaksi_valid)
