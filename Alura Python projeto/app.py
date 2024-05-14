import os

restaurantes = [{'nome':'Burger King', 'categoria':'Hamburgueria', 'ativo':False}, {'nome':'Atlântico', 'categoria':'pizarria', 'ativo':True}, {'nome':'China Arthur', 'categoria':'Japonesa', 'ativo':True}]

def exibir_nome_do_programa():
    ''' Função que exibe nome do programa.
    Output:
    - print.

    '''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    '''Essa função é responsavel por exibir as opções iniciais

    Outputs:
    - Cadastrar restaurante;
    - Listar restaurante;
    - Alternar estado do restaurante;
    - sair
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função é responsavel por finalizar o aplicativo
    
    Input:
    - Exibir subtitulo.
    '''
    exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
    '''Essa função é responsavel por voltar ao menu principal
    
    Inputs:
    - Digitar uma tecla;
    '''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    '''Essa função é responsavel por mostrar a opção invalida
    
    Outputs:
    - Opção inválida.
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsavel por exibir subtitulo
    
    Outputs:
    - linha;
    - Texto;
    - Linha.
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adicionar um novo restaurante na lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante para cadastro: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsavel por listar os restaurantes cadastrados
    
    Outputs:
    - Exibir a lista de restaurantes

    '''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsavel por atualizar o estado do restaurante
    
    Input:
    - Nome do restaurante

    Output:
    - Mensagem de confirmação e alteração no estado do restaurante
    - Mensagem do restaurante não encontrado
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante para alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if (nome_restaurante == restaurante['nome']):
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsavel por apresentar as opções escolhidas
    
    Input:
    - Escolher a opção de um número inteiro de 1 a 4.

    Output:
    - Cadastrar novo restaurante
    - Listar restaurante
    - Alternar estado do restaurante
    - Finalizar app
    - Opção invalida
    '''
    try:
        opção_escolhida = int(input('Escolha uma opção: '))

        match opção_escolhida:
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
    '''Essa função é responsavel por mostrar o menu principal'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if(__name__ == '__main__'):
    main()

