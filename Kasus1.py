nota_lengkap = True
lpj_disetujui = True
kuitansi_sah = True

#Model Logika
pencairan = nota_lengkap and lpj_disetujui and kuitansi_sah

#Output hasil administrasi
if pencairan:
    print("pencairan anggaran SIAP DIPROSES")
else:
    print("pencairan anggaran DITOLAK")