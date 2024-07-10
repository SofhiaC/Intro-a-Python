import os

restaurantes = ['Lasanha', 'Batata']

def exibir_nome_do_programa():
    print('Comidinha Legal \n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair \n')

def exibir_funcao(texto):
    os.system('cls')
    print(texto)
    print()

def voltar_ao_menu_inicial():
    input('\nDigite uma tecla para voltar ao menu inicial: ')
    main()

def cadastrar_novo_restaurante():
    exibir_funcao('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso! \n')
    voltar_ao_menu_inicial()

def listar_restaurantes():
    exibir_funcao('Listanto os restaurantes')
    for restaurante in restaurantes:
        print(f'. {restaurante}')
    voltar_ao_menu_inicial()

def ativar_restaurante():
    pass

def finalizar_app():
    exibir_funcao('Finalizando programa.')

def opcao_invalida():
    print('Opção inválida.\n')
    voltar_ao_menu_inicial()

def escolher_opçao():
    try:
        escolha = int(input('Escolha uma opção:'))
        print(f'Você escolheu a opção {escolha}')
        match escolha:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar Restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

#função que controla o projeto
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opçao()

if __name__ == '__main__':
    main()