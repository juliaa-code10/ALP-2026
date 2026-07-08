def exibir_mensagem():
    print('a info1a é top')
def exibir_elogio(nome):
    nome = input('seu nome: ')
    print(nome, 'é top')
def classificar_nota(valor)
    nota = int(input('escolha valor int, referente a nota '))
    if nota > 60:
        print('aprovado')
    else: 
        print('reprovado')
def contagem_regressiva(valor):
    import time
    valor = int(input('valor int positivo: '))
    print(valor)
    while valor > 0:
        valor = valor - 1 
        print(valor)
        time.sleep(1)
def roleta(numero):
    import random
    numero = random.randint(1,36)
    if numero % 2 == 0:
        print(numero, 'preto')
    elif numero % 2 != 0:
        print(numero, 'vermelho')