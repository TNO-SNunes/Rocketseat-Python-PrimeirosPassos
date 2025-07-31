
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

print("\nFor utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print ("\nFor utilizando dicionário - chaves")
for chave in pessoa.keys():
    print(chave)

print("\nFor utilizando dicionario - valores")
for valor in pessoa.values():
    print(valor)

    print("\nFor utilizando dicionario - items")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# range(): intervalo numérico
# [0,1,2,3,4,5,6,7,8,9]
print("\n Utilizando a função range()")
for numero in range(5):
    print("Numero:", numero)

# len() - automaticamente muda de acordo com o aumento da lista
print("\n Utilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)

# enumerate() - permite uso de lista
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")
