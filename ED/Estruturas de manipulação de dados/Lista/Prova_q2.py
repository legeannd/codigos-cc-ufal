from lista import chainedList

lista = chainedList()
lista2 = []
while True:
	nome = input("Digite o nome (0 para sair )")
	if nome == '0':
		break
	num = int(input("Digite o numero "))
	lista2 = [nome, num]
	lista.push(lista2)
	lista.listPrint()
print(lista.search(0))