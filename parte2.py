#%%
#1. Elabore um algoritmo que contenha uma função chamada “Operacao”, 
# a qual recebe 2 parâmetros e, após as operações, imprima a soma da exponenciação, o resto da divisão do primeiro pelo segundo e a subtração do segundo pelo primeiro.

def Operacao(num1, num2):
  """
  Função que recebe dois números e realiza operações matemáticas.

  Argumentos:
    num1 (int ou float): O primeiro número.
    num2 (int ou float): O segundo número.

  Retorna:
    None: A função não retorna nenhum valor. 

  Exemplos:
    Operacao(5, 2) -> Imprime: 25 1 3
    Operacao(10, 3) -> Imprime: 1000 1 7
  """

  # Cálculo da exponenciação
  expo = num1 ** num2

  # Cálculo do resto da divisão
  resto = num1 % num2

  # Cálculo da subtração
  subtracao = num2 - num1

  # Impressão dos resultados
  print(f"{expo} {resto} {subtracao}")

# Exemplo de uso da função
Operacao(5, 2)  # Imprime: 25 1 3
Operacao(10, 3)  # Imprime: 1000 1 7
# %%
# #2.  	Um Banco contratou-lhe para implementar uma operação no seu sistema que aplica a taxa de rendimento sobre o valor aplicado na poupança. Logo, o supervisor de TI pediu para implementar uma função que receba dois parâmetros: “CapitalAplicado” e “TempoDeAplicacao:

# a) Implemente um algoritmo que solicite ao usuário o valor, em dinheiro, aplicado e a quantidade de meses em aplicação, considerando que a taxa de juros, por mês, é de 0,6022%. Ao final, imprima o valor aplicado inicialmente, a quantidade de meses e o valor final com o acréscimo de juros, em “Template String”, da seguinte forma: **A quantia de R$[CapitalAplicado] aplicada em [TempoDeAplicacao] meses, rendeu R$[ValorRendimento] a juros de [TaxaDeJuros].** Caso o valor informado for menor que 0 ou diferente de um número, o algoritmo deve apresentar uma alerta na tela com a seguinte mensagem: “Valor informado inválido! Por favor, informe o valor depositado na poupança”. Em seguida, solicite novamente ao cliente o valor aplicado na poupança e a quantidade de meses, até que o valor válido seja informado.

# b) Faça um algoritmo que, se o capital aplicado for maior ou igual a R$999,99 e menor ou igual R$10.000,00 e o tempo de aplicação for maior que 5 meses e menor que 12 meses, a taxa de rendimento deve ser 2%. O algoritmo deve solicitar ao cliente o valor do capital aplicado e o tempo de aplicação e, após a operação, o programa deve exibir na tela, o valor aplicado, a quantidade de meses em aplicação e o valor de rendimento em R$, utilizando o “Tamplate string”, da seguinte forma: **A quantia de R$[CapitalAplicado] aplicada em [TempoDeAplicacao] meses, rendeu R$[ValorRendimento].** Caso o valor informado for menor que 0 ou diferente de um número, o algoritmo deve apresentar uma alerta na tela com a seguinte mensagem: “Valor informado inválido! Por favor, informe o valor depositado na poupança”. Em seguida, solicite novamente ao cliente o valor aplicado na poupança e a quantidade de meses, até que o valor válido seja informado.

# c) Elabore um algoritmo que se o valor da poupança do cliente for maior que R$ 50.000,00 e menor ou igual R$100.000,00 e, se o tempo de aplicação for maior que 12 (meses) e menor ou igual a 24(meses), a taxa de juro de ser 5 %. Caso o tempo de aplicação for maior ou igual a 12 (meses) e menor ou igual a 24 (meses), a taxa de juros deverá ser de 10%. Por fim, imprima a mensagem na tela, em “Template String” da seguinte forma: “**A poupança de  R$[CapitalAplicado] aplicada em [TempoDeAplicacao] meses, rendeu R$[ValorRendimento]**”. Caso o valor informado for menor que 0 ou diferente de um número, o algoritmo deve apresentar uma alerta na tela com a seguinte mensagem: “Valor informado inválido! Por favor, informe o valor depositado na poupança!”. Em seguida, solicite novamente ao cliente o valor aplicado na poupança e a quantidade de meses, até que o valor válido seja informado.

def calcular_rendimento_poupanca(capital_aplicado, tempo_aplicacao):
  """
  Calcula o rendimento da poupança com taxa de juros fixa de 0,6022%.

  Argumentos:
    capital_aplicado (float): Valor aplicado na poupança.
    tempo_aplicacao (int): Tempo de aplicação em meses.

  Retorna:
    float: Valor final da poupança após o rendimento.
  """

  # Validação dos parâmetros
  if capital_aplicado <= 0 or not isinstance(capital_aplicado, (int, float)):
    raise ValueError("Valor informado inválido! Por favor, informe o valor depositado na poupança.")

  if tempo_aplicacao <= 0 or not isinstance(tempo_aplicacao, int):
    raise ValueError("Valor informado inválido! Por favor, informe a quantidade de meses em aplicação.")

  # Cálculo da taxa de juros mensal
  taxa_mensal = 0.006022

  # Cálculo do rendimento
  rendimento = capital_aplicado * (1 + taxa_mensal) ** tempo_aplicacao - capital_aplicado

  # Cálculo do valor final
  valor_final = capital_aplicado + rendimento

  # Exibição do resultado
  print(f"A quantia de R${capital_aplicado:.2f} aplicada em {tempo_aplicacao} meses, rendeu R${rendimento:.2f} a juros de {taxa_mensal * 100:.4f}%.")

# Solicitação de dados ao usuário
while True:
  try:
    capital_aplicado = float(input("Informe o valor aplicado na poupança: R$"))
    tempo_aplicacao = int(input("Informe a quantidade de meses em aplicação: "))
    calcular_rendimento_poupanca(capital_aplicado, tempo_aplicacao)
    break
  except ValueError as e:
    print(e)

def calcular_rendimento_poupanca_especial(capital_aplicado, tempo_aplicacao):
  """
  Calcula o rendimento da poupança com taxa de juros especial de 2%.

  Argumentos:
    capital_aplicado (float): Valor aplicado na poupança.
    tempo_aplicacao (int): Tempo de aplicação em meses.

  Retorna:
    float: Valor final da poupança após o rendimento.
  """

  # Validação dos parâmetros
  if capital_aplicado <= 0 or not isinstance(capital_aplicado, (int, float)):
    raise ValueError("Valor informado inválido! Por favor, informe o valor depositado na poupança.")

  if tempo_aplicacao <= 0 or not isinstance(tempo_aplicacao, int):
    raise ValueError("Valor informado inválido! Por favor, informe a quantidade de meses em aplicação.")

  # Cálculo da taxa de juros mensal
  if 999.99 <= capital_aplicado <= 10000.00 and 5 < tempo_aplicacao < 12:
    taxa_mensal = 0.02
  else:
    taxa_mensal = 0.006022

  # Cálculo do rendimento
  rendimento = capital_aplicado * (1 + taxa_mensal) ** tempo_aplicacao - capital_aplicado

  # Cálculo do valor final
  valor_final



# %%
# 3.  O seu primo pretende desenvolver um jogo de acerto para que o filho dele possa brincar, mas como ele não possui o conhecimento em programa, solicitou a sua ajuda, tendo em conta que você havia lhe dito que está fazendo o programa trilhas e aprendendo sobre o algoritmo e lógica de programação. Neste contexto, ele definiu as funcionalidades que gostaria que o jogo tenha:

# - O programa deve criar um número secreto e solicitar ao usuário que chute um número entre 20 e 30;
# - Se o número secreto for igual ao de chute, o programa deve exibir uma mensagem de acerto;
# - Se o número secreto for diferente do número de chute, o programa deve exibir uma mensagem de erro, solicitando novamente um número entre 20 e 30;
# - O programa deve oferecer 3 tentativas para o chute e, por fim, exibir uma mensagem de tentativas esgotadas e finalizar.

import random

# Gera um número secreto aleatório entre 20 e 30
numero_secreto = random.randint(20, 30)

# Contador de tentativas
tentativas = 3

while tentativas > 0:
  # Solicita o chute do jogador
  chute_jogador = int(input("Digite um número entre 20 e 30: "))

  # Verifica se o chute está dentro do intervalo válido
  if 20 <= chute_jogador <= 30:
    # Verifica se o jogador acertou o número secreto
    if chute_jogador == numero_secreto:
      print("Parabéns! Você acertou o número secreto!")
      break
    else:
      # Se o jogador errou, diminui o contador de tentativas e exibe uma mensagem de erro
      tentativas -= 1
      if tentativas == 0:
        print("Você esgotou suas tentativas. O número secreto era", numero_secreto)
      else:
        print("Você errou! Tente novamente. Você ainda tem", tentativas, "tentativas.")
  else:
    # Se o chute estiver fora do intervalo válido, exibe uma mensagem de erro
    print("Número inválido. Digite um número entre 20 e 30.")

# %%
