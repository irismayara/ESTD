class Deque:
  
  CAPACIDADE_PADRAO = 5 

  def __init__(self):
    self._dados = [None] * Deque.CAPACIDADE_PADRAO
    self._tamanho = 0
    self._inicio = 0
    self._fim = 0

  def __len__(self):
    return self._tamanho 

  def is_empty(self):
    return self._tamanho == 0

  def first(self):
    if not self.is_empty():
        return self._dados[self._inicio]
    
  def last(self):
    if not self.is_empty():
        return self._dados[self._fim]

  def delete_first(self):
    if not self.is_empty():
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) % len(self._dados)
        self._tamanho -= 1
        return result
    
  def delete_last(self):
    if not self.is_empty():
        result = self._dados[self._fim]
        self._dados[self._fim] = None
        self._fim = (self._fim - 1) % len(self._dados)
        self._tamanho -= 1
        return result

  def add_first(self, e): 
    if self._tamanho == len(self._dados):
      self._altera_tamanho(2 * len(self._dados))
    disponivel = (self._inicio + self._tamanho) % len(self._dados)
    self._dados[disponivel] = e
    self._inicio = (self._inicio - 1) % len(self._dados)
    self._tamanho += 1

  def add_last(self, e):  
    if self._tamanho == len(self._dados):
      self._altera_tamanho(2 * len(self._dados))
    disponivel = (self._inicio + self._tamanho) % len(self._dados)
    self._dados[disponivel] = e
    self._fim = (self._fim + 1) % len(self._dados)
    self._tamanho += 1

  def _altera_tamanho(self, novo_tamanho):   # novo_tamanho precisar ser >= len(self)
    dados_antigos = self._dados               # keep track of existing list
    self._dados = [None] * novo_tamanho       # allocate list with new capacity
    posicao = self._inicio
    for k in range(self._tamanho):            # only consider existing elements
      self._dados[k] = dados_antigos[posicao] # intentionally shift indices
      posicao = (1 + posicao) % len(dados_antigos) # use dados_antigos size as modulus
    self._inicio = 0                          # front has been realigned

  def show(self):
    print(self)

  def __str__(self):
    posicao = self._inicio
    result = "["
    
    for k in range(self._tamanho):
      result += str(self._dados[posicao]) + ", "
      posicao = (1 + posicao) % len(self._dados)
    result += f'] tamanho: {len(self)} capacidade {len(self._dados)}\n'
    return result