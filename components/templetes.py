import PySimpleGUI as sg

from app.manager import Manager

manager = Manager("./database/tasks.json")


def adicionar_tarefa():
    description = sg.popup_get_text("Descrição da tarefa:")
    priority = sg.popup_get_text("Prioridade (alta, média, baixa):")
    status = sg.popup_get_text("Status (pendente, em andamento, concluída):")
    manager.add_task(description, priority, status)
    manager.save_tasks()

    sg.popup("Tarefa adicionada com sucesso!")


def remover_tarefa():
    if manager.tasks:
        indice = sg.popup_get_text("Índice da tarefa para remover:")
        manager.remove_task(indice)
        manager.save_tasks()

        sg.popup("Tarefa removida com sucesso!")
    else:
        sg.popup("Não há tarefas para remover.")


def editar_tarefa():
    if manager.tasks:
        indice = sg.popup_get_text("Índice da tarefa para editar:")
        description = sg.popup_get_text("Descrição da tarefa:")
        priority = sg.popup_get_text("Prioridade (alta, média, baixa):")
        status = sg.popup_get_text(
            "Status (pendente, em andamento, concluída):")
        manager.edit_task(indice, description, priority, status)
        manager.save_tasks()

        sg.popup("Tarefa editada com sucesso!")
    else:
        sg.popup("Não há tarefas para editar.")


def mostrar_tarefas():
    if manager.tasks:
        tasks = manager.get_tasks()
        sg.popup_scrolled(tasks, title="Tarefas")
    else:
        sg.popup("Não há tarefas para mostrar.")
