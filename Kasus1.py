nilai_teori = True
nilai_praktik = True

#Model Logika
lulus = nilai_teori and nilai_praktik 

#Output hasil administrasi
if lulus:
	print("Siswa lulus:", lulus)
else:
	print("Siswa Tidak lulus")
