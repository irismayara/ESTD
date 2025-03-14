from Tarefa import *
from ListaTarefas import *

def criaListaVazia():
    return ListaTarefas()

def criaTarefas():
    return [
        Tarefa("Fazer a lista de TAD", "Média"), #0
        Tarefa("Ler o artigo", "Média"), #1
        Tarefa("Ler um livro", "Baixa"), #2
        Tarefa("Resolver exercícios de Álgebra", "Alta"), #3
        Tarefa("Revisar matéria para prova", "Alta"), #4
        Tarefa("Estudar Python", "Média"), #5
        Tarefa("Escrever relatório", "Média"), #6
        Tarefa("Fazer compras", "Baixa"), #7
        Tarefa("Assistir aula online", "Alta"), #8
        Tarefa("Ler um artigo científico", "Média"), #9
    ]

def criaListaPreechida():
    lista = criaListaVazia()
    tarefas = criaTarefas()[:9]

    for tarefa in tarefas:
        lista.adicionar_no_fim(tarefa)

    return lista

def testeLista():
    lista = criaListaVazia()

    print(lista.capacidade) # Saída: 10
    print(lista.tamanho) # Saída: 0
    print(lista.tarefas) # Saída: [None, None, None, None, None, None, None, None, None, None]

def testeAdicionarNoFinal():
    lista = criaListaVazia()

    tarefa1, tarefa2, tarefa3 = criaTarefas()[:3]

    lista.adicionar_no_fim(tarefa1)
    lista.adicionar_no_fim(tarefa2)
    lista.adicionar_no_fim(tarefa3)

    print(lista) 
    print(lista.tamanho) # Saída: 3

def testeAdicionarNoInicio():
    lista = criaListaPreechida() # com 9 elementos
    nova_tarefa = criaTarefas()[9]

    ## adiciona no inicio, posicao: 0
    lista.adicionar_em_posicao(nova_tarefa, 0)

    print(lista)
    print(lista.tamanho) # Saída 10

def testeAdicionarNoMeio():
    lista = criaListaPreechida() # com 9 elementos
    nova_tarefa = criaTarefas()[9]

    ## adiciona no meio, posicao: tamaho//2
    lista.adicionar_em_posicao(nova_tarefa, lista.tamanho//2)

    print(lista)
    print(lista.tamanho) # Saída 10

def testeAdicionarNoFim():
    lista = criaListaPreechida() # com 9 elementos
    nova_tarefa = criaTarefas()[9]

    ## adiciona no fim, posicao: tamanho
    lista.adicionar_em_posicao(nova_tarefa, lista.tamanho)

    print(lista)
    print(lista.tamanho) # Saída 10

def testeAdicionarPosicaoInvalida():
    lista = criaListaPreechida() # com 9 elementos
    nova_tarefa = criaTarefas()[9]

    ## adiciona em posicao invalida, posicao: 10
    lista.adicionar_em_posicao(nova_tarefa, 10)

    print(lista)
    print(lista.tamanho) # Saída 9

def testeObterTarefa():
    lista = criaListaPreechida()

    print(lista.obter_tarefa(3)) #Saída: Tarefa("Resolver exercícios de Álgebra", "Alta")

def testeRemoverTarefa():
    lista = criaListaPreechida()
    print(lista.tamanho)
    print(lista)

    lista.remover_tarefa(3)
    
    print(lista)
    print(lista.tamanho)

testeRemoverTarefa()

