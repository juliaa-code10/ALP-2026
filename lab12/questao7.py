import datetime
data1 = input("Digite data de nascimento da pessoa 1")
data2 = input("Digite data de nasciemtno da pessoa 2")
data1 = datetime.datetime.strptime(data_str, "%d/%m/%Y")
data2 = datetime.datetime.strptime(data_str, "%d/%m/%Y")
if data1>data2:
    print("Pessoa 2 é mais velha")
else:
    print("Pessoa 1 é mais velha")
if data1==data2:
    print("Pessoa 1 e pessoa 2 tem a mesma idade")
