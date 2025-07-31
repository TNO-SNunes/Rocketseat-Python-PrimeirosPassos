# Dicionário é uma coleção não ordenada de pares, chaves e valores

# Criando um dicionário de exemplo
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

print("Meu dicionário de exemplo:", pessoa)

#Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
pessoa["sobrenome"] = "Silva"
print("Cidade:", pessoa["cidade"])
print("Sobrenome:", pessoa["sobrenome"])