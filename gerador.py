from secrets import *
from string import *
from time import sleep


def linha():
    print('-' * 60)


def gera_senha(tamanho=8):
    caracteres = ascii_letters + punctuation + digits
    senha = ''.join(choice(caracteres) for c in range(tamanho))
    return senha


historico_senhas = list()
contador_senhas = 0
while True:
    print('MENU PRINCIPAL'.center(60))
    linha()
    
    opções = [
            "Gerar nova senha",
            "Ver histórico de senhas",
            "Sair"
    ]

    for i, v in enumerate(opções):
        print(f"{f'[{i+1}]':>20} {v:<60}")
    
    linha()
    
    try:
        opcao = int(input('Escolha uma opção:'.center(60)))
    except ValueError:
        print('Por favor, digite um número válido.'.center(60))
        continue

    if opcao == 1:
        nova_senha = gera_senha()
        historico_senhas.append(nova_senha)
        contador_senhas += 1
        print(f'Nova senha: {nova_senha}'.center(60))
        linha()
        sleep(0.5)

    elif opcao == 2:
        if len(historico_senhas) == 0:
            
            linha()
            print('Não existe nenhuma senha gerada anteriormente.'.center(60))
            sleep(0.5)
            linha()
        
        else:
            linha()
            for i, v in enumerate(historico_senhas):
                print(f'Senha {i + 1}: {v}'.center(60))
            linha()


    elif opcao == 3:
        print('Saindo...'.center(60))
        sleep(0.6)
        break

    else:
        print('Opção inválida, tente novamente.')
