from fila_encadeada import Queue

pacotes = [1,2,3,5,6,8,10,4,7,9,15,12,11,13,14]
fila = Queue()
aux = Queue()

for i in pacotes:
    if fila.isEmpty():
        fila.push(i)
    else:
        print('o i é: ',i)
        if fila.end.item > i:
            print('ENTROU NO I ', i)
            while fila.start.item < i:
                popinho = fila.pop()
                aux.push(popinho)

                print('enfileirou',popinho)
            aux.push(i)

            while(fila.start != None):
                val = fila.pop()
                aux.push(val)

            while(aux.start != None):
                val = aux.pop()
                fila.push(val)

            print('enfileirou fora do while', i)
            print('principal')
            fila.queuePrint()
            print('auxiliar')
            aux.queuePrint()

        else:
            fila.push(i)
while not fila.isEmpty():
    aux.push(fila.pop())
print('principal')
fila.queuePrint()
print('auxiliar')
aux.queuePrint()
