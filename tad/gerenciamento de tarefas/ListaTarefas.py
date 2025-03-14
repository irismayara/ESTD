class ListaTarefas:
    def __init__(self):
        self.capacidade = 10
        self.tamanho = 0
        self.tarefas = [None] * self.capacidade

    def __str__(self):
        string = '['

        if self.tamanho > 0:
            for t in self.tarefas: 
                if t == None: break
                string += str(t)
                string += ', '
        
        return string[: -2] + ']'
    
    def adicionar_no_fim(self, tarefa):
        if self.tamanho < self.capacidade:
            self.tarefas[self.tamanho] = tarefa
        self.tamanho += 1

    def adicionar_em_posicao(self, tarefa, posicao):
        if posicao < 0 or posicao > self.tamanho:
            print("Posição Inválida!")
            return 
        
        if self.tamanho < self.capacidade:
            novo_elemento = tarefa
            for i in range(posicao, self.capacidade):
                temp = self.tarefas[i]
                self.tarefas[i] = novo_elemento
                novo_elemento = temp
            self.tamanho += 1

    def obter_tarefa(self, posicao):
        pass

    def remover_tarefa(self, posicao):
        pass

    def contem(self, tarefa):
        pass

    def tamanho(self):
        pass


    