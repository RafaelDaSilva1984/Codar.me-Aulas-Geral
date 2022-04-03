
usuarios = {'Alice','Bob'} # Chaves declara conjuntos
usuarios2 = set(['Alice','Bob']) # declara uma lista em un conjunto
#conjuntos não podem ter valores repetidos
# não garante ordenação de inserção sem ordem
print(usuarios)
usuarios.add('Bob')
print(usuarios)
usuarios.add('Carlos')
print(usuarios)

# para remover duplicatas de dados de uma lista
#set
usuarios2 = ['alice', 'bob', 'alice']
usuariosunicos = set(usuarios2)
print(usuariosunicos)

#union
usuarios = {'Alice','Bob', 'Carlos'}
usuarios2 = set(['Alice', 'Bob', 'Lucas'])
print(usuarios.union(usuarios2)) # une os valores em conjunto
e_igual = usuarios.union(usuarios2) == usuarios | usuarios2 # | é comando igual a union
print(e_igual)

#intersection
usuarios = {'alice', 'bob', 'calos'}
usuarios3 = {'alice','bob', 'lucas'}
print(usuarios.intersection(usuarios3))
e_igual = usuarios.intersection(usuarios3) == usuarios & usuarios3 # intersectio == &
print(e_igual)

#difference
usuarios = {'alice', 'bob', 'calos'}
usuarios3 = {'alice','bob', 'lucas'}
print(usuarios.difference(usuarios3))
e_igual = usuarios.difference(usuarios3) == usuarios - usuarios3 # intersectio == &
print(e_igual)