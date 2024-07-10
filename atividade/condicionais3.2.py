usuario_certo = "sofhia"
senha_certa = "12345"

usuario = input("Usuário:")
senha = input("Senha:")

match usuario == usuario_certo and senha == senha_certa:
    case True:
        print("Login realizado.")
    case False: 
        print("Tente novamente.")


 
    