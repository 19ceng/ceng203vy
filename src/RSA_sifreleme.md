e: AÇIK/PUBLIC,	d: ÖZEL/PRIVATE

>>> (Ae,Ad,n) = RSAgenkeys(p=5563, q=8191)
>>> (Be,Bd,n) = RSAgenkeys(p=5563, q=8191)

>>> m = ord('A')

A) M MESAJINI SADECE B KULLANICISI ALMASI İÇİN NASIL ŞİFRELERİZ?

	 c = modexp(m, Be, n)
	mc = modexp(c, Bd, n)

B) M MESAJINI A'nın GÖNDERDİĞİNDEN NASIL EMİN OLABİLİRİZ?

	 c = modexp(m, Ad,n)
	mc = modexp(c, Ae, n)

C) M MESAJINI GÖNDEREN A, ALAN B

	# sifrele(bilgi, anahtar)

	# verici
	 c = sifrele(sifrele(m,  Ad), Be)

	# alici
	mc = sifrele(sifrele(c,  Bd), Ae)
	

>>> c = modexp(m, e, n)			# s117
c = 1879653L

>>> mc = modexp(c, d, n)
>>> chr(mc)
'A'
