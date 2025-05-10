# **Projeto: Simulação de Concorrência com Lista Encadeada**

## **Integrante da Equipe**
- Iris Mayara Vieira Nunes

---

## **Construção do Projeto**

Para a construção do projeto, utilizou-se como base o código das classes `Noh` e `ListaEncadeada`, apresentado em sala de aula e disponibilizado no repositório GitHub do professor. As principais modificações incluíram a implementação dos métodos de inserção no final da lista e remoção no início, como solicitado na atividade.

A simulação do ambiente concorrente foi realizada por meio das classes `Thread`, `Lock` e `Semaphore`, fornecidas pelo módulo `threading`. A função `sleep`, do módulo `time`, foi utilizada para representar atrasos no processamento, simulando o tempo de execução de tarefas reais. Além disso, a biblioteca **Colorama** foi empregada para colorir os logs no terminal, facilitando a distinção das ações realizadas por cada thread produtora, consumidora ou de busca.

Foram criadas três funções principais para simular o comportamento das threads:

- **`tarefa_produtor`** – insere elementos no final da lista, sempre após consultar seu estado atual;
- **`tarefa_consumidor`** – remove elementos do início da lista, após verificar se há itens disponíveis;
- **`tarefa_busca`** – realiza buscas por elementos aleatórios na lista encadeada.

Cada uma dessas funções recebe como parâmetro o identificador da thread e um valor booleano que define se o uso de `Lock` será ativado, permitindo a simulação tanto de cenários seguros (com sincronização) quanto inseguros (com possibilidade de condição de corrida).

Além do `Lock`, foi incorporado um **Semaphore** para controlar o número de itens disponíveis na lista para consumo. A cada inserção realizada por uma thread produtora, o semáforo é incrementado (`release()`), sinalizando que há um novo item disponível. Por sua vez, as threads consumidoras chamam `acquire()` antes de tentar remover um elemento, bloqueando-se automaticamente caso o semáforo indique que não há itens disponíveis. Essa mecânica garante que os consumidores só acessem a lista quando houver elementos a serem processados, evitando erros de acesso a uma lista vazia.

Para evitar deadlocks ao final da execução, especialmente no caso de um número maior de remoções do que inserções, foi adicionado um controle por meio de um contador protegido por `Lock`, que monitora a quantidade de produtores ativos. Quando todos os produtores terminam sua execução e a lista se esvazia, os consumidores são liberados para encerrar sua atividade de forma segura.

---

## **Resultados da Execução do Projeto**

A execução do projeto demonstrou corretamente o funcionamento das threads produtoras, consumidoras e pesquisadoras, que manipularam a lista encadeada com sucesso. Quando executadas com o uso de `Locks`, a sincronização garantiu a integridade dos dados e evitou condições de corrida.

Por outro lado, ao desativar o `Lock`, foi possível observar claramente os efeitos da condição de corrida. Um exemplo notável ocorreu quando uma thread consumidora removeu um elemento da lista mesmo após verificar que ela estava vazia. Isso se deu devido a uma inserção simultânea realizada por uma thread produtora no intervalo entre a verificação e a ação, demonstrando na prática os riscos da falta de sincronização em ambientes concorrentes.

Durante alguns testes, observou-se também que a thread responsável pela busca (**`tarefa_busca`**) iniciou sua execução antes que qualquer elemento fosse inserido na lista. Como resultado, diversas buscas consecutivas retornaram "Não encontrado", pois a lista ainda estava vazia. Esse comportamento era esperado, já que o agendamento das threads é **não determinístico**, e não há garantia de ordem de execução entre produtores e buscadores. A sincronização via `Lock` apenas evita condições de corrida, mas não controla a ordem de execução entre as threads.


Em outro cenário de teste, com um produtor e um consumidor, o produtor foi configurado para inserir 
50 elementos, enquanto o consumidor tentou consumir 60. Como o `Semaphore` foi utilizado sem considerar 
o fim da produção, a thread consumidora permaneceu bloqueada no método `acquire()`, aguardando sinais 
(`release()`) que jamais ocorreriam, uma vez que o produtor já havia encerrado sua execução. Esse caso 
representou um exemplo clássico de deadlock por ausência de sinalização de término, o que evidenciou 
a necessidade de um controle adicional. Para solucionar esse problema, foi implementado um contador 
protegido indicando a quantidade de produtores ativos, permitindo que o consumidor saiba quando deve 
encerrar sua espera.

Por fim, a utilização de cores no terminal, por meio da biblioteca `Colorama`, contribuiu significativamente 
para a visualização das operações realizadas por cada thread, tornando o comportamento concorrente mais 
compreensível e didático.

## **Conteúdo Consultado para Realização do Projeto**
----------------------------------------------
- Código-base das aulas: https://github.com/ricardo9n/estd/tree/main/listas-encadeadas
- How to Use Python Threading Lock to Prevent Race Conditions
- O que é uma condição de corrida? – Stack Overflow:
  https://pt.stackoverflow.com/questions/159342/o-que-%c3%a9-uma-condi%c3%a7%c3%a3o-de-corrida
- Colorama – PyPI: https://pypi.org/project/colorama/
- Python sleep(): How to Add Time Delays to Your Code – Real Python:
  https://realpython.com/python-sleep/
- Semaphores on Python:
  https://stackoverflow.com/questions/31508574/semaphores-on-python

## **Autoavaliação**
-------------
A atividade foi concluída de acordo com os objetivos propostos, proporcionando uma revisão eficaz de 
conceitos fundamentais de sistemas operacionais, como concorrência, sincronização e memória compartilhada. 
Além disso, permitiu explorar funcionalidades relevantes da linguagem Python, como os módulos `threading` 
e `colorama`, bem como reforçar o uso da estrutura de dados `ListaEncadeada` em um contexto prático e realista.

A simulação possibilitou uma visualização concreta dos efeitos causados por condições de corrida, 
especialmente ao comparar a execução com e sem o uso de `Lock`. Essa abordagem evidenciou a importância 
da sincronização no acesso a recursos compartilhados entre threads.

Durante o desenvolvimento, um leve desafio foi enfrentado ao implementar corretamente o uso de semáforos 
(`Semaphore`). Inicialmente, o consumidor ficava bloqueado indefinidamente ao tentar consumir mais elementos 
do que os efetivamente produzidos, resultando em um deadlock. Esse problema foi superado com a introdução 
de um controle adicional de término da produção, usando um contador protegido por Lock, garantindo que os 
consumidores pudessem encerrar sua execução de forma segura quando a produção fosse finalizada.

A alternativa de implementação com o módulo `multiprocessing` foi considerada, mas optou-se por seguir com 
a abordagem baseada em threads, por ser mais direta, leve e compatível com o escopo da atividade proposta.
