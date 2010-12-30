nokta_sayisi = input("kullanilacak nokta sayisi:")
nokta_dizisi = range(nokta_sayisi)
deger_dizisi = [1]*nokta_sayisi

print nokta_sayisi

while True:
	girdi = raw_input("baglanti (or. 6-9 veya cikis icin 'end'): ")
	if girdi == "end":
		print "cikis zamani"
		break

	ilk_nokta, ikinci_nokta = girdi.split("-")
	ilk_nokta, ikinci_nokta = int(ilk_nokta), int(ikinci_nokta)

	if (ilk_nokta > nokta_sayisi) or (ikinci_nokta > nokta_sayisi):
	   print "Sinir deger asimi"
 
	gecici_ilk = ilk_nokta
	while gecici_ilk != nokta_dizisi[gecici_ilk]:
		gecici_ilk = nokta_dizisi[gecici_ilk]
	
	gecici_ikinci = ikinci_nokta
	while gecici_ikinci != nokta_dizisi[gecici_ikinci]:
		gecici_ikinci = nokta_dizisi[gecici_ikinci]

	if gecici_ilk != gecici_ikinci:
		if deger_dizisi[gecici_ilk] < deger_dizisi[gecici_ikinci]:
			nokta_dizisi[gecici_ilk] = gecici_ikinci
			deger_dizisi[gecici_ikinci] += deger_dizisi[gecici_ilk]
		else:
			nokta_dizisi[gecici_ikinci] = gecici_ilk
			deger_dizisi[gecici_ilk] += deger_dizisi[gecici_ikinci]

	print girdi + " ",
	print "Yeni durum, nokta: " + str(nokta_dizisi) + ", deger: " + str(deger_dizisi)
