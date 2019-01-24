n = int(input())
fator = []
for i in range(1, n+1):
    if n%i==0:
        fator.append(i)
print(fator)
