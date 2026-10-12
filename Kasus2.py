username_benar = True
password_benar = False

#Model Logika
login_berhasil = username_benar and password_benar

#Output hasil administrasi
if login_berhasil:
	print("Login berhasil:", login_berhasil)
else:
	print("Gagal login:", login_berhasil)
