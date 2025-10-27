import menu.py
import acoes.py

usuarios = {}
saldos = {}


def cadastro():
    print("CADASTRO")
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if nome in usuarios:
        print("Usuário já cadastrado. Escolha outro nome.")
        return
    usuarios[nome] = senha
    saldos[nome] = {"corrente": 0.0, "poupanca": 0.0}
    print(f"Usuário '{nome}' cadastrado com sucesso!")


def login():
    print("LOGIN")
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if nome in usuarios and usuarios[nome] == senha:
        print(f"Login bem-sucedido! Bem-vindo, {nome}!")
        acoes(nome)
    elif nome in usuarios:
        print("Senha incorreta. Tente novamente.")
    else:
        print("Usuário não encontrado. Faça o cadastro primeiro.")