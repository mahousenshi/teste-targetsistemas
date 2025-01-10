lugares = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53,
}

total = sum(lugares.values())

for lugar, valor in lugares.items():
    print(f"Estado: {lugar} | Porcento: {valor / total * 100:.2f}%")
