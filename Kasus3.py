ipk = False
aktif_organisasi = False

#Model Logika
dapat_beasiswa = ipk and aktif_organisasi

#Output hasil administrasi
if dapat_beasiswa:
	print("Mendapat beasiswa:", dapat_beasiswa)
else:
	print("Tidak Medapat beasiswa:", dapat_beasiswa)
