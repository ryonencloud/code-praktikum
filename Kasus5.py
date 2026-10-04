surat_rujukan = False
kondisi_darurat = True
resep_dokter = False

#Model Logika
klaim_diterima = surat_rujukan or kondisi_darurat or resep_dokter

#Output hasil administrasi
if klaim_diterima:
    print("klaim asuransi DITERIMA")
else:
    print("klaim asuransi DITOLAK")