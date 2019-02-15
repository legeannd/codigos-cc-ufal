from pilha_encadeada import ChainedStack

countA = 0
countB = 0
countC = 0
countD = 0
valida = True
p = ChainedStack()

senha = input("Digite a senha\n")
for i in senha:
    if i == 'a':
        countA += 1
    elif i == 'b':
        countB += 1
    elif i == 'c':
        countC += 1
    elif i == 'd':
        countD += 1

if countA != countD or countB != countC:
    valida = False

if valida:
    for i in senha:
        if i == 'a':
            p.pile('d')
        if i == 'b':
            p.pile('c')
        if i == 'c':
            if p.unpile() != 'c':
                valida = False
                break
            else:
                valida = True
        if i == 'd':
            if p.unpile() != 'd':
                valida = False
                break
            else:
                valida = True
print(valida)
