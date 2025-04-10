from .tad.pilha.Pilha import *

class Fila:
    def __init__(self):
        self.pilha1 = Pilha()
        self.pilha2 = Pilha()
        self.tamanho = 0
        self.atual = self.pilha1
        self.inserir = self.pilha2
    
    def first(self):
        if not self.atual.isEmpty():
            return self.atual.top()
    
    def dequeue(self):
        if not self.atual.isEmpty():
            self.atual.pop()
            self.tamanho -= 1
    
    def enqueue(self, x):
        if self.atual.isEmpty():
            self.atual.push(x)
            self.tamanho += 1
        else:
            while not self.atual.isEmpty():
                self.inserir.push(self.atual.pop())

            self.inserir.push(x)
            self.tamanho += 1
        
            while not self.inserir.isEmpty():
                self.atual.push(self.inserir.pop())