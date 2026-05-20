import random
n = random.randint(1, 10)
chances = 5
while chances>0: 
    N = float(input("Escolha um número de um a 10: "))
    chances -= 1
    if N==n:
        print("Parabéns! Você acertou =)")
        break
    if chances == 0:
        if N != n:
            print("Você errou =(")
            break
print(n)
