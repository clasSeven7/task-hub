import PySimpleGUI as sg

from app.manager import Manager

manager = Manager("./database/tasks.json")

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
        break

    if event == "Adicionar Tarefa":
        description = sg.popup_get_text("Descrição da tarefa:")
        priority = sg.popup_get_text("Prioridade (alta, média, baixa):")
        status = sg.popup_get_text(
            "Status (pendente, em andamento, concluída):")
        manager.add_task(description, priority, status)
        manager.save_tasks()
        sg.popup("Tarefa adicionada com sucesso!")

    if event == "Remover Tarefa":
        if manager.tasks:
            tasks = manager.get_tasks()
            indice = sg.popup_get_text("Índice da tarefa para remover:")
            manager.remove_task(indice)
            manager.save_tasks()
            sg.popup("Tarefa removida com sucesso!")
        else:
            sg.popup("Não há tarefas para remover.")

    if event == "Editar Tarefa":
        if manager.tasks:
            tasks = manager.get_tasks()
            indice = sg.popup_get_text("Índice da tarefa para editar:")
            manager.edit_task(indice)
            manager.save_tasks()
            sg.popup("Tarefa editada com sucesso!")
        else:
            sg.popup("Não há tarefas para editar.")

    if event == "Mostrar Tarefas":
        tasks = manager.get_tasks()
        sg.popup(tasks)

manager.save_tasks()
window.close()
