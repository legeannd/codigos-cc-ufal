from pilha_encadeada import ChainedStack

p = ChainedStack()
aux = ChainedStack()
flag = 0
while True:
    tarefa = int(input("Digite a prioridade da tarefa\n"))
    if tarefa == 0:
        break
    if str(tarefa) in '12345':
        if flag == 1:
            print('\n')
            while p.top.item > tarefa:
                num = p.unpile()
                print("Desempilhou",num,"da principal\n")
                aux.pile(num)
                print("Empilhou",num,"na auxiliar\n")
        p.pile(tarefa)
        flag = 1
        print('\n')
        while not aux.isEmpty():
            num = aux.unpile()
            print("Desempilhou",num,"da auxiliar\n")
            p.pile(num)
            print("Empilhou",num,"na principal\n")
print('Ordem de tarefas:')
p.stackPrint()
