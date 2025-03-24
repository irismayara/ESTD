class Pilha:
    def __init__(self):
        self.pilha = []

    def __len__(self):
        return len(self.pilha)

    def push(self, elemento):
        self.pilha.append(elemento)

    def pop(self):
        if not self.isEmpty:
            return self.pilha.pop()

    def top(self):
        if not self.isEmpty:
            return self.pilha[-1]

    def isEmpty(self):
        return len(self.pilha) == 0