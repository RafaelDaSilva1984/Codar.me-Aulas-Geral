#Listas
notas = [8, 10, 8.5]
#        0   1  2

notas.append(9) # adiciona valor a lista na última posição
print(notas)
notas.sort() # ordena os valores da lista do menor para o maior
print(notas) 
notas.sort(reverse=True) # Inverse a lista na decrescente
print(notas) 
notas.pop() # elimina o último valor da lista
print(notas)
notas.insert(0, 8) # insere valor na posiçao 0 ( o primeiro número é a posição e segunda o valor adicionar)
print(notas)
notas.pop(0) # elimina o valor na posição indicada
print(notas)