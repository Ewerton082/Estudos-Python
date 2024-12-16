""" Criar um programa que avallia um financiamento de uma casa """


def avaliacao_casa(valor_casa: float, salario: float, duracao_anos: int):
    PERCENTUAL = 30

    mensalidade = valor_casa / (duracao_anos * 12)
    compromentimento = (salario * PERCENTUAL / 100)

    if mensalidade < compromentimento:
        dados_finais = {"valor_casa": valor_casa, "valor_parcela": mensalidade,
                        "salario": salario, "compromentimento" : compromentimento,
                        "status": "\033[92mAPROVADO\033[0m", "parcelas": duracao_anos * 12}
        return dados_finais
    else:
        dados_finais = {"valor_casa": valor_casa, "valor_parcela": mensalidade,
                        "salario": salario, "compromentimento": compromentimento,
                        "status": "\033[91mNEGADO\033[0m", "parcelas": duracao_anos * 12}
        return dados_finais

casa = float(input("Qual o valor da casa que deseja financiar? R$ ").strip().replace(',', '.'))
dinheiro = float(input("Qual o valor do seu salário? R$ ").strip().replace(',', '.'))
tempo = int(input("Em quantos anos você deseja pagar? ").strip())
ava_dict = avaliacao_casa(casa, dinheiro, tempo)

print(f"O valor da casa é de {ava_dict['valor_casa']:.2f} R$ para ser pago em {ava_dict['parcelas']} vezes o valor de {ava_dict['valor_parcela']:.2f}")
print(f"\n O Financiamento foi {ava_dict['status']}")
