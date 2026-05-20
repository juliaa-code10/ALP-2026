#objetivo: somar 10 numeros digitados pelo usuario
soma = 0
contador = 0
while contador < 10: 
    num = int(input("Digite um número para somar: "))
    soma += num
    contador += 1 
print("Sua soma é", soma)

# o contador deve começar definido como 0 
# a soma não deve estar no comando do while pq ela soma N + N e n numero de numeros digitados + 1 
# dnv o certo é < sem = pq o while deve rodar apenas se o contador for menor que N, o = n deve ser colocado, pq se esse while rodar, o numero de inputs vai ultrapassar o maximo anteriormente definido pelo usuario 
# o contador deve ser redefinido a cada numero digitado