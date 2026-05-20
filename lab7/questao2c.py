#objetivo: imprimir o maior numero digitado pelo usuario
maior = float('-inf')
contador = 0
while contador < 10: 
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num
    contador += 1
print('O maior número é', maior)


# o certo nesse caso é -inf pq é o menor numero possivel, ent no inicio do programa o maior numero vai ser o menor possivel e vai sendo redefinido pelo usuario ao longo do codigo
# o contador tem q ser definido no inicio do codigo como 0 
# a soma dnv n é certo pq ela soma N + N e n numero de numeros digitados + 1  
# o contador tem q ser redefinido (soma 1) a cada numero digitado 
