def validate_email(email):
    return "@gmail.com" in email


def check_existing_email(email):
    try:
        with open("database.txt", "r") as file:
            data = file.readlines()
            emails = [data[i].strip()[7:] for i in range(2, len(data), 4)]  # Obtém todos os emails do arquivo
            return email in emails
    except FileNotFoundError:
        return False


def cadastrar():
    print("Cadastro:")
    name = input("Digite seu nome: ")
    nickname = input("Digite seu apelido: ")
    name = name.capitalize()
    nickname = nickname.capitalize()
    print(f"Seu nome é {name} {nickname}")

    while True:
        email = input("Digite seu email: ")
        if not validate_email(email):
            print("""
            ERRO!
            ESSE EMAIL É INVÁLIDO
            """)
        elif check_existing_email(email):
            print("""
            ERRO!
            ESTE EMAIL JÁ ESTÁ CADASTRADO. POR FAVOR, FAÇA LOGIN.
            """)
        else:
            print(f"Seu email é {email}")
            save_to_database(name, nickname, email)
            break


def iniciar():
    print("\nIniciar sessão:")
    email = input("Digite seu email: ")

    if check_existing_email(email):
        with open("database.txt", "r") as file:
            data = file.readlines()
            index = [data[i].strip()[7:] for i in range(2, len(data), 4)].index(email)
            name = data[index * 4 + 1].strip()[9:]
            print(f"Bem-vindo de volta, {name}!")
    else:
        print("Usuário não cadastrado. Por favor, faça o login ou cadastre-se.")
        return False  # Indica que o usuário não foi encontrado


def save_to_database(name, nickname, email):
    with open("database.txt", "a") as file:
        file.write(f"Name: {name}\nNickname: {nickname}\nEmail: {email}\n\n")


def main():
    while True:
        escolha = input("""
        Escolha uma opção:
        1 - Cadastrar
        2 - Iniciar sessão
        3 - Sair
        
        """)
        if escolha == "1":
            cadastrar()
        elif escolha == "2":
            if not iniciar():
                break
        elif escolha == "3":
            print("Programa encerrado.")
            break
        else:
            print("Escolha inválida.")


main()

