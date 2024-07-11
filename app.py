import os

restaurantes = [{'nome':'Hamburquerer', 'categoria':'Hamburgueria', 'ativo':False}, 
                {'nome':'Justino', 'categoria':'Pizzaria', 'ativo':True}, 
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    '''Exibe o nome do programana tela.'''
    print('Comidinha Legal \n')

def exibir_opcoes():
    '''Exibe as funções do menu inicial.'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar Estado do Restaurante')
    print('4. Sair \n')

def exibir_funcao(texto):
    '''Limpa o terminal e exibe o texto referente a função selecionada no menu inicial.'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_inicial():
    '''Solicita ao usuário uma tecla para retornar ao menu inicial.
    Inputs:
    - Uma tecla qualquer
    Outputs:
    - Retorno ao menu inicial
    '''
    input('\nDigite uma tecla para voltar ao menu inicial: ')
    main()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante.
    Inputs: 
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante na lista de restaurantes.
    '''
    exibir_funcao('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso! \n')
    voltar_ao_menu_inicial()

def listar_restaurantes():
    '''Lista os restaurantes presentes na lista.
    Outputs:
    - Exibe a lista de restaurantes.
    '''
    exibir_funcao('Listanto os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_inicial()

def alternar_estado_restaurante():
    '''Altera o estado do restaurante para ativo ou  desativado.
    Inputs: 
    - Nome do restaurante que se deseja alterar
    Outputs:
    - Exibe a mensagem referente ao resultado da solicitação
    '''
    exibir_funcao('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu_inicial()

def finalizar_app():
    '''Exibe mensagem da finalização do aplicativo.'''

    exibir_funcao('Finalizando programa.')

def opcao_invalida():
    '''Exibe mensagem de opção invalida e retorna ao menu inicial. 
    Outputs:
    - Retorna ao menu inicial.
    '''
    print('Opção inválida.\n')
    voltar_ao_menu_inicial()

def escolher_opçao():
    '''Solicita que o usuário execute uma opção.
    Inputs:
    - Opção escolhida
    Outputs:
    - Executa a opção escolhida
    '''
    try:
        escolha = int(input('Escolha uma opção:'))
        print(f'Você escolheu a opção {escolha}')
        match escolha:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função princial que executa a aplicação.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opçao()

if __name__ == '__main__':
    main()