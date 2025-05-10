from ListaEncadeada import *
from threading import Thread, Lock, Semaphore
from time import sleep
from random import randint
from colorama import Fore, Style, init

lista = ListaEncadeada()
lock = Lock()
controle_produtores = Lock()
semaforo = Semaphore(0)

produtores_ativos = 2

init(autoreset=True)

def tarefa_produtor(id_thread, usar_lock=True):
    for i in range(50):
        if usar_lock:
            with lock:
                print(Fore.GREEN + f"{id_thread} - Consulta lista: {lista}")
                sleep(1)  
                lista.insere_fim(i)
                semaforo.release()
                print(Fore.YELLOW + f"{id_thread} - Escreve na lista: {lista}")
        else:
            print(Fore.GREEN + f"{id_thread} - Consulta lista: {lista}")
            sleep(1)
            lista.insere_fim(i)
            semaforo.release()
            print(Fore.YELLOW + f"{id_thread} - Escreve na lista: {lista}")
    
    global produtores_ativos
    with controle_produtores:
        produtores_ativos -= 1

def tarefa_consumidor(id_thread, usar_lock=True):
    for i in range(60):
       
        with controle_produtores:
            if produtores_ativos == 0 and lista.is_empty():  #Finaliza se não houver mais produtores ou itens para remover
                break

        semaforo.acquire()  

        if usar_lock:
            with lock:
                print(Fore.GREEN + f"{id_thread} - Consulta lista: {lista}")
                sleep(1) 
                removido = lista.remove_inicio()
                print(Fore.RED + f"{id_thread} - Remove da lista: {removido}")
        else:
            print(Fore.GREEN + f"{id_thread} - Consulta lista: {lista}")
            sleep(1)
            removido = lista.remove_inicio()
            print(Fore.RED + f"{id_thread} - Remove da lista: {removido}")

def tarefa_busca(id_thread, usar_lock=True):
    for _ in range(30):
        alvo = randint(0,49)
        
        if usar_lock:
            with lock:
                encontrado = lista.busca_elemento(alvo)
                sleep(1)
                cor = Fore.CYAN if encontrado else Fore.MAGENTA
                print(cor + f"{id_thread} Buscou por {alvo}: {'Encontrado' if encontrado else 'Não encontrado'}")
        else:
            encontrado = lista.busca_elemento(alvo)
            sleep(1)
            cor = Fore.CYAN if encontrado else Fore.MAGENTA
            print(cor + f"{id_thread} Buscou por {alvo}: {'Encontrado' if encontrado else 'Não encontrado'}")

t1 = Thread(target=tarefa_produtor, args=("[Produtor-1]", True))
t2 = Thread(target=tarefa_produtor, args=("[Produtor-2]", True))
t3 = Thread(target=tarefa_consumidor, args=("[Consumidor-1]", True))
t4 = Thread(target=tarefa_consumidor, args=("[Consumidor-2]", True))
t5 = Thread(target=tarefa_busca, args=("[Buscador]", True))

t1.start()
t2.start() 
t3.start()
t4.start()  
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print(Style.BRIGHT + f"\n Lista final: {lista}")