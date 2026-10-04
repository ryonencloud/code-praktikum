kartu_pkh = False
surat_sktm = False
kip_kuliah = True

#Model Logika
bantuan_layak = kartu_pkh or surat_sktm or kip_kuliah

#Output hasil administrasi
if bantuan_layak:
    print("pendaftar LAYAK menerima bantuan")
else:
    print("pendaftar TIDAK LAYAK menerima bantuan")