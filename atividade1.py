altura = float(input("Digite a altura em metros "))
largura = float(input("Digite a largura em metros "))
                
area = altura * largura

quantidade_de_lata = area / 2

valor_total = quantidade_de_lata * 50

print("A area da parede é de: ", area,
        "\nA quantidade de latas " \
        "que será usada é de:  ", quantidade_de_lata,
        "\nValor total: ", valor_total)