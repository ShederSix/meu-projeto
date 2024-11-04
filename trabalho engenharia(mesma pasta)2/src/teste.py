# Primeiramente importamos a biblioteca de testes, o unittest     
import unittest
from lista import ListaDeTarefas

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
