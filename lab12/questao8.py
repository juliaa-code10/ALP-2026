import datetime
nome1 = input("nome da pessoa 1 ")
nome2 = input("nome da pessoa 2 ")
data1 = int(input("data de nascimento da pessoa 1 "))
data2 = int(input("data de nascimento da pessoa 2 "))
datetime.datetime.strptime(data, "%d/%m/%Y")
hoje = datetime.datetime.now()
dia = hoje.day
mes = hoje.month
ano = hoje.year

