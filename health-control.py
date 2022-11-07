import datetime

class Paciente:
    peso = {}
    altura = {}

    def __init__(self, nome, data_nascimento, peso=None, altura=None):
        self.nome = nome
        self.data_nascimento = data_nascimento
        if peso != None:    self.add_peso(peso)
        if altura != None:  self.add_altura(altura)
    
    def add_peso(self, peso, data=datetime.date.today()):
        self.peso[data] = peso
    
    def add_altura(self, altura, data=datetime.date.today()):
        self.altura[data] = altura

class Proficional:
    def __init__(self, nome, especialidade, cidade, telefone=None):
        self.nome = nome
        self.especialidade = especialidade
        self.telefone = telefone
        self.cidade = cidade

class Sintoma:
    def __init__(self, nome, data=datetime.data.today(), qnt=None):
        self.data = data
        self.nome = nome
        self.qnt = qnt

class Consulta:
    def _init__(self, data, proficional, local, sintomas, receita=None, diagnostico=None, exame=None):
        self.data = data
        self.proficional = proficional
        self.local = local
        self.sintomas = sintomas
        self.receita = receita
        self.diagnostico = diagnostico
        self.exame = exame

class Doenca:
    def __init__(self, data, nome):
        self.data = data
        self.nome = nome

class Receita:
    def __init__(self, proficional, data, medicacao):
        self.proficional = proficional
        self.data = data
        self. medicacao = medicacao

class Medicacao:
    def __init__(self, nome):
        self.nome = nome

class Exame:
    def __init__(self, nome, medico, data=datetime.date.today()):
        self.nome = nome
        self.medico = medico
        self.data = data


