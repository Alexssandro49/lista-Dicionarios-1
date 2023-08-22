#encoding: latin-1
pessoas={'João':32,'Suzan':42,'Leia':52,'José':22,'Raissa':34,'Pedro':25,'Carlos':19,'Beto':56,'Tania':60,'Vitor':12}
print(pessoas)
nome=input("Digite um nome: ")
if nome in pessoas.keys():
    print(str(pessoas[nome])+" anos")
else : print("Nome não encontrado!")
continuar=input("Deseja atualizar a idade de alguém? [S/N]: ")
if continuar=="S":
    nome=input("Nome de quem deseja atualizar: ")
    idade= input("Idade qual deseja inserir: ")
    if nome in pessoas.keys():
        pessoas[nome]=idade
        print(nome+" "+str(pessoas[nome])+" anos, atualizado com sucesso!")
    else:print("Nome não encontrado!")
continuar= input("Deseja remover alguém da lista? [S/N]: ")
if continuar=="S":
    nome=input("Nome de quem deseja Remover: ")
    if nome in pessoas.keys():
        pessoas.pop(nome)
        print("Atualizado com sucesso!")
        print(pessoas)
    else:print("Nome não encontrado!")
totalPessoas=len(pessoas)
print("Total de pessoas atualmente na lista: "+ str(totalPessoas))
mediaIdades=(sum(pessoas.values()))/totalPessoas
print("Média da idade das pessoas atualmente na lista: "+ str(mediaIdades))
MaiorIdade=max(pessoas, key=pessoas.get)
print("A pessoa mais velha atualmente na lista é "+MaiorIdade+" com "+ str(pessoas[MaiorIdade])+" anos")
MenorIdade=min(pessoas, key=pessoas.get)
print("A pessoa mais nova atualmente na lista é "+MenorIdade+" com "+ str(pessoas[MenorIdade])+" anos")
Nomes=[nome for nome in pessoas if nome[0].upper() == 'J']
print("Pessoas cujo nome inicia com a letra j: "+ str(Nomes))




