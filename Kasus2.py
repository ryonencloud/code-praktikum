surat_pengantar = True
proposal_disetujui = True
bebas_tanggungan = True

#Model Logika
izin_terbit = surat_pengantar and proposal_disetujui and bebas_tanggungan

#Output hasil administrasi
if izin_terbit:
    print("surat izin penelitian DAPAT DITERBITKAN")
else:
    print("surat izin penelitian BELUM DAPAT DITERBITKAN")