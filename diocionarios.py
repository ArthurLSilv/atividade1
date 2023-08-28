print("1")

DicionarioVazio = {}
DicionarioVazio['nome'] = "Arthur"
DicionarioVazio['idade'] = "17"

print(DicionarioVazio)

print("\n2")

dicionario1 = {'nome':'Arthur', 'idade':17,'cidade':'Guarapuava'}
print(dicionario1)

print("\n3")

dicionario2 = {'bolacha':5.90,'leite':6.50,'miojo':3.00}
print(dicionario2)

print("\n4")

Capitais = {'Paraná':'Curitiba','Bahia':'Salvador','Acre':'Rio Branco'}
estado_digitado = input("Digite um Estado: ")
capital = Capitais.get(estado_digitado)

if capital:
    print(f"O estado digitado foi: {estado_digitado} e sua capital é {capital}")

else:
    print("estado nao encontrado no dicionario")

print("\n5")

dicionario_populaçao = {'Guarapuava':182644, 'Curitiba':1773733, 'São Paulo':11451245,'Rio de Janeiro':6211423,'Campina do Simão':3859}

maior = 0

for cidade,populaçao in dicionario_populaçao.items():
    if populaçao > maior:
        maior = populaçao
        cidade_maior_populaçao = cidade

print("A cidade com maior população é:", cidade_maior_populaçao,"com",maior,"habitantes")

print("\n6")

dicionarioCalorias = {'ovo':107,'bolacha':146,'banana':100}
comidaDigitada = input("Digite um alimento: ")
caloria = dicionarioCalorias.get(comidaDigitada)

if caloria:
    print(f"A comida digitada foi {comidaDigitada} e contém {caloria} calorias")

else:
    print("alimento nao encontrado no dicionario!!")

print("\n7")

dicionarioAnimais = {'macaco':'mamifero', 'tucano':'ave','lagarto':'reptil','cachorro':'mamifero','galinha':'ave'}
print(dicionarioAnimais.keys())

print("\n8")

dicionarioPaises = {'Brasil':'bandeira','Russia':'bandeira','Espanha':'bandeira','Portugal':'bandeira','Argentina':'bandeira'}
print(dicionarioPaises.keys())

print("\n9")

dicionarioFrutas = {'maça':'vermelha','banana':'amarela','uva':'roxa','laranja':'laranja','pera':'verde'}

for chave,valor in dicionarioFrutas.items():
    print(chave,valor)

print("\n10")

dicionarioJogos = {'volei':12,'futsal':10,'futebol':22}
jogodigitado = input("Digite um jogo: ")
jogo = dicionarioJogos.get(jogodigitado)

if jogo:
    print(f"O jogo é {jogodigitado} e precisa de {jogo} jogadores")

else:
    print("Jogo nao encontrado no dicionario!!")
