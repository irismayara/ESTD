from Noh import *

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def insere_inicio(self, item):  
        temp = Noh(item)
        temp.setNext(self.head)
        self.head = temp

    def insere_fim(self, item):  
        novo_noh = Noh(item)
        if self.head is None:
            self.head = novo_noh
        else:
            atual = self.head
            while atual.getNext() is not None:
                atual = atual.getNext()
            atual.setNext(novo_noh)

    def remove_inicio(self): 
        if self.head is not None:
            removido = self.head.getData()
            self.head = self.head.getNext()
            return removido
        return None

    def size(self):
        atual = self.head
        contador = 0
        while atual is not None:
            contador += 1
            atual = atual.getNext()
        return contador

    def busca_elemento(self, item):
        atual = self.head
        encontrou = False
        while atual is not None and not encontrou:
            if atual.getData() == item:
                encontrou = True
            else:
                atual = atual.getNext()
        return encontrou

    def remove_fim(self, item):
        atual = self.head
        anterior = None
        encontrou = False

        while atual is not None and not encontrou:
            if atual.getData() == item:
                encontrou = True
            else:
                anterior = atual
                atual = atual.getNext()

        if not encontrou:
            print("Item não encontrado na lista.")
            return

        if anterior is None:
            self.head = atual.getNext()
        else:
            anterior.setNext(atual.getNext())

    def __str__(self):
        atual = self.head
        result = '['
        while atual is not None:
            result += str(atual.getData())
            if atual.getNext():
                result += ","
            atual = atual.getNext()
        result += ']'
        return result

    def show(self):
        info = self.head
        dados = []
        while info is not None:
            dados.append(str(info.getData()))
            info = info.getNext()
        print(dados)
