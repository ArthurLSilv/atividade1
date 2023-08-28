print("\n1")

conjunto = {1,2,3,4,5,6,7,8,9,10}
print(conjunto)

conjunto1 = {1,2,3,4,5}
conjunto2 = {3,4,5,6,7}

print("\n2")

print(conjunto1.union(conjunto2))
print(conjunto1.intersection(conjunto2))
print(conjunto1.symmetric_difference(conjunto2))

print("\n3")

conjunto_vogais = {'a','e','i','o','u'}

palavra = input("Digite uma palavra: ")

for i in palavra:
    if i in conjunto_vogais:
        print(i)

print("\n4")

conjunto_fruta1 = {'banana','abacate','uva'}
conjunto_fruta2 = {'uva','maça','pera'}

semelhantes = conjunto_fruta1.intersection(conjunto_fruta2)

print(semelhantes)

print("\n5")

conjuntoInteiros = {11,22,3,46,578,69}
maior = 0
menor = 0


for i in conjuntoInteiros:
    if i >= maior:
        maior = i
        menor = i

    elif i <= menor:
        menor = i

print("O maior numero é:", maior)
print("O menor numero é:", menor)

print("\n6")

conjunto_ArcoIris = {'vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'anil', 'violeta'}

cor = input("Digite uma cor")

if cor in conjunto_ArcoIris:
    print("Contem essa cor no arco iris")

else:
    print("Nao contem essa cor no arco irir")

print("\n7")

conjuntoSemana = {'Segunda','terca','quarta','quinta','sexta','sabado','domingo'}

conjuntoSemana.remove('Segunda')
conjuntoSemana.remove('terca')
conjuntoSemana.remove('quarta')
conjuntoSemana.remove('quinta')
conjuntoSemana.remove('sexta')


print(conjuntoSemana)

print("\n8")

conjunto1a20 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
conjuntosPares = {2,4,6,8,10}

diferenca = conjunto1a20.difference(conjuntosPares)

print(diferenca)

print("\n9")

conjuntoNotas = {6.4,7.8,8.9}

media = sum(conjuntoNotas) / 3

if media > 7:
    print("APROVADO!")

else:
    print("REPROVADO!")

print("\n10")

conjuntosPrimos = {2,3,5,7,11,13,17,19}

numeroUsuario = int(input("Digite um numero: "))

if numeroUsuario in conjuntosPrimos:
    print("Este numero esta no conjunto!")

else:
    print("Numero nao encontrado")
