rt = int(input('Root: '))
lim = int(input('Limite: '))
i=0
num = 0
vezes = 1
while num < lim:
    num = (i)*rt +1
    print(i,' -> ',num)
    i+= (rt-1)*vezes
    vezes+=rt-2
