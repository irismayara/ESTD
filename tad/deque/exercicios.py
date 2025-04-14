from Fila import *S

#1. Qual os valores retornados durante a seguinte série de 
#operações em uma deque "d" inicialmente inicialmente vazio? 
#add_first(4), add_last(8), add_last(9), add_first(5), back(),
# delete_first(), delete_last(), add_last(7), first(), last(),
# add_last(6), delete_first(), delete_first().

d = Deque()

d.add_first(4) #[4]
d.add_last(8) #[4,8]
d.add_last(9) #[4,8,9]
d.add_first(5) #[5,4,8,9]
d.last() #9
d.delete_first() #[4,8,9]
d.delete_last() #[4,8]
d.add_last(7) #[4,8,7]
d.first() #4
d.last() #7
d.add_last(6) #[4,8,7,6]
d.delete_first() #[8,7,6]
d.delete_first() #[7,6]

print(d)

#2. Suponha que você tem um deque D contendo os números 
#(1,2,3,4,5,6,7,8) , nesta ordem. Suponha também que você
#inicialmente uma fila F vazia. Apresente o código que usa 
#SOMENTE D e F (e nenhuma outra variável) e armazena em F os 
#elementos de na ordem (1,2,3,4,5,6,7,8).

deque = Deque()
f = Fila()

deque.add_last(1)
deque.add_last(2)
deque.add_last(3)
deque.add_last(4)
deque.add_last(5)
deque.add_last(6)
deque.add_last(7)
deque.add_last(8)

while deque not is_empty():
    f.enqueue(deque.first())
    deque.delete_first()

print(f)

#3. João tem 4 vacas que ele deseja levar para o outro lado de um ponto, 
#mas tem somente uma canga que permite colocar duas vacas, lado a lado, amarradas na canga. 
#A canga é muito pesada pela ele carregar pela ponte, mas ele consegue prender (e soltar)
#as vacas na canga a qualquer momento sem gastar muito tempo (tempo 0). 
#Das suas vacas:
# - Malhada pode atravessar a ponte em 2 minutos
# - Estrelinha pode atravessar em 4 minutos
# - Celeste pode atravessar em 10 minutos
# - Pintada pode atravessar em 20 minutos.
#Claro, quando duas vacas são unidas a canga, elas se andam na velocidade da vaca mais lenta.
#Descreva como João pode levar todas as vacas pela ponte em 34 minutos ou menos.
# - canga = peça de madeira usada para atrelar bois a carroça ou arado, 
#para que andem no mesmo compasso; jugo.


