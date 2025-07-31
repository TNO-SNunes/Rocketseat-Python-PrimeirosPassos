# Tupla é uma coleção ordenada de elementos
# Depois de criada, não pode ser alterada

# Criando uma tupla de exemplo
minha_tupla = (1, 2, 2, 3, 4)
print("Minha Tupla:", minha_tupla)

print("Minha Tupla[0]:", minha_tupla[0])
print("Minha Tupla[2]:", minha_tupla[2])
print("Minha Tupla[-1]:", minha_tupla[-1])

# Método count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

indice = minha_tupla.index(3)
print("Indice da primeira ocorrencia do elemento 3:", indice)

