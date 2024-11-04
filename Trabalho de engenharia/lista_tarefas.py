# Primeiramente importamos a biblioteca de testes, o unittest     
import unittest

# Código principal :
# # Classe que representa a lista de tarefas
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

"""while True:
    print("MENU:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Mostrar Tarefas")
    print("4. Sair")
    opcao = input("Informe o número da opção desejada: ")
    
    if opcao == "1":
        tarefa_para_adicionar = input("Informe qual tarefa deve ser adicionada na lista: ")
        adicionarTarefa(tarefa_para_adicionar)
    elif opcao == "2":
        tarefa_para_remover = input("Informe qual tarefa deve ser removida da lista: ")
        removerTarefa(tarefa_para_remover)
    elif opcao == "3":
        visualizarTarefas()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

print("Fim do programa.")"""

#Observação: Caso o usuário digite um enter "vazio" selecionando a opção '1.Adicionar Tarefa', uma tarefa chamada " " será criada
#e caso o usuário selecione a opção '2.Remover Tarefa', ele consegue remover a tarefa " ".

# Código de testes usando o unittest

# Criamos a classe de testes
class TesteListaDeTarefas(unittest.TestCase):
    def setUp(self):
        self.lista = ListaDeTarefas()

    def test_adicionar_tarefa(self):
        resultado = self.lista.adicionar_tarefa("Estudar Python")
        self.assertIn("Estudar Python", self.lista.lista_de_tarefas)
        self.assertEqual(resultado, "Estudar Python adicionada com sucesso à sua lista de tarefas.")

    def test_remover_tarefa_existente(self):
        self.lista.adicionar_tarefa("Estudar Python")
        resultado = self.lista.remover_tarefa("Estudar Python")
        self.assertNotIn("Estudar Python", self.lista.lista_de_tarefas)
        self.assertEqual(resultado, "Estudar Python removida com sucesso de sua lista de tarefas.")

    def test_remover_tarefa_inexistente(self):
        resultado = self.lista.remover_tarefa("Estudar Java")
        self.assertEqual(resultado, "Tarefa 'Estudar Java' não encontrada na lista.")

    def test_visualizar_tarefas_com_tarefas(self):
        self.lista.adicionar_tarefa("Estudar Python")
        self.lista.adicionar_tarefa("Fazer exercícios")
        resultado = self.lista.visualizar_tarefas()
        self.assertEqual(resultado, "Estudar Python\nFazer exercícios")

    def test_visualizar_tarefas_sem_tarefas(self):
        resultado = self.lista.visualizar_tarefas()
        self.assertEqual(resultado, "Sua lista de tarefas está vazia.")

if __name__ == "__main__":
    unittest.main()
