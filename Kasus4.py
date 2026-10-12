punya_member = True
punya_kupon = False

#Model Logika
dapat_diskon = punya_member or punya_kupon

#Output hasil administrasi
if dapat_diskon:
	print("Mendapat diskon:", dapat_diskon)
else:
	print("Tidak Mendapat diskon:", dapat_diskon)
