def soma_nao_primos(a, b):
    a = a+1

    if a >= b:
        return 0

    if a % 2 == 0 and a != 2:
        return soma_nao_primos(a, b)
    elif a % 3 == 0 and a != 3:
        return soma_nao_primos(a, b)
    elif a % 5 == 0 and a != 5:
        return soma_nao_primos(a, b)
    
    return a + soma_nao_primos(a, b)

print(soma_nao_primos(4,8))
print(soma_nao_primos(4,10))
print(soma_nao_primos(10,20))
print(soma_nao_primos(24, 28))
