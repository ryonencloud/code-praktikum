jalur_utama = True
jalur_cadangan = True

#Model Logika
akses_valid = jalur_utama ^ jalur_cadangan

#Output hasil administrasi
if akses_valid:
	print("Akses valid:", akses_valid)
else:
	print("Akses Tidak valid:", akses_valid)
