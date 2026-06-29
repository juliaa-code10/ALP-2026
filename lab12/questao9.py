import datetime
hoje = datetime.datetime.now()
data_prova = datetime.datetime(2026, 7, 14)
diferenca = data_prova - hoje
if diferenca.days>0:
    print("faltam", diferenca.days, "dias")
if diferenca.days<0:
    print("a prova já passou a",diferenca.days,"dias")