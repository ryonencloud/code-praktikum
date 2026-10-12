kartu_anggota = False
kartu_izin = True

#Model Logika
boleh_masuk = kartu_anggota or kartu_izin

#Output hasil administrasi
if boleh_masuk:
	print("Boleh masuk:", boleh_masuk)
else:
	print("Tidak Boleh masuk:", boleh_masuk)
