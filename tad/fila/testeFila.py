from Fila import *

fila = Fila()
fila.enqueue(5) # [5]
fila.enqueue(3) # [5, 3]
fila.dequeue() # [3]
fila.enqueue(2) # [3, 2]
fila.enqueue(8) #  [3, 2, 8]
fila.dequeue() # [2, 8]
fila.dequeue() # [8]
fila.enqueue(9) # [8, 9]
fila.enqueue(1) # [8, 9, 1]
fila.dequeue() # [9, 1]
fila.enqueue(7) # [9, 1, 7]
fila.enqueue(6) # [9, 1, 7, 6]
fila.dequeue() # [1, 7, 6]
fila.dequeue() # [7, 6]
fila.enqueue(4)  # [7, 6, 4]
fila.dequeue() # [6, 4]
fila.dequeue() # [4]

#print(fila)

fila.enqueue(9)
fila.enqueue(3)
fila.dequeue()
fila.dequeue()
fila.enqueue(1)
fila.enqueue(7)
fila.dequeue()
fila.dequeue()
fila.enqueue(8)
fila.enqueue(5)
fila.enqueue(4)
fila.enqueue(0)
fila.enqueue(2)
fila.enqueue(9)
fila.enqueue(3)

print(fila.inicio)


print(fila.dados)

