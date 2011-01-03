QUICK-UNION

id[i]: i'nin ebeveynini tutar.
Örnek: i=3, id[3] = 6, 3'ün ebeveyni 6'dır. 6'ya 3 bağlıdır.

BULMA:	"p" ve "q" aynı kök "id" sine sahipse bağlıdır.

BİRLEŞTİRME: "q" nın kök "id" si, "p" nin kök "id" si olur.

def KÖK(i):
	while (i != id[i]):
		i = id[i]
	return id[i]

def BULMA(p, q):
	return KÖK(p) == KÖK(q)

def BİRLEŞTİRME(p, q):
	i = KÖK(p)
	j = KÖK(q)
	
	id[i] = j

Örnek:
i	0	1	2	3	4	5	6	7	8	9
id[i]	0	1	9	4	9	6	6	7	8	9

p=3, q=5	KÖK(3)->9, KÖK(5)->6
i	0	1	2	3	4	5	6	7	8	9
id[i]	0	1	9	4	9	6	6	7	8	6


