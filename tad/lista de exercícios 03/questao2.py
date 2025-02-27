class Conjunto:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.itens = list()
        for i in range(tamanho):
            self.itens.append(None)

    def ehUnico(self, item):
        for i in range(self.tamanho):
            if(self.itens[i] == item):
                return False
        return True

    def adiciona(self, item):
        if self.ehUnico(item):
            for i in range(self.tamanho):
                if self.itens[i] is None:
                    self.itens[i] = item
                    return
        print(f'O item {item} não pôde ser adicionado: conjunto cheio ou item duplicado.')

novo_conjunto = Conjunto(5)
novo_conjunto.adiciona('TESTE')
novo_conjunto.adiciona('OUTRO TESTE')
novo_conjunto.adiciona('TESTE')
print(novo_conjunto.itens)
