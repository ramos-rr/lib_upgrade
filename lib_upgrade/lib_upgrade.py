import os
import subprocess
from time import sleep


def cabecalho_lista(lista: list):
    for a in lista:
        print(a)


def remover_espacos(linha_opcao: str):
        ajuste = linha_opcao.split(' ')
        contar_espaco = ajuste.count('')
        while contar_espaco != 0:
            ajuste.remove('')
            contar_espaco = ajuste.count('')
        return ajuste


def menu_atualizacao(lista_original: list, lista_editada: list):
    print('\nAbaixo, lista das LIBS que possuem atualizações disponíveis:')
    cabecalho_lista(lista_original[:2])
    for index, line in enumerate(lista_editada):
        print(index, line)
    print('999 -> SAIR SEM FAZER ATUALIZAÇÃO')
    print(lista_original[1])
    try:
        opcao = int(input(f'Qual LIB deseja atualizar <selecione de 0 a {len(lista_editada)-1} / 999 para SAIR>: '))
        while opcao not in range(0, len(lista_editada)):
            if opcao == 999:
                break
            print('Opção inválida.')
            opcao = int(input(f'Qual LIB deseja atualizar <selecione de 0 a {len(lista_editada)-1} / 999 para SAIR>: '))
    except Exception:
        print('Erro... Tente novamente!')
        menu_atualizacao(lista_original, lista_editada)
    except KeyboardInterrupt:
        quit('O usuário interrmopeu o sistema. Até logo!')
    else:
        if opcao == 999:
            quit('Encerrando o programa de atualização... Até logo')
        return opcao


def atualizar_opcao_lib(opcao: int, lista_editada: list):
    lib_update = remover_espacos(lista_editada[opcao])
    continuar = str(input(f'Atualizar \033[1;32m{lib_update[0]}, v.{lib_update[1]} para v.{lib_update[2]}'
                          f'\033[m? [S/N]: ')).strip().upper()[0]
    if continuar == 'S':
        try:
            update = subprocess.check_output(f'pip install {lib_update[0]}=={lib_update[2]}')
        except:
            print(f'Erro na atualização da lib {lib_update[0]}')
        else:
            print(update)
            print(f'\033[1;32mAtualização da LIB {lib_update[0].upper()} realizada com sucesso!\033[m')
        finally:
            lista_editada.pop(opcao)
            print('Retornando ao menu das atualizações')
            print()
    else:
        print('Retornando ao menu anterior')
        sleep(0.5)


def upgrade_lib():
    txt = 'requeriments_to_update.txt'
    while True:
        try:
            original_update_list = []
            edited_update_list = []
            code = os.system(f'pip list -o > {txt}')
            print(f'Aguarde o retorno da lista das LIBS para atualização...')
            sleep(3.0)
            with open(txt) as arq:
                for line in arq:
                    original_update_list.append(line.strip())
            edited_update_list = original_update_list[2:]
            os.remove(txt)
        except Exception:
            print(f'Erro ao ler o arquivo "{txt}"')
            continuar = str(input('Deseja tentar novamente: [S/N] ')).upper().strip()[0]
            if continuar == 'N':
                quit('Você encerrou a atualização sem realizar nenhuma alteração')
            else:
                pass
        else:
            if len(original_update_list) == 0:
                print('Todas as LIBS já estão atualizadas!')
                quit('Encerrando o sistema de atualização... Até logo')
            else:
                atualizar_opcao_lib(opcao=menu_atualizacao
                (lista_original=original_update_list, lista_editada=edited_update_list),
                                    lista_editada=edited_update_list)