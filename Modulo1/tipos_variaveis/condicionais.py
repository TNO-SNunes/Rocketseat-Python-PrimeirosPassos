# Condicionais
# if, elif e else

#exemplo de "IF"

idade = int(input ("Quantos anos você tem?"))
print("Exemplo de comando if")
    # >= - maior ou igual
#if idade >= 18:
    #print("Você é maior de idade.")
    
    # == - diferença, comparar com valor exato
#if idade == 19:
    #print("Você tem 19 anos.")

    # <= menor ou igual
#if idade < 18:
    #print("Você é menor de idade.")

    # diferença
#if idade != 10:
    #print("Você não tem 10 anos.")

if idade >= 18:
    print("Você é maior de idade.")
elif idade>= 12:
    print("Você é um adolescente.")
else:
    print("Você é menor de idade.")

mensagem = "Pode tirar CNH." if idade >= 18 else "Você não pode tirar CNH."
print(mensagem)

