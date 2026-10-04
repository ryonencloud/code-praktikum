kartu_keluarga = False
surat_pindah = True
ktp_lama = False

#Model Logika
identitas_valid = kartu_keluarga or surat_pindah or ktp_lama

#Output hasil administrasi
if identitas_valid:
    print("verifikasi identitas BERHASIL")
else:
    print("verifikasi identitas GAGAL")