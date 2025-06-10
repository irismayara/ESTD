from BinaryTree import *

#8. Escreva um código python que construa uma árvore binária usando listas de listas 
# para representar a seguinte estrutura:
# ['a', 
#   ['b', 
#       ['c', 
#           [], [d]
#       ], 
#       ['e', 
#           [f], []
#       ]
#   ], 
#   ['g', 
#       ['h', 
#           [i], []
#       ], 
#       []
#   ]
# ] 

r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('g')

node_b = r.getLeftChild()
node_b.insertLeft('c')
node_b.insertRight('e')

node_g = r.getRightChild()
node_g.insertLeft('h')

node_c = node_b.getLeftChild()
node_c.insertRight('d')

node_e = node_b.getRightChild()
node_e.insertLeft('f')

node_h = node_g.getLeftChild()
node_h.insertLeft('i')

print(r)

#9. Implemente a função eh_folha (tree) que retorna True se a árvore contém apenas um nó 
# (ou seja, a raiz não tem filhos), e False caso contrário. 

def eh_folha(tree):
    return tree[1] == [] and tree[2] == []

print(eh_folha(['a', [], []])) # True 
print(eh_folha (['a', ['b', [], []], []])) # False 

#10. Implemente a função `tem_filho (tree)` que retorna `True` se a árvore contém 
# pelo menos um filho, e `False` caso contrário. 

def tem_filho(tree):
    return tree[1] != [] or tree[2] != []

print(tem_filho(['a', [], []])) # False 
print(tem_filho(['a', ['b', [], []], []])) # True 

#11. Implemente uma função `altura (tree)` que retorna a **altura** de uma árvore binária 
# representada como listas de listas. 

def altura (tree):
    if tree == []:
        return 0
    esquerda = tree[1]
    direita = tree[2]
    return 1 + max(esquerda, direita)

#12. Implemente uma função contar_nos (tree) que retorna a quantidade total de nós na árvore. 

def contar_nos(tree):
    if tree == []:
         return 0
    return 1 + contar_nos(tree[1]) + contar_nos(tree[2])

print(contar_nos([]))  # 0
print(contar_nos(['a', [], []]))  # 1
print(contar_nos(['a', ['b', [], []], []]))  # 2
print(contar_nos(['a', ['b', ['d', [], []], []], ['c', [], []]]))  # 4