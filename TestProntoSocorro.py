import unittest
from io import StringIO
from unittest.mock import patch
from trabalho import ProntoSocorro, Paciente

class TestProntoSocorro(unittest.TestCase):
    def setUp(self):
        self.pronto_socorro = ProntoSocorro()

    def test_adicionar_paciente(self):
        input_values = ['Carlos', '30', '2']
        with patch('builtins.input', side_effect=input_values):
            self.pronto_socorro.adicionar_paciente()
        self.assertEqual(len(self.pronto_socorro.fila_prioridades), 1)

    def test_atender_proximo_paciente(self):
        paciente = Paciente('João', 25, 1)
        self.pronto_socorro.fila_prioridades.append(paciente)
        proximo_paciente = self.pronto_socorro.atender_proximo_paciente()
        self.assertEqual(proximo_paciente, paciente)
        self.assertEqual(len(self.pronto_socorro.fila_prioridades), 0)

    def test_visualizar_fila_prioridades(self):
        paciente1 = Paciente('Maria', 40, 3)
        paciente2 = Paciente('Pedro', 35, 2)
        self.pronto_socorro.fila_prioridades = [paciente1, paciente2]
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.pronto_socorro.visualizar_fila_prioridades()
            expected_output = "Nome: Maria, Idade: 40, Prioridade: 3\nNome: Pedro, Idade: 35, Prioridade: 2\n"
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_mostrar_proximo_paciente(self):
        paciente = Paciente('José', 50, 5)
        self.pronto_socorro.fila_prioridades.append(paciente)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.pronto_socorro.mostrar_proximo_paciente()
            expected_output = "Próximo Paciente: Nome: José, Idade: 50, Prioridade: 5\n"
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_listar_ultimos_pacientes_chamados(self):
        ultimos_pacientes = [
            Paciente('Ana', 28, 1),
            Paciente('Miguel', 33, 2),
            Paciente('Sofia', 45, 3),
            Paciente('Rafael', 22, 4),
            Paciente('Isabella', 50, 5)
        ]
        self.pronto_socorro.ultimos_pacientes_chamados = ultimos_pacientes
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.pronto_socorro.listar_ultimos_pacientes_chamados()
            expected_output =  "Últimos 5 Pacientes Chamados:\nNome: Ana, Idade: 28, Prioridade: 1\nNome: Miguel, Idade: 33, Prioridade: 2\nNome: Sofia, Idade: 45, Prioridade: 3\nNome: Rafael, Idade: 22, Prioridade: 4\nNome: Isabella, Idade: 50, Prioridade: 5\n"
            self.assertEqual(fake_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()