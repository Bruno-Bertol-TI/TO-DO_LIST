import os

tam = 30 * '-'
tarefas = set()
lista_tarefas = []


# validar concluido
def validar_tarefa(valid_list):
        if valid_list not in tarefas:
            tarefas.add(valid_list)
            lista_tarefas.append({valid_list: 'pendente'})
            print(f'|{tam * 2}|')
            print(f'|     Sua tarefa foi adicionada.')
            print(f'|{tam * 2}|')


        else:
            os.system('cls')
            print(f'| Ops, a tarefa "{valid_list}" ja esta na lista de tarefas.')

# add_tarefa concluido
def add_tarefa():
        
    while True:

        os.system('cls')

        print(f'|{tam}|')
        print(f'|     Adicione sua tarefa.     |')
        print(f'|{tam}|')

        nova_tarefa = input(f'|     Descreva a tarefa :  ' ).lower()

        validar_tarefa(nova_tarefa)

        check_add_list = input('| Clique em qualquer tecla para sair... ou [C] para continuar: ').lower()

        os.system('cls')
        
        if check_add_list.startswith('c'):
            continue
        else:
            break

# concluir tarefa concluida
def concluir_tarefa():

    os.system('cls')

    if lista_tarefas:
        print(f'| Cód | ......... nome .... status |')
        for i, lista in enumerate(lista_tarefas):
            for nome, status in lista.items():
                print(f'|  {i} |   {nome}  |   {status} |')
    
        while True:
            concluir = int(input('| Digite o numero da tarefa que deseja concluir: '))
            if concluir >= 0 and concluir < len(lista_tarefas):
                lista = lista_tarefas[concluir]
                for nome in lista:
                     lista[nome] = 'concluida'
                os.system('cls')
                if lista_tarefas:
                    print(f'| Cód | ......... nome .... status |')
                    for i, lista in enumerate(lista_tarefas):
                        for nome, status in lista.items():
                            print(f'|  {i} |   {nome}  |   {status} |')
                    check_return_menu = input('|   press enter para seguir ao menu...')
                    os.system('cls') 
                    break  
                break
                    
            else:
                os.system('cls')
                print("| Número inválido. Por favor, digite um número correspondente a uma tarefa.")
                continue
    else:
        print("| A lista de tarefas está vazia.")

# remover tarefa concluida
def remover_tarefa():
    os.system('cls')

    if lista_tarefas:
        print(f'| Cód | ......... nome .... status |')
        for i, lista in enumerate(lista_tarefas):
            for nome, status in lista.items():
                print(f'|  {i} |   {nome}  |   {status} |')
    
        while True:
            excluir = int(input('| Digite o numero da tarefa que deseja excluir: '))
            if excluir >= 0 and excluir < len(lista_tarefas):
                os.system('cls')
                del lista_tarefas[excluir]
                print(f'| lista')
                if lista_tarefas:
                    print(f'| Cód | ......... nome .... status |')
                    for i, lista in enumerate(lista_tarefas):
                        for nome, status in lista.items():
                            print(f'|  {i} |   {nome}  |   {status} |')
                    check_return_menu = input('|   press enter para seguir ao menu...')
                    os.system('cls')   
                    break
                break
            else:
                os.system('cls')
                print("| Número inválido. Por favor, digite um número correspondente a uma tarefa.")
                continue
    else:
        print("| A lista de tarefas está vazia.")

# vizualizar_tarefa concluido
def vizualizar_tarefa():

    os.system('cls')

    if lista_tarefas:
        print(f'| Cód | ......... nome .... status |')
        for i, lista in enumerate(lista_tarefas):
            for nome, status in lista.items():
                print(f'|  {i} |   {nome}  |   {status} |')
        check_menu = input('| Pressione [enter] para retornar ao menu...')
        os.system('cls')

# funcao de encerramento concluida
def encerrar_sistema():
    os.system('cls')
    exit()

while True:

    funcoes = {
        '1': 'Adicionar Tarefa.',
        '2': 'Concluir Tarefa.',
        '3': 'Remover Tarefa.',
        '4': 'Vizualizar Tarefa.',
        '5': 'Encerrar sistema.'
    }

    print(f'|{tam}|')

    for i in funcoes:
        print(f'| {i} | {funcoes.get(i)}')

    print(f'|{tam}|')

    entrada = input('| O que quer fazer agora? : ')
    os.system('cls')
    entrada = int(entrada) if entrada.isdigit() else entrada

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
        
        print(f'Opção | {entrada} | não é permitida, tente novamente, mas desta vez, uma opção valida.')
        print(f'{tam * 2}')
        continue

    continue