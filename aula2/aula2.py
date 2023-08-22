#encoding: latin-1
pessoas={'Jo�o':32,'Suzan':42,'Leia':52,'Jos�':22,'Raissa':34,'Pedro':25,'Carlos':19,'Beto':56,'Tania':60,'Vitor':12}
print(pessoas)
nome=input("Digite um nome: ")
if nome in pessoas.keys():
    print(str(pessoas[nome])+" anos")
else : print("Nome n�o encontrado!")
continuar=input("Deseja atualizar a idade de algu�m? [S/N]: ")
if continuar=="S":
    nome=input("Nome de quem deseja atualizar: ")
    idade= input("Idade qual deseja inserir: ")
    if nome in pessoas.keys():
        pessoas[nome]=idade
        print(nome+" "+str(pessoas[nome])+" anos, atualizado com sucesso!")
    else:print("Nome n�o encontrado!")
continuar= input("Deseja remover algu�m da lista? [S/N]: ")
if continuar=="S":
    nome=input("Nome de quem deseja Remover: ")
    if nome in pessoas.keys():
        pessoas.pop(nome)
        print("Atualizado com sucesso!")
        print(pessoas)
    else:print("Nome n�o encontrado!")
totalPessoas=len(pessoas)
print("Total de pessoas atualmente na lista: "+ str(totalPessoas))
mediaIdades=(sum(pessoas.values()))/totalPessoas
print("M�dia da idade das pessoas atualmente na lista: "+ str(mediaIdades))
MaiorIdade=max(pessoas, key=pessoas.get)
print("A pessoa mais velha atualmente na lista � "+MaiorIdade+" com "+ str(pessoas[MaiorIdade])+" anos")
MenorIdade=min(pessoas, key=pessoas.get)
print("A pessoa mais nova atualmente na lista � "+MenorIdade+" com "+ str(pessoas[MenorIdade])+" anos")
Nomes=[nome for nome in pessoas if nome[0].upper() == 'J']
print("Pessoas cujo nome inicia com a letra j: "+ str(Nomes))




