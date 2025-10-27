from acoes import acoes
from cadlog import cadastro
from cadlog import login

usuarios = {}
saldos = {}

while True:
    print("MENU PRINCIPAL")
    print("1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastro()
    elif escolha == "2":
        login()
    elif escolha == "3":
        print("Encerrando o sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")