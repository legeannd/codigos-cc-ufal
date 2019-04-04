from lista import chainedList

inteiros = [4,3,2,24,15,8,3,20,1,5,6,7,13,9]
lista_int = chainedList()
flag = 0

for i in range(len(inteiros)):
	lista_int.push(inteiros[i],i)

x = int(input())
for i in range(lista_int.listSize()-1):
	for j in range(lista_int.listSize()-1):
		n1 = lista_int.pop(i)
		n2 = lista_int.pop(j)
		if n1 != None and n2 != None:
			soma = n1 + n2
			if soma == x:
				print('n1', n1)
				print('n2', n2)
				flag += 1
		lista_int.push(n1,i)
		lista_int.push(n2,j)
	soma = 0
if flag == 0:
	print('Nao')