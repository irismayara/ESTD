class Fila:
    CAPACIDADE_PADRAO = 5

    def __init__(self, capacidade = CAPACIDADE_PADRAO):
        self.dados = [None] * capacidade
        self.tamanho = 0
        self.inicio = 0

    def __len__(self):
        return self.tamanho

    def __str__(self):
        posicao = self.inicio
        result = "["
              
        for k in range(self.tamanho):
            result += str(self.dados[posicao]) + ", "
            posicao = (1 + posicao) % len(self.dados)
        result += f'] tamanho: {len(self)} capacidade {len(self.dados)}\n'
        return result

    def first(self):
        if not self.is_empty():
            return self.dados[self.inicio]

    def enqueue(self, e):
        if self.tamanho == len(self.dados):
            raise FilaCheia('A fila está cheia.')
            #self.altera_capacidade(2 * len(self.dados))
        disponivel = (self.inicio + self.tamanho) % len(self.dados)
        self.dados[disponivel] = e
        self.tamanho += 1

    def dequeue(self):
        if not self.is_empty():
            inicio = self.dados[self.inicio]
            self.dados[self.inicio] =  None
            self.inicio = (self.inicio + 1) % len(self.dados)
            self.tamanho -= 1
            return inicio

    def is_empty(self):
        return self.tamanho == 0

    def altera_capacidade(self, nova_capacidade):
        dados_antigos = self.dados               
        self.dados = [None] * nova_capacidade       
        posicao = self.inicio
        for k in range(self.tamanho):            
            self.dados[k] = dados_antigos[posicao]
            posicao = (1 + posicao) % len(dados_antigos) 
            self.inicio = 0  
    
    def rodar(self):
        if not self.is_empty():
            disponivel = (self.inicio + self.tamanho) % len(self.dados)
            self.dados[disponivel] = self.dados[self.inicio]
            self.dados[self.inicio] =  None
            self.inicio = (self.inicio + 1) % len(self.dados)
            
class FilaCheia(Exception):
    pass