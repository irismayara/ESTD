class DequeTamanhoFixo:
    def __init__(self, capacidade):
        self._dados = [None] * capacidade
        self._inicio = 0
        self._tamanho = 0
    
    def add_first(self, e):
        if self._tamanho == len(self._dados):
            self._inicio = (self._inicio + self._tamanho - 1) % len(self._dados)
            self._dados[self._inicio] = e
        else:
            self._inicio = (self._inicio + 1) % len(self._dados)
            self._dados[self._inicio] = e
            self._tamanho += 1

    def add_last(self, e):
        if self._tamanho == len(self._dados):
            self._dados[self._inicio] = e
            self._inicio = (self._inicio + 1) % len(self._dados)
        else:
            disponivel = (self._inicio + self._tamanho) % len(self._dados)
            self._dados[disponivel] = e
            self._tamanho += 1
    
    def __str__(self):
        posicao = self._inicio
        result = "["
        
        for k in range(self._tamanho):
            result += str(self._dados[posicao]) + ", "
            posicao = (1 + posicao) % len(self._dados)
        result += f']'
        return result


d = DequeTamanhoFixo(3)
d.add_last(1)
d.add_last(2)
d.add_last(3)

print(d) #[1,2,3]

d.add_last(4) 

print(d) #[2,3,4]

d.add_first(0)

print(d) #[0,2,3]