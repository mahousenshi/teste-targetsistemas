import json


def analisar_faturamento(caminho_json):
    # 1. Ler dados de um arquivo JSON
    with open(caminho_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    # 2. Filtrar somente dias com faturamento > 0 (ignorando zero)
    faturamentos_validos = [item['valor'] for item in dados if item['valor'] > 0]

    # Se não houver valores > 0, não há o que analisar
    if not faturamentos_validos:
        print("Não há faturamentos válidos (diferentes de zero) para análise.")
        return

    # 3. Cálculo do menor, maior e média (entre os faturamentos não zerados)
    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)
    media_faturamento = sum(faturamentos_validos) / len(faturamentos_validos)

    # 4. Número de dias acima da média
    dias_acima_da_media = sum(1 for valor in faturamentos_validos if valor > media_faturamento)

    # 5. Exibir resultados
    print(f"Menor valor de faturamento no mês (desconsiderando 0): {menor_faturamento}")
    print(f"Maior valor de faturamento no mês (desconsiderando 0): {maior_faturamento}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")


caminho_arquivo = analisar_faturamento("teste.json")
