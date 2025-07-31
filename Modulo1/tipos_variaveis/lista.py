# Declaracao

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo a lista individual
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])

# Fatiando/Slice lista
print("minha_lista[1:7]:", minha_lista[1:7])
# Lista exibida no intervalo escolhido, sempre lembrar de adiciona 1 à valor do alvo final.
print("minha_lista[:6]", minha_lista[:6])
print("minha_lista[:2]", minha_lista[:2])


# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append (6):", minha_lista)

# Método index
indice = minha_lista.index(6)
print("Inidice do elemento 6:", indice) 

# Método insert: Insere um elemento em um índice específico   
minha_lista.insert(2, 10)
print("Após insert (2,10)", minha_lista)  

# Método pop
elemento_removido = minha_lista.pop(3)
print("Elemento removido(3):", elemento_removido)
print("Após pop(3):", minha_lista)

# Método remove - remove o elemento com valor especificado
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

# Método sort - organizar lista em ordem crescente
minha_lista.sort()
print("Após sort():", minha_lista)


