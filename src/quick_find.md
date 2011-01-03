QUICK-FIND

BULMA:	"p" ve "q" aynı "id" ye sahipse bağlıdır.

BİRLEŞTİRME: "id[p]" li tüm girdileri "id[q]" ile değiştir.

def BULMA(p, q):
	return id[p] == id[q]

def BİRLEŞTİRME(p, q):
	pid = id[p]
	for i in range(id):
		if id[i] == pid:
			id[i] = id[q]

Örnek:
i	0	1	2	3	4	5	6	7	8	9
id[i]	0	1	9	9	9	6	6	7	8	9

p=3, q=6
i	0	1	2	3	4	5	6	7	8	9
id[i]	0	1	6	6	6	6	6	7	8	6

p=3, q=2		id[3]->6, id[2]->6	İYİLEŞTİR
i	0	1	2	3	4	5	6	7	8	9
id[i]	0	1	6	6	6	6	6	7	8	6

