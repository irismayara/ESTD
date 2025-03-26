class Pilha:
    def __init__(self):
        self.pilha = []

    def __len__(self):
        return len(self.pilha)
    
    def __str__(self):
        return str(self.pilha)

    def push(self, elemento):
        self.pilha.append(elemento)

    def pop(self):
        if not self.isEmpty():
            return self.pilha.pop()

    def top(self):
        if not self.isEmpty:
            return self.pilha[-1]

    def isEmpty(self):
        return len(self.pilha) == 0

    def removeTodos(self):
        if not self.isEmpty():
            self.pop()
            return self.removeTodos()
        
    def inverte(self):
        nova_pilha = Pilha()
        while not self.isEmpty():
            nova_pilha.push(self.pop())
        return nova_pilha
