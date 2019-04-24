def decimal_places(num):
    places = 0
    if num == 0: 
        return 0
    while num < 1:
        num *= 10
        places += 1
    return places+3

def sqrt(num):
    num_abs = abs(num)

    resultado = 0
    impar = 1
    
    places = decimal_places(num_abs)
    num_abs *= 10** (places*2)

    while impar < num_abs:
        resultado += 1
        num_abs -= impar
        impar += 2

    resultado += (num_abs)/impar

    resultado /= 10**places

    if num < 0:
        resultado= complex(0, resultado)
    else:
        resultado= complex(resultado, 0)

    return resultado

print(sqrt(float(input('Num: '))))