#Declaração de variáveis
nome_completo = "Sergio Gama Nunes"
nome = "Sergio"
sobrenome = "Gama"

nome_completo_aspas = """Sergio 
Gama 
Nunes"""

nome_completo_quebra = "Sergio \
Gama \
Nunes"

# Exibindo variáveis
# print(nome)
# print(sobrenome)
# print(nome_completo)
# print(nome_completo_aspas)
# print(nome_completo_quebra)

# Formatação 
print("Nome completo(1a forma):", nome_completo)
print("Nome completo(2a forma):" + nome_completo)
print("Nome completo(3a forma):" + "Sergio" + "Gama Nunes")
print("Nome completo(4a forma):" + "Sergio", "Gama Nunes")
print("Nome completo(5a forma):", nome_completo_aspas)
print("Nome completo(6a forma):", nome_completo_quebra)
print("Nome completo(7a forma): %s" % nome_completo)
print("Nome completo(8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo(9a forma): {nome} {sobrenome}")
print("Nome completo(10a forma): {} {}" .format(nome, sobrenome))