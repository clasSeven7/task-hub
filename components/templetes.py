import PySimpleGUI as sg

from app.manager import Manager

manager = Manager("./database/tasks.json")


def adicionar_tarefa():
    description = sg.popup_get_text("Descrição da tarefa:")
    priority = sg.popup_get_text("Prioridade (alta, média, baixa):")
    status = sg.popup_get_text("Status (pendente, em andamento, concluída):")
    manager.add_task(description, priority, status)
    manager.save_tasks()


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


def pesquisar_tarefas():
    if manager.tasks:
        search = sg.popup_get_text(
            "Digite a descrição da tarefa que deseja pesquisar:")
        tasks = manager.search_task(search)
        sg.popup_scrolled(tasks, title="Tarefas")
    else:
        sg.popup("Não há tarefas para pesquisar.")


def filtrar_tarefas():
    if manager.tasks:
        filter = sg.popup_get_text(
            "Digite o status(pendente, em andamento, concluída) da tarefa que deseja filtrar:")
        tasks = manager.filter_task(filter)
        sg.popup_scrolled(tasks, title="Tarefas")
    else:
        sg.popup("Não há tarefas para filtrar.")


def prioridade_tarefa(priority):
    if manager.tasks:
        tasks = manager.priority_task(priority)
        sg.popup_scrolled(tasks, title="Tarefas")
    else:
        sg.popup("Não há tarefas para filtrar.")


def status_tarefa(status):
    if manager.tasks:
        tasks = manager.status_task(status)
        sg.popup_scrolled(tasks, title="Tarefas")
    else:
        sg.popup("Não há tarefas para filtrar.")
