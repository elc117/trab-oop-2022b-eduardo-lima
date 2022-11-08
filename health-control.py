from datetime import date

class Proficional:
    def __init__(self, nome: str, especialidade: str, cidade: str, telefone: str = None):
        self.nome = nome
        self.especialidade = especialidade
        self.telefone = telefone
        self.cidade = cidade
    
    def __str__(self):
        return '{} {}'.format(self.especialidade, self.nome)

class Medicacao:
    def __init__(self, nome: str, qnt: int = None, un: str = None,intervalo: float = None, duracao: date = None, condicao: str = None):
        '''
        
        Parametros:
        
            nome: nome
            qnt: quantidade
            un: unidade da quantidade
            intervalo: intervalo em horas
            duração: duração em dias
            condicao: condição para tomar a medicação
        '''
        self.nome = nome
        self.intervalo = intervalo
        self.duracao = duracao
    
    def __str__(self):
        return self.nome

class Receita:
    def __init__(self, proficional: Proficional, data: date, medicacao: list | Medicacao):
        self.proficional = proficional
        self.data = data
        self. medicacao = medicacao
    
    def __str__(self):
        s = '{}\n{}\n'.format(self.data, self.proficional)
        for m in self.medicacao:
            s += '{}\n'.format(m)
        return s

class Sintoma:
    def __init__(self, nome: str, data: date = date.today(), qnt=None):
        self.data = data
        self.nome = nome
        self.qnt = qnt
    
    def __str__(self):
        return self.nome

class Doenca:
    def __init__(self, nome: str, data: date):
        self.data = data
        self.nome = nome
    
    def __str__(self):
        return self.nome

class Exame:
    def __init__(self, nome, medico, data=date.today()):
        self.nome = nome
        self.medico = medico
        self.data = data
    
    def __str__(self):
        return self.nome

class Consulta:
    def __init__(self, proficional: Proficional, local: str, sintomas: list | Sintoma, data: date, receita: Receita = None, diagnostico: Doenca = None, exame: Exame = None):
        self.data = data
        self.proficional = proficional
        self.local = local
        self.sintomas = sintomas
        self.receita = receita
        self.diagnostico = diagnostico
        self.exame = exame
    
    def __str__(self):
        return '{} | {} | {}'.format(self.data, self.proficional, self.local)

class Paciente:
    peso = {}
    altura = {}
    consultas = {}

    def __init__(self, nome: str, data_nascimento: date, peso: float = None, altura: float = None):
        self.nome = nome
        self.data_nascimento = data_nascimento
        if peso != None:    self.add_peso(peso)
        if altura != None:  self.add_altura(altura)
    
    def add_peso(self, peso: float, data:date = date.today()):
        self.peso[data] = peso
    
    def add_altura(self, altura, data = date.today()):
        self.altura[data] = altura
    
    def add_consulta(self, consulta: Consulta):
        self.consultas[consulta.data] = consulta
    
    def __str__(self):
        return self.nome

def main():
    '''
    Caso de uso, registrar consulta
    '''

    paciente = Paciente('Eduardo Machado de Lima', date(1997, 8, 13), 70.9, 1.73)

    data = date(2022, 10, 24)

    sintomas = []
    sintomas.append(Sintoma('febre', data, 38.3))
    sintomas.append(Sintoma('dor de cabeça', data))

    medico = Proficional('Eduarda Dalcin Marques', 'Médica', 'Santa Maria')
    medicamentos = []
    medicamentos.append(Medicacao('Amoxicilina 500mg + Clavulanato 125mg',30, 'comp', 8, 10))
    medicamentos.append(Medicacao('Lisador', 1, 'caixa', 6, condicao='dor ou febre'))
    medicamentos.append(Medicacao('Predisim 20mg', 1, 'caixa', 12, 5))
    medicamentos.append(Medicacao('Rinosoro Jet', 1, 'frasco', 8, condicao='sintomas'))
    medicamentos.append(Medicacao('Avamys', 1, 'frasco', 24, 30, condicao='noite'))
    
    receita = Receita(medico, data, medicamentos)

    diagnostico = Doenca('Sinusite', data)
    
    consulta = Consulta(medico, 'Hospital da Brigada', sintomas, data, receita, diagnostico)

    paciente.add_consulta(consulta)
    
    for k in paciente.consultas.keys():
        print('Consulta:')
        print(paciente.consultas[k])
        print('\nReceita:')
        print(paciente.consultas[k].receita)
        print('Diagnostico:', paciente.consultas[k].diagnostico)

main()








