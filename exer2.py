n = int(input("Digite um número: "))

if n == 0 or n == 1:
    print(f"Número {n} esta na sequência de Fibonnaci!")
else:
    n1 = 1
    n2 = 2

    while n > n2:
        n1, n2 = n2, n1 + n2

    if n == n2:
        print(f"Número {n} esta na sequência de Fibonnaci!")
    else:
        print(f"Número {n} não esta na sequência de Fibonnaci!")
