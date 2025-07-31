
def add_contato(contatos, nome_contato, tel_contato, mail_contato):
    contato = {"nome": nome_contato, "telefone": tel_contato, "email": mail_contato, "favorito": False}
    contatos.append(contato)
    print(f"O {nome_contato} foi adicionado à lista de contatos!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "☆" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        print(f"{indice}. [{status}] {nome_contato}")

def ver_det_contatos(contato, tel_contato, mail_contato):
    print(f"\nContato {nome_contato} detalhado")
    print(f"Tel:{tel_contato} - Email:{mail_contato}")

def att_contato(contatos, indice_contato, novo_nome, novo_tel, novo_mail):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome
        contatos[indice_contato_ajustado]["telefone"] = novo_tel
        contatos[indice_contato_ajustado]["email"] = novo_mail
        print(f"Contato {indice_contato} atualizado para {novo_nome}, Tel:{novo_tel}, Email:{novo_mail}")

def favoritar_contato(contatos, indice_contato):
    if 0 <= indice_contato < len(contatos):
            contatos[indice_contato]["favorito"] = not contatos[indice_contato]["favorito"]
            estado = "favoritado" if contatos[indice_contato]["favorito"] else "removido dos favoritos"
            print(f"Contato '{contatos[indice_contato]["nome"]}' foi {estado}.")

def listar_favoritos(contatos):
    favoritos = [c for c in contatos if c["favorito"]]
    if not favoritos:
        print("Nenhum favorito encontrado.")
        return
    print("\n☆ Contatos Favoritos:")
    for contato in favoritos:
        print(f"- {contato["nome"]} (Telefone: {contato["telefone"]}, Email: {contato["email"]})")

def deletar_contato(contatos):
    if not contatos:
        print("\nA lista de contatos está vazia.")
        return
    if 0 <= indice_contato < len(contatos):
            nome = contatos[indice_contato]['nome']
            del contatos[indice_contato]
            print(f"O Contato '{nome}' foi deletado com sucesso.")
        
contatos = []

while True:
    print("\nMenu do Gerenciador de Contatos:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Ver detalhes dos contatos")
    print("4. Atualizar contatos")
    print("5. Favoritar contatos")
    print("6. Listar Favoritos")
    print("7. Deletar contatos")
    print("8. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato: ")
        tel_contato = input("Digite o telefone do contato: ")
        mail_contato = input("Digite o e-mail do contato: ")
        add_contato(contatos, nome_contato, tel_contato, mail_contato)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        detalhe_contato = input("Digite o número do contato para detalhar: ")
        ver_det_contatos(contatos, tel_contato, mail_contato)
    
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = int(input("Digite o número do contato para atulizar: "))
        novo_nome = input("Digite o novo nome: ")
        novo_tel = input("Digite o telefone:")
        novo_mail = input("Digite o novo email: ")
        att_contato(contatos, indice_contato, novo_nome, novo_tel, novo_mail)

    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = int(input("Digite o número do contato para (des)favoritar: ")) - 1
        favoritar_contato(contatos, indice_contato)

    elif escolha == "6":
        listar_favoritos(contatos)


    elif escolha == "7":
        ver_contatos(contatos)
        indice_contato = int(input("Digite o número do contato que deseja deletar: ")) - 1
        deletar_contato(contatos)

    elif escolha == "8":
        break

print ("Agenda fechada, volte quando quiser!")
