def inverter_palavra(palavra):
    palavra_invertida = ""

    for letra in palavra:
        palavra_invertida = letra + palavra_invertida

    return palavra_invertida


s = "Pneumoultramicroscopicossilicovulcanoconiótico"
print(inverter_palavra(s))

print(inverter_palavra(input("Digite uma palavra: ")))
