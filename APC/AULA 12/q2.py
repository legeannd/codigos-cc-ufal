import pickle
arq = open('arq2.txt','wb')
while True:
    x = input('Digite valores(digite sair para sair)')
    if x == 'sair':
        break
    x = int(x)
    pickle.dump(x, arq)
print(pickle.load(arq))
