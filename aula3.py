# lacos de repeticao
# for
# white


# quantidade = int(input("Digite a quantidade de notas: "))

# somaDaNota = 0
# for i in range(quantidade):
#     somaDaNota += int(input("Digite sua nota: "))

# media = somaDaNota / quantidade
# print(f"A média é de {media} ") 
    
# contador = 0
# while contador < 15:
#     print(contador)
#     contador += 1

# lista_de_compras = ["maça", "carne", "monster", "café"]

# for i in lista_de_compras:
#     print(i)


# o usuario escolhe um número para ser 
# feito a tabuada sendo operado do 1 ao 10
# e voce imprime essa tabuada 
# ex : 10 1 x = 10; 2 x 10 = 20 ... \n

tabuada = int(input("Digite um numero para descobrir a tabuada: "))

for i in range(1,11):
    resultado = i * tabuada 
    print(f"{i} x {tabuada} = {resultado}")
    