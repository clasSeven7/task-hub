

class Task:
    def __init__(self, description, priority, status):
        self.description = description
        self.priority = priority
        self.status = status
        self.next = None

    def to_json(self):
        return {
            "descricao": self.description,
            "prioridade": self.priority,
            "status": self.status
        }

    @classmethod
    def from_json(cls, data_json):
        try:
            description = data_json["descricao"]
            priority = data_json.get("prioridade", None)
            status = data_json["status"]
        except KeyError as e:
            chave_faltante = str(e.args[0])
            mensagem_erro = f"Erro ao carregar tarefa. O arquivo JSON está faltando a chave '{chave_faltante}'."
            raise ValueError(mensagem_erro)

        return cls(description, priority, status)
