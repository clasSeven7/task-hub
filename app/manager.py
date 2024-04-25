import json

from app.task import Task


class Manager:
    def __init__(self, name_file_json):
        self.name_file_json = name_file_json
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.name_file_json, "r") as file:
                data_json = json.load(file)
                for task_json in data_json:
                    task = Task.from_json(task_json)
                    self.tasks.append(task)
            if self.tasks:
                print(f"{len(self.tasks)} tarefas carregadas com sucesso.")
        except FileNotFoundError:
            print("Nenhuma tarefa carregada.")

    def save_tasks(self):
        data_json = []
        for task in self.tasks:
            data_json.append(task.to_json())

        with open(self.name_file_json, "w") as file:
            json.dump(data_json, file)

    def add_task(self, description, priority, status):
        new_task = Task(description, priority, status)
        self.tasks.append(new_task)

        self.save_tasks()

    def remove_task(self, indice):
        del self.tasks[indice]

        self.save_tasks()

    def edit_task(self, indice):
        edit_task = self.tasks[indice]
        description = input("Nova descrição da tarefa: ")
        priority = input("Nova prioridade da tarefa: ")
        status = input("Novo status da tarefa: ")
        edit_task.set_description(description)
        edit_task.set_priority(priority)
        edit_task.set_status(status)

        self.save_tasks()

    def get_tasks(self):
        if self.tasks:
            print("\nTarefas:")
            for indice, task in enumerate(self.tasks):
                print(
                    f"{indice}. {task.get_description()} - {task.get_priority()} - {task.get_status()}")
        else:
            print("Não há tarefas cadastradas.")
