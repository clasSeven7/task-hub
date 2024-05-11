import PySimpleGUI as sg

from components.templetes import (adicionar_tarefa, editar_tarefa,
                                  filtrar_tarefas, mostrar_tarefas,
                                  pesquisar_tarefas, remover_tarefa)

sg.theme('reddit')

layout = [
    [sg.Text("Escolha uma ação:")],
    [sg.Button("Adicionar Tarefa")],
    [sg.Button("Remover Tarefa")],
    [sg.Button("Editar Tarefa")],
    [sg.Button("Mostrar Tarefas")],
    [sg.Button("Pesquisar Tarefas")],
    [sg.Button("Filtrar Tarefas")],
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
