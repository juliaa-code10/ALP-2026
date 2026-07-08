def olá(nome, gênero):
    nome = input("nome da pessoa: ")
    gênero = input("qual seu gênero: ")
    if gênero == 'masculino':
        return f"Olá, {nome}, bem-vinda!"
    if gênero == 'femenino':
        return f"Olá, {nome}, bem-vinda!" 
    if gênero == 'neutro':
        return f"Olá, {nome}, boas vindas!"
        
    