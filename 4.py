try:
    usuario = input("Digite seu nome: ")
    senha = input("Digite a senha: ")

    if usuario == "Olegario" and senha == "234":
        print("Bem-vindo, Olegario!")
        print("👌👌👌")
    else:
        print("Usuário ou senha incorretos. Tente novamente ")
        print("🤐🤐🤐")
except:
    print("Deu errado")