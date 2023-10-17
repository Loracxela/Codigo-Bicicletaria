# ---------------Inicio das Variáveis Globais---------------
lista_peça = []

# ---------------Fim das Variáveis Globais---------------

# ---------------Inicio de cadastrar_peça()---------------
def cadastrar_peça(código):  # Para a criação de uma função
    print('Bem-vindo(a) ao meu Cadastro de Peça:')
    print('Código da Peça: {}'.format(código))
    nome = input('Entre com o NOME da Peça: ')
    fabricante = input('Entre como FABRICANTE da Peça:')
    preço = float(input('Entre com o PREÇO(R$) da Peça: '))  # int representa a classe dos números inteiros em Python # input permite solicitar uma informação ao usuário, faz um login em um sistema
    dicionário_peça = {'código': código,
                       'nome': nome,
                       'fabricante': fabricante,
                       'preço': preço}
    lista_peça.append(dicionário_peça.copy())


# ---------------Fim de cadastrar_peça()---------------

# ---------------Inicio de consultar_peça()---------------
def consultar_peça():  # Para a criação de uma função
    while True:  # Enquando(while): Estrutura de repetição utilizada quando queremos que determinado bloco de código seja executado
        try:
          print('Bem-vindo(a) a Consulta de Peças: ')
          consultar_peça = int(input('\n Escolha a opção desejada:\n' +  # Input permite solicitar uma informação ao usuário, faz um login em um sistema
                                     '1-Consultar TODAS as peças \n' +
                                     '2-Consultar peça por CÓDIGO \n' +
                                     '3-Consultar produto (s) por FABRICANTE \n' +
                                     '4-Retornar \n' +
                                     '>>'))
          if consultar_peça == 1 :  # Funsão if significa 'se', ela é execultada apenas se a condição for verdadeira
              print('Você escolheu a opção Consultar TODAS as Peças:')
              for peça in lista_peça:  # Peça vai varrer toda a lista de peças
                print('-------------------------')
                for key, value in peça.items():  # Varrer todos os conjuntos de chaves e valor do dicionário peça desejada
                  print('{}: {}'.format(key, value))
                  print('-------------------------')
          elif consultar_peça == 2 :  # O comando elif é utilizado quando queremos realizar a verificação de outra expressão caso a primeira validação seja falsa
            print('Você escolheu a opção Consultar Peça por CÓDIGO:')
            código = int(input('Entre com o CÓDIGO desejado:'))
            for peça in lista_peça:
              if (peça['código'] == código) :
                print('-------------------------')
                for key, value in peça.items():  # Varrer todos os conjuntos chaves e o valor do dicionário peça
                 print('{} : {}'.format(key, value))
                 print('-------------------------')
          elif consultar_peça == 3 :
            print('Você escolheu a opção Consultar Peça(s) por FABRICANTE:')
            fabricante = input('Entre com Fabricante desejado: ')
            for peça in lista_peça:
              if (peça['fabricante'] == fabricante) :  # O valor do campo código desse dicionário é igual o valor
                print('-------------------------')
                for key, value in peça.items():  # Varrer todos os conjuntos chaves e o valor do dicionário peça
                  print('{} : {}'.format(key, value))
                  print('-------------------------')

            break
          else:  # O comando é usado para execultar um bloco de códgo, caso o resultado da expressão informada na instrução if seja falso
            print('Opção Inválida. Tente Novamente:')
            continue  # Volta para o inicio do laço
        except ValueError:
         continue

# ---------------Fim de consultar_peça()---------------

# ---------------Inicio de remover_peça()---------------

def remover_peça():  # Para a criação de uma função
    print('Bem-vindo(a) ao menu Remover Peça:')
    código = int(input('Entre com o CÓDIGO da peça que seja remover: '))
    for peça in lista_peça:  # for é utilizado para percorrer ou iterar sobre uma sequência de dados(listas,tupla,string), executa um conjunto de instruções em cada item
          if (peça['código'] == código):
            lista_peça.remove(peça)
            print('Produto Removido:')


# ---------------Fim de remover_peça()---------------

# ---------------Inicio de Main()---------------
print('Bem-vindo(a) a Bicicletaria')
registro = 0
while True: # Enquando(while): Estrutura de repetição utilizada quando queremos que determinado bloco de código seja executado
  try:
    print('Escolha a opção desejada:') # Input permite solicitar uma informação ao usuário, faz um login em um sistema
    print('1- Cadastrar peça: \n' +
          '2- Consultar Peça: \n' +
          '3- Remover Peça: \n' +
          '4- Sair: \n' +
          '>>:' )
    opção = int(input('Digita a opção desejada:'))
    if opção == 1:  # Funsão if significa 'se', ela é execultada apenas se a condição for verdadeira
      registro = registro + 1
      cadastrar_peça(registro)
    elif opção == 2:  # O comando elif é utilizado quando queremos realizar a verificação de outra expressão caso a primeira validação seja falsa
      consultar_peça()
    elif opção == 3:
      remover_peça()

      print('Fim do atendimento!')

    else:  # O comando é usado para execultar um bloco de códgo, caso o resultado da expressão informada na instrução if seja falso1
      print('Opção Inválida. Tente novamente!:')
      continue  # Volta para o inicio do laço
  except ValueError:
    print('Digite apenas valores numéricos.')

# ---------------Fim de Main()---------------