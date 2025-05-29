from HashTable import *

# 1. Implemente o método __len___ para uma classe HashTable que retorne
#  o número de itens na tabela hash. 

def __len__(self):
    tamanho = 0
    for i in self._slots:
        if i is not None:
            tamanho += 1
    return tamanho

# 2. Implemente o método ___contains_ para verificar se uma chave está
#  presente em uma tabela hash. 

def __contains__(self, chave):
    return chave in self._slots

h = HashTable()

print(len(h))

h.put(1, 'a')
h.put(12, 'b')  # colisão com 1 se tamanho for 11
h.put(23, 'c')

print(len(h))

# 3. Considere o trecho de código abaixo. Qual será o valor retornado pela função 
# hash_val para chave = 25 ? 

def hash_val (chave, tamanho): 
    return chave % tamanho 

tamanho = 10 
print (hash_val(25, tamanho)) # 5

#4. Qual técnica de rehash está sendo implementada no código a seguir? 

def rehash (indice, tamanho, tentativa): 
    return (indice + tentativa ** 2) % tamanho # quadract probing

# 5. Qual o resultado da execução do código abaixo? 
tabela = [None] * 7 
chave = 20 
indice = chave % len(tabela) 
tabela[indice] = 'Valor' 
print(tabela) # [None, None, None, None, None, None, 'Valor']



