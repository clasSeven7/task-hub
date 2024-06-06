import json

import PySimpleGUI as sg

from .queue import Queue
from .task_manager import Task


class Manager:
    def __init__(self, name_file_json):
        self.name_file_json = name_file_json
        self.tasks = Queue()
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.name_file_json, "r") as file:
                data_json = json.load(file)
                for task_json in data_json:
                    task = Task.from_json(task_json)
                    self.tasks.enqueue(task)
            if not self.tasks.is_empty():
                print(f"{self.tasks.size} tarefas carregadas com sucesso.")
        except FileNotFoundError:
            print("Nenhuma tarefa carregada.")

    def save_tasks(self):
        data_json = []
        temp_queue = Queue()

        while not self.tasks.is_empty():
            task = self.tasks.dequeue()

            data_json.append(task.to_json())
            temp_queue.enqueue(task)

        while not temp_queue.is_empty():
            self.tasks.enqueue(temp_queue.dequeue())

        with open(self.name_file_json, "w") as file:
            json.dump(data_json, file)

    def add_task(self, description, priority, status):
        # Verificar se os campos estão vazios
        if not description or not priority or not status:
            # Se algum campo estiver vazio, perguntar ao usuário se deseja cancelar a adição da tarefa
            if sg.popup_yes_no("Um ou mais campos estão vazios. Deseja cancelar a adição da tarefa?") == "Yes":
                print("Adição de tarefa cancelada.")
                return
        else:
            # Se todos os campos estiverem preenchidos, criar a nova tarefa
            new_task = Task(description, priority, status)
            self.tasks.enqueue(new_task)
            self.save_tasks()
            sg.popup("Tarefa adicionada com sucesso.")

    def remove_task(self, indice):
        try:
            indice = int(indice)
        except ValueError:
            print("Índice inválido.")
            return
        if indice < 0 or indice >= self.tasks.size:
            print("Índice inválido.")
            return

        temp_queue = Queue()
        current_index = 0

        while not self.tasks.is_empty():
            task = self.tasks.dequeue()
            if current_index != indice:
                temp_queue.enqueue(task)
            current_index += 1

        while not temp_queue.is_empty():
            self.tasks.enqueue(temp_queue.dequeue())

        self.save_tasks()
        print("Tarefa removida com sucesso!")

    def edit_task(self, indice, description, priority, status):
        if indice < 0 or indice >= self.tasks.size:
            print("Índice inválido.")
            return

        temp_queue = Queue()
        found = False

        while not self.tasks.is_empty():
            task = self.tasks.dequeue()
            if indice == 0 and not found:
                task.description = description
                task.priority = priority
                task.status = status
                found = True

            temp_queue.enqueue(task)
            indice -= 1

        if not found:
            print("Índice não encontrado.")

        while not temp_queue.is_empty():
            self.tasks.enqueue(temp_queue.dequeue())

        self.save_tasks()

    def get_tasks(self):
        if not self.tasks.is_empty():
            tasks_string = "\nTarefas:\n"
            temp_queue = Queue()
            current_index = 0

            while not self.tasks.is_empty():
                task = self.tasks.dequeue()
                tasks_string += f"{current_index}. {task.description} - {task.priority} - {task.status}\n"
                temp_queue.enqueue(task)
                current_index += 1

            while not temp_queue.is_empty():
                self.tasks.enqueue(temp_queue.dequeue())

            return tasks_string
        else:
            return "Não há tarefas cadastradas."

    def search_task(self, search):
        if not self.tasks.is_empty():
            tasks_string = "\nTarefas encontradas:\n"
            temp_queue = Queue()
            current_index = 0

            while not self.tasks.is_empty():
                task = self.tasks.dequeue()
                if search in task.description:
                    tasks_string += f"{current_index}. {task.description} - {task.priority} - {task.status}\n"
                    current_index += 1
                temp_queue.enqueue(task)

            while not temp_queue.is_empty():
                self.tasks.enqueue(temp_queue.dequeue())

            return tasks_string
        else:
            return "Não há tarefas cadastradas."

    def filter_task(self, filter):
        if not self.tasks.is_empty():
            tasks_string = "\nTarefas filtradas:\n"
            temp_queue = Queue()
            current_index = 0

            while not self.tasks.is_empty():
                task = self.tasks.dequeue()
                if filter == task.status:
                    tasks_string += f"{current_index}. {task.description} - {task.priority} - {task.status}\n"
                    current_index += 1
                temp_queue.enqueue(task)

            while not temp_queue.is_empty():
                self.tasks.enqueue(temp_queue.dequeue())

            return tasks_string
        else:
            return "Não há tarefas cadastradas."

    def clear_tasks(self):
        while not self.tasks.is_empty():
            self.tasks.dequeue()

        self.save_tasks()
        print("Tarefas apagadas com sucesso.")

    def priority_task(self, priority):
        if not self.tasks.is_empty():
            temp_queue = Queue()
            tasks_string = "\nTarefas filtradas por prioridade:\n"
            current_index = 0

            while not self.tasks.is_empty():
                task = self.tasks.dequeue()
                if priority == task.priority:
                    tasks_string += f"{current_index}. {task.description} - {task.priority} - {task.status}\n"
                    current_index += 1
                temp_queue.enqueue(task)

            while not temp_queue.is_empty():
                self.tasks.enqueue(temp_queue.dequeue())

        return tasks_string

    def status_task(self, status):
        if not self.tasks.is_empty():
            temp_queue = Queue()
            tasks_string = "\nTarefas filtradas por status:\n"
            current_index = 0

            while not self.tasks.is_empty():
                task = self.tasks.dequeue()
                if status == task.status:
                    tasks_string += f"{current_index}. {task.description} - {task.priority} - {task.status}\n"
                    current_index += 1
                temp_queue.enqueue(task)

            while not temp_queue.is_empty():
                self.tasks.enqueue(temp_queue.dequeue())

        return tasks_string
