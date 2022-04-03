#Listas

notas = [8, 9, 10, 7.5, 4]

i = 0 # inicaliza na posição 0
total = 0
qtd = len(notas) # a quatidade de notas da lista
while i < qtd:
    total = total + notas[i] # acumula as notas no indice i = inicialização
    i = i + 1

print('O total das notas é: ',total)

media = total / qtd
print('A média de notas é: ', media)

