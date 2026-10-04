serah_hardcopy = True
serah_softcopy = False

#Model Logika
penyerahan_valid = serah_hardcopy ^ serah_softcopy

#Output hasil administrasi
if penyerahan_valid:
    print("penyerahan dokumen VALID (pilih tepat satu metode)")
else:
    print("penyerahan dokumen INVALID (pilih salah satu, tidak boleh keduanya/kosong)")