#objetivo do código: contar qnts numeros impares o usuario digitou
N = int(input("Quantos números quer digitar?"))
contador = 0
impares = 0

while contador < N:
    num = int(input("Digite um número: "))
    contador += 1
    if num % 2 != 0:
        impares += 1
print(f"Quantidade de ímpares entre 1 e {num}: {impares}")
# o contador deve começar no programa como 0, pq eles ainda n recebeu nenhum input de nenhum
# o while deve rodar apenas se o contador for menor que N, o = n deve ser colocado, pq se esse while rodar, o numero de inputs vai ultrapassar o maximo anteriormente definido pelo usuario
#  o contador deve ser redefinido somando 1 a cada input recebido
