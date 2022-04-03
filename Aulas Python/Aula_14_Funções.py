def calcular_conta(consumo, taxa_serviço=0.1, desconto_fidelidade=0):#valor padrão, os argumetos val padrão sempre vem depois sem val padrão
    if taxa_serviço == 0 and desconto_fidelidade == 0:
        return consumo

    serviço = consumo * taxa_serviço
    desconto = consumo * desconto_fidelidade
    valor = consumo + serviço
    valor = valor - desconto
    return valor

print(calcular_conta(consumo=100))