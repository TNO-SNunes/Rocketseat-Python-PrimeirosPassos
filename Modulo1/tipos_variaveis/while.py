# while - tipo de loop utilizado para repetir bloco de código enquanto uma condição for verdadeira
print("Exemplo de whie")
contador = 0 
while contador < 5:
    print("Contagem:", contador)
    contador = contador + 1
    # Pode-se utilizar contador +=1 / -=1
    if contador == 5:
        break

print("Programa finalizado.")
