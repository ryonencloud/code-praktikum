kehadiran_memenuhi = False
izin_dosen = False

#Model Logika
boleh_ujian = kehadiran_memenuhi or izin_dosen

#Output hasil administrasi
if boleh_ujian:
	print("Boleh mengikuti ujian:", boleh_ujian)
else:
	print("Tidak Boleh mengikuti ujian:", boleh_ujian)
