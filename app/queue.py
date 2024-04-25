class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # Inicialize o tamanho da fila como 0

    def enqueue(self, task):
        if not self.head:
            self.head = task
            self.tail = task
        else:
            self.tail.next = task
            self.tail = task
        self.size += 1  # Incrementar o tamanho da fila ao adicionar uma tarefa

    def dequeue(self):
        if not self.head:
            return None
        else:
            task = self.head
            self.head = self.head.next
            self.size -= 1  # Decrementar o tamanho da fila ao remover uma tarefa
            return task

    def is_empty(self):
        return self.head is None
