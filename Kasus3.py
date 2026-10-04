masa_kerja_cukup = True
skp_baik = True
ijazah_terverifikasi = True

#Model Logika
kenaikan_pangkat = masa_kerja_cukup and skp_baik and ijazah_terverifikasi

#Output hasil administrasi
if kenaikan_pangkat:
    print("pegawai MEMENUHI SYARAT kenaikan pangkat")
else:
    print("pegawai TIDAK MEMENUHI SYARAT kenaikan pangkat")