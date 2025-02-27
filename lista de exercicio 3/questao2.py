#2. Escreva uma função recursiva que permita inverter uma palavra N. "Python" -->> "nohtyP"

def inverter(palavra):
    if len(palavra) == 1:
        return palavra
   
    return palavra[-1] + inverter(palavra[:-1])
        
print(inverter('python'))
print(inverter('recursiva'))