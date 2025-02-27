def super_digito(num):
    num = str(num)

    if len(num) == 1:
        return int(num)
    
    return int(num[-1]) + super_digito(num[:-1])

print(super_digito(71))

