nokta_sayisi = input("kullanilacak nokta sayisi:")
nokta_dizisi = range(nokta_sayisi)

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

	gecici= nokta_dizisi[ilk_nokta]
	if gecici != nokta_dizisi[ikinci_nokta]:
	    sayac = 0
	    while sayac < nokta_sayisi:
		if nokta_dizisi[sayac] == gecici:
		    nokta_dizisi[sayac] = nokta_dizisi[ikinci_nokta]
		sayac += 1

	print girdi + " ",
	print "Yeni durum: " + str(nokta_dizisi)

