def eh_num_perfeito(num, div=1, soma=0):
    if div == num:
        if soma == num:
            return True
        else:
            return False
    
    if num % div == 0:
        soma += div

    return eh_num_perfeito(num, div+1, soma)

print(eh_num_perfeito(496))     # True
print(eh_num_perfeito(24))     # False
print(eh_num_perfeito(5))     # False
print(eh_num_perfeito(6))     # True
print(eh_num_perfeito(1))     # False
print(eh_num_perfeito(28))     # True