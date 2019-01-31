from pilha import Pilha
exp = '3-[15+2*(4-3)*[2+(5-1)]]/4'
p = Pilha(len(exp))
bem = True
for i in range(len(exp)):
    if exp[i] in '{[(':
        p.empilhar(exp[i])
    elif exp[i] in ')' and p.desempilhar() != '(':
        bem = False
        break
    elif exp[i] in '}' and p.desempilhar() != '{':
        bem = False
        break
    elif exp[i] in ']' and p.desempilhar() != '[':
        bem = False
        break

bem = p.vazia()
print('Expressão bem formada') if bem == True else print('Expressão mal formada')
