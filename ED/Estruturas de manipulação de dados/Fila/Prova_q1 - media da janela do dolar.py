from fila import Queue

w = int(input())
window = Queue()
i = 0
x = None
while True:
	if x == 0:
		break
	if i < w:
		x = float(input())
		window.push(x)
		i += 1
	else:
		soma = 0
		while not window.isEmpty():
			soma += window.pop()
		i = 0
		print(soma/w)