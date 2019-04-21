from sqrt import sqrt

while True:
    num = float(input("num: "))
    intervalo = 0
    with open("log", "w") as f:
        ultimo = 0
        i= 0

        while  i <= num:
            res = sqrt(i)            
            f.write('(%.1f, %f)\n' % (i, i-res.real**2))#((i**(1/2))-res.real)))
            i+= 1