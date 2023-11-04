import heapq
import random

class Paciente:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade

    def __lt__(self, outro):
        if self.prioridade != outro.prioridade:
            return self.prioridade < outro.prioridade
        else:
            return self.idade < outro.idade

class ProntoSocorro:
    def __init__(self):
        self.fila_prioridades = []
        self.ultimos_pacientes_chamados = []

    def adicionar_paciente(self):
        nome = input("Digite o nome do paciente: ")
        idade = int(input("Digite a idade do paciente: "))
        prioridade = int(input("Digite a prioridade do paciente: "))
        paciente = Paciente(nome, idade, prioridade)
        heapq.heappush(self.fila_prioridades, paciente)

    def atender_proximo_paciente(self):
        if self.fila_prioridades:
            paciente = heapq.heappop(self.fila_prioridades)
            self.ultimos_pacientes_chamados.append(paciente)
            return paciente
        else:
            return None

    def visualizar_fila_prioridades(self):
        for paciente in self.fila_prioridades:
            print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Prioridade: {paciente.prioridade}")

    def mostrar_proximo_paciente(self):
        if self.fila_prioridades:
            proximo_paciente = self.fila_prioridades[0]
            print(f"Próximo Paciente: Nome: {proximo_paciente.nome}, Idade: {proximo_paciente.idade}, Prioridade: {proximo_paciente.prioridade}")
        else:
            print("Não há pacientes na fila.")

    def listar_ultimos_pacientes_chamados(self):
        if self.ultimos_pacientes_chamados:
            print("Últimos 5 Pacientes Chamados:")
            for paciente in self.ultimos_pacientes_chamados[-5:]:
                print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Prioridade: {paciente.prioridade}")
        else:
            print("Nenhum paciente foi chamado ainda.")

    def simular_jogo(self):
        while True:
            print("\nMenu do Pronto-Socorro:")
            print("1. Adicionar Paciente Manualmente")
            print("2. Adicionar Paciente Aleatoriamente")
            print("3. Atender Próximo Paciente")
            print("4. Visualizar Fila de Prioridades")
            print("5. Mostrar Próximo Paciente (sem chamar)")
            print("6. Listar Últimos 5 Pacientes Chamados")
            print("7. Sair")

            escolha = input("Digite sua escolha: ")
            if escolha == '1':
                self.adicionar_paciente()
            elif escolha == '2':
                nome = f"Paciente {random.randint(1, 100)}"
                idade = random.randint(1, 100)
                prioridade = random.randint(1, 10)
                paciente = Paciente(nome, idade, prioridade)
                heapq.heappush(self.fila_prioridades, paciente)
            elif escolha == '3':
                proximo_paciente = self.atender_proximo_paciente()
                if proximo_paciente:
                    print(f"Atendido Paciente: Nome: {proximo_paciente.nome}, Idade: {proximo_paciente.idade}, Prioridade: {proximo_paciente.prioridade}")
                else:
                    print("Não há pacientes na fila.")
            elif escolha == '4':
                self.visualizar_fila_prioridades()
            elif escolha == '5':
                self.mostrar_proximo_paciente()
            elif escolha == '6':
                self.listar_ultimos_pacientes_chamados()
            elif escolha == '7':
                print("Todos os pacientes foram atendidos.")
                break
            else:
                print("Escolha inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    pronto_socorro = ProntoSocorro()
    pronto_socorro.simular_jogo()
