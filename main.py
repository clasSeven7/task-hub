import PySimpleGUI as sg


from components.templetes import (adicionar_tarefa, editar_tarefa,
                                  filtrar_tarefas, mostrar_tarefas,
                                  pesquisar_tarefas, prioridade_tarefa,
                                  remover_tarefa, status_tarefa)

sg.theme('reddit')

layout = [
    [sg.Text("Escolha uma ação:")],
    [sg.Button("Adicionar Tarefa")],
    [sg.Button("Remover Tarefa")],
    [sg.Button("Editar Tarefa")],
    [sg.Button("Mostrar Tarefas")],
    [sg.Button("Pesquisar Tarefas")],
    [sg.Button("Filtrar Tarefas")],
    [sg.Button("Prioridade Tarefa")],
    [sg.Button("Status Tarefa")],
    [sg.Button("Sair")]
]

layout_prioridade = [
    [sg.Text("Escolha uma prioridade:")],
    [sg.Button("Prioridade Alta")],
    [sg.Button("Prioridade Média")],
    [sg.Button("Prioridade Baixa")],
    [sg.Button("Sair")]
]

layout_status = [
    [sg.Text("Escolha um status:")],
    [sg.Button("Pendente")],
    [sg.Button("Em Andamento")],
    [sg.Button("Concluída")],
    [sg.Button("Sair")]
]

window = sg.Window("Gerenciador de Tarefas", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Sair":
        if sg.popup_yes_no("Deseja realmente sair?") == "Yes":
            window.close()
            print('Saindo do programa...')
            break
        if event == "No":
            continue

    if event == "Adicionar Tarefa":
        adicionar_tarefa()

    if event == "Remover Tarefa":
        mostrar_tarefas()
        remover_tarefa()

    if event == "Editar Tarefa":
        editar_tarefa()

    if event == "Mostrar Tarefas":
        mostrar_tarefas()

    if event == "Pesquisar Tarefas":
        pesquisar_tarefas()

    if event == "Filtrar Tarefas":
        filtrar_tarefas()

    if event == "Prioridade Tarefa":
        window_prioridade = sg.Window("Prioridade", layout_prioridade)

        while True:
            event, values = window_prioridade.read()

            if event == sg.WIN_CLOSED or event == "Sair":
                window_prioridade.close()
                print('Saindo do programa...')
                break

            if event == "Prioridade Alta":
                prioridade_tarefa(priority='alta')
                break

            if event == "Prioridade Média":
                prioridade_tarefa(priority='media')
                break

            if event == "Prioridade Baixa":
                prioridade_tarefa(priority='baixa')
                break

    if event == "Status Tarefa":
        window_status = sg.Window("Status", layout_status)

        event, values = window_status.read()

        while True:
            if event == sg.WIN_CLOSED or event == "Sair":
                print('Saindo do programa...')
                break

            if event == "Pendente":
                status_tarefa(status='pendente')
                break

            if event == "Em Andamento":
                status_tarefa(status='em andamento')
                break

            if event == "Concluída":
                status_tarefa(status='concluída')
                break

            if event == "Ok":
                continue

    if event == "Sair":
        break
