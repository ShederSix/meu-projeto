class ListaDeTarefas:
    #Está def inicia a lista de tarefas vazia
    def __init__(self):
        self.lista_de_tarefas = []
    
    #Está def é utilizada para adicionar uma tarefa na lista de tarefas
    def adicionar_tarefa(self, tarefa):
        self.lista_de_tarefas.append(tarefa)
        return f"{tarefa} adicionada com sucesso à sua lista de tarefas."

    #Está def é utilizada para remover uma tarefa na lista de tarefas
    def remover_tarefa(self, tarefa):
        if tarefa in self.lista_de_tarefas:
            self.lista_de_tarefas.remove(tarefa)
            return f"{tarefa} removida com sucesso de sua lista de tarefas."
        else:
            return f"Tarefa '{tarefa}' não encontrada na lista."
        
    #Está def é utilizada para visualizar as tarefas já na lista de tarefas
    def visualizar_tarefas(self):
        if self.lista_de_tarefas:
            return "\n".join(self.lista_de_tarefas)
        else:
            return "Sua lista de tarefas está vazia."