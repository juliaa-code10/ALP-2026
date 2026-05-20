print("Cardápio:  1. Açaí 300ml - R$ 12   2. Mousse - R$ 6,50  3. Salada de frutas - R$ 10  4. Fechar a conta")
preço_final = 0
preço1=12
preço2=6,5 
preço3=10
opcao = int(input("Escolha oq vc deseja: "))
while opcao != 4:
    if opcao==1 or opcao==2 or opcao==3:
        if opcao==1:
            preço_final+=preço1
        if opcao==2: 
            preço_final+=preço2
        if opcao==3:
            preço_final+=preço3
    if opcao==4:
        print("Fechar conta")
        print(preço_final)
        break
            