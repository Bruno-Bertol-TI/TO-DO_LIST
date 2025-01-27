import os
from pprint import pformat

funcoes = {
    '1': 'Adicionar Tarefa.',
    '2': 'Concluir Tarefa.',
    '3': 'Remover Tarefa.',
    '4': 'Vizualizar Tarefa.',
    '5': 'Encerrar sistema.'
}
tam = 30 * '-'
tarefas = set() #lista 
lista_tarefas = [] #lista fonte do armazenamento

def pause():
    click_enter = input('Pressione [ENTER] para seguir')
    os.system('cls')

def validar_tarefa(valid_list, adl_tarefa, adl_situacao):
        if valid_list not in tarefas:
            tarefas.add(valid_list)
            def atribuir_dados_lista():
                lista_tarefas.append({'tarefa': adl_tarefa, 'situacao': adl_situacao})
            print(f'|{tam * 2}|')
            print(f'|     Sua tarefa foi adicionada.')
            print(f'|{tam * 2}|')
            atribuir_dados_lista()
        else:
            os.system('cls')
            print(f'| Ops, a tarefa "{valid_list}" ja esta na lista de tarefas.')

def add_tarefa():
        
    os.system('cls')
    while True:
        print(f'|{tam}|')
        print(f'|     Adicione sua tarefa.     |')
        print(f'|{tam}|')
        tarefa = input(f'|     Descreva a tarefa :  ' ).lower()

        while True:
            situacao = input(f'|     Descreva a situacao, [PENDENTE] ou  [CONCLUIDA]: ').lower()
            if situacao.startswith('pendente') or situacao.startswith('concluido'):
                validar_tarefa(tarefa, tarefa, situacao)
                break
            else:
                os.system('cls')
                continue
        pause()
        break
    os.system('cls')
        
def concluir_tarefa():
    os.system('cls')
    vizualizar_tarefa()
    
    while True:
        concluir = int(input('| Digite o numero da tarefa que deseja concluir: '))
        if concluir >= 0 and concluir < len(lista_tarefas):
            lista_tarefas[concluir]['situacao'] = 'concluida'
            os.system('cls')
            vizualizar_tarefa()
            os.system('cls') 
            break        
        else:
            os.system('cls')
            print("| Número inválido. Por favor, digite um número correspondente a uma tarefa.")
            continue

def remover_tarefa():
    os.system('cls')

    vizualizar_tarefa()

    if not lista_tarefas:
        print("Não há tarefas para remover.")
        return

    excluir = input('| Digite o número da tarefa que deseja excluir: ')

    if not excluir.strip():
        print("| Entrada vazia. Por favor, digite um número válido.")
        pause()
        return

    if not excluir.isdigit():
        print("| Entrada inválida. Digite um número.")
        pause()
        return

    excluir = int(excluir)

    if 0 <= excluir < len(lista_tarefas):
        tarefa_removida = lista_tarefas.pop(excluir)
        print(f"Tarefa '{tarefa_removida['tarefa']}' removida com sucesso!")
    else:
        print("| Tarefa inválida. Digite um número dentro da lista.")
    pause()

def vizualizar_tarefa():
    os.system('cls')

    vizualizar_lista_tarefas = [
    {**tarefas_situacao, 'tarefa': tarefas_situacao['tarefa'], 'situacao': tarefas_situacao['situacao']}
    for tarefas_situacao in lista_tarefas
    ]

    if not vizualizar_lista_tarefas:
        print('Lista está vazia')
    else:
        for idx, i in enumerate(vizualizar_lista_tarefas):
            lista_formatada_impressao = f'[{idx}] A tarefa: "{i["tarefa"]}" está {i["situacao"]}'
            formatar = pformat(lista_formatada_impressao, width=65)
            formatar_barras = '\n'.join(f'| {line} |' for line in formatar.splitlines())
            print(formatar_barras)
    pause()

def encerrar_sistema():
    os.system('cls')
    exit()

while True:
    print(f'|{tam}|')
    for i in funcoes:
        print(f'| {i} | {funcoes.get(i)}')
    print(f'|{tam}|')

    entrada = input('| O que quer fazer agora? : ')
    entrada = int(entrada) if entrada.isdigit() else entrada
    os.system('cls')

    if entrada == 1:
        add_tarefa() 
    elif entrada == 2:
        concluir_tarefa() 
    elif entrada == 3:
         remover_tarefa()
    elif entrada == 4:
        vizualizar_tarefa()
    elif entrada == 5:
        encerrar_sistema()
    else:
        os.system('cls')
        print(f'|{tam * 3}|')
        print(f'| Opção | {entrada} | não é permitida, tente novamente, mas desta vez, uma opção valida.')
        print(f'|{tam * 3}|')
        continue
    continue