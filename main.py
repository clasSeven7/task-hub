import PySimpleGUI as sg

from components.templetes import (adicionar_tarefa, editar_tarefa,
                                  mostrar_tarefas, remover_tarefa)

sg.theme('reddit')

layout = [
    [sg.Text("Escolha uma ação:")],
    [sg.Button("Adicionar Tarefa")],
    [sg.Button("Remover Tarefa")],
    [sg.Button("Editar Tarefa")],
    [sg.Button("Mostrar Tarefas")],
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
