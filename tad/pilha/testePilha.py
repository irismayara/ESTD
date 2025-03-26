from Pilha import *

p = Pilha()

p.push(5) # [5]
p.push(3) # [5, 3]
p.pop() # Remove: 3; [5]
p.push(2) # [5, 2]
p.push(8) # [5, 2, 8]
p.pop() # Remove: 8; [5, 2]
p.pop() # Remove: 2; [5]
p.push(9) # [5, 9]
p.push(1) # [5, 9, 1]
p.pop() # Remove: 1; [5, 9]
p.push(7) # [5, 9, 7]
p.push(6) # [5, 9, 7, 6]
p.pop() # Remove: 6; [5, 9, 7]
p.pop() # Remove: 7; [5, 9]
p.push(4) # [5, 9, 4]
p.pop() # Remove: 4; [5, 9]
p.pop() # Remove: 9; [5]


p.push(14)
p.push(4)
p.push(1)
p.push(2)
p.push(22)
p.push(5)
print(p)
#p.removeTodos()
print(p.inverte())
