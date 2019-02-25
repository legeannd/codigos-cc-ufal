from fila import Queue

download = ['d1','d2','d3','d4','d5','d6','d7','','','','d8','d9']
upload = ['u1','u2','','','','u3','u4','u5','u6','u7']

fdown = Queue()
fup = Queue()

for i in download:
	fdown.push(i)
for i in upload:
	fup.push(i)

trafego = Queue()

i = 0
j = 0 
flag = False
while True:
	if not fdown.isEmpty():
		if not flag and i < 6:
			pacote = fdown.pop()
			if pacote != '':
				trafego.push(pacote)
				i += 1
			else:
				flag = True
				i = 6
		if i == 6:
			i = 0
			flag = True
	else:
		flag = True
	if not fup.isEmpty():
		if flag and j < 3:
			pacote = fup.pop()
			if pacote != '':
				trafego.push(pacote)
				j += 1
			else:
				flag = False
				j = 3
		if j == 3:
			j = 0
			flag = False
	else:
		flag = False
	if fdown.isEmpty() and fup.isEmpty():
		trafego.queuePrint()
		break