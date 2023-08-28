print(1)

tupla1 = (1,2,3,4,5)
print(tupla1)

print("\n2")

tupla2 = ('BRASIL','ARGENTINA','EQUADOR')
print(tupla2[1])

print("\n3")

tupla3 = ('Valor da refeiçao = R$30.00 ', 'taxa de serviço = R$10.00', 'valor total = R$40.00')

print(tupla3[0])
print(tupla3[1])
print(tupla3[2])

print("\n4")

tupla4 = ('Arthur','Hansen','Julio','Andre','Matheus')

numeroDigitado = int(input("Digite um numero de 1 a 5: "))

if 1 <= numeroDigitado <= 5:
    nomeCorrespondente = tupla4[numeroDigitado - 1]
    print("O nome correspondente é: ", nomeCorrespondente)
else:
    print("Numero fora do intervalo valido")

print("\n5")

tupla5 = (7,8.5,10)
media = sum(tupla5) / 3

print(media)

print("\n6")

tupla6 = ('vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'anil', 'violeta')
cor = input("Digite uma cor")

if cor in tupla6:
    print("Contem essa cor no arco iris")
else:
    print("Nao contem essa cor no arco irir")

print("\n7")

tupla7 = (21.9,10.6,33.5,32.7,12.0,19.5,18.1)

temperatura_maxima = max(tupla7)
temperatura_minima = min(tupla7)

print("Temperatura máxima da semana:", temperatura_maxima)
print("Temperatura mínima da semana:", temperatura_minima)

print("\n8")

tupla8 = (("Maçã","Vermelha"), ("Laranja","Laranja"), ("Banana","Amarela"), ("Pera","Verde"), ("Uva","Roxa"))
for fruta, cor in tupla8:
    print(fruta, ":", cor)

print("\n9")

tupla9 = (1,2,3,4,5,6,7,8,9,10)
tupla9_ = (5,6,7,8,9,10,11,12,13,14,15)

tupla99 = set(tupla9)
tupla100 = set(tupla9_)

intersecao = tupla99.intersection(tupla100)

print(intersecao)

print("\n10")

tupla10 = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
tupla10_ = ('a','e','i','o','u')

ConjuntoLetras = set(tupla10)
conjuntoVogais = set(tupla10_)

diferenca = ConjuntoLetras.difference(conjuntoVogais)

print(diferenca)
