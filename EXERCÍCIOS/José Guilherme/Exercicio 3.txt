class ListaDeTarefas:
    def __init__(self):
        self._tarefas = []

    def adicionar(self, tarefa):
        self._tarefas.append(tarefa)

    def __len__(self):
        return len(self._tarefas)

    def __getitem__(self, index):
        return self._tarefas[index]

    def __iter__(self):
        return iter(self._tarefas)
