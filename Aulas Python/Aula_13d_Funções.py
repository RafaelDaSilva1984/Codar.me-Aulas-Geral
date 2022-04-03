def calcular_conta(consumo, taxa_serviço, desconto_fidelidade):
    if taxa_serviço == 0 and desconto_fidelidade == 0:
        return consumo
    #serviço = consumo * taxa_serviço
    #desconto = consumo * desconto_fidelidade
    #valor = consumo + serviço
    #valor = valor - desconto
    #return valor
#valor = calcular_conta(consumo=100, taxa_serviço=0.1, desconto_fidelidade=0.05)
#print('O valor do serviço é: ', valor)

print(calcular_conta(consumo=100, taxa_serviço=0 , desconto_fidelidade=0))
