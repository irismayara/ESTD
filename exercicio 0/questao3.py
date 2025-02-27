#3. Calcule o fatorial de um numero qualquer. 
# O fatorial de um número n é n * (n-1) * (n-2) * ... * 1.

def fatorial(n):
    if n == 0:
        return 1

    return n * fatorial(n-1)

print(fatorial(4))