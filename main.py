from app.manager import Manager

manager = Manager("tasks.json")

while True:
    action = input("\nEscolha uma ação:\n"
                   "1. Adicionar Tarefa\n"
                   "2. Remover Tarefa\n"
                   "3. Editar Tarefa\n"
                   "4. Mostrar Tarefas\n"
                   "5. Sair\n"
                   "Opção: ")

    if action == "1":
        description = input("Descrição da tarefa: ")
        priority = input("Prioridade (alta, média, baixa): ")
        status = input("Status (pendente, em andamento, concluída): ")
        manager.add_task(description, priority, status)
        manager.save_tasks()
        print("Tarefa adicionada com sucesso!")

    elif action == "2":
        if manager.tasks:
            manager.get_tasks()
            indice = int(input("Índice da tarefa para remover: "))
            manager.remove_task(indice)
            manager.save_tasks()
            print("Tarefa removida com sucesso!")
        else:
            print("Não há tarefas para remover.")

    elif action == "3":
        if manager.tasks:
            manager.get_tasks()
            indice = int(input("Índice da tarefa para editar: "))
            manager.edit_task(indice)
            manager.save_tasks()

            print("Tarefa editada com sucesso!")
        else:
            print("Não há tarefas para editar.")

    elif action == "4":
        manager.get_tasks()

    elif action == "5":
        break

    else:
        print("Opção inválida. Tente novamente.")

print("\nSaindo do gerenciador de tarefas.")
