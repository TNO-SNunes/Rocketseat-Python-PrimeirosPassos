
# Módulos são arquivos com definições e e instruções que podem ser reutilizadas por outros programas.

print("Exemplo de importação de módulo padrão: ")
# import math
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"Resultado: {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado")

#import meu_modulo
from meu_modulo import saudacao, dobro

mensagem = saudacao("Sergio")
resultado_dobro = dobro(5)

print(mensagem)
print(f"O dobro de 5 é: {resultado_dobro}")