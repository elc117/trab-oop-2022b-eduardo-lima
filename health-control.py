from datetime import date
import json

class Proficional:
    def __init__(self, nome: str, especialidade: str, cidade: str, telefone: str = None):
        self.nome = nome
        self.especialidade = especialidade
        self.telefone = telefone
        self.cidade = cidade
    
    def as_dict(self):
        return {'nome': self.nome,
                'especialidade': self.especialidade,
                'telefone': self.telefone,
                'cidade': self.cidade}

    def register():
        pass

    def __str__(self):
        return '{} {}'.format(self.especialidade, self.nome)

class Medicacao:
    def __init__(self, nome: str, qnt: int = None, un: str = None, intervalo: float = None, duracao: date = None, condicao: str = None):
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
        self.qnt = qnt
        self.un = un
        self.intervalo = intervalo
        self.duracao = duracao
        self.condicao = condicao

    
    def as_dict(self):
        return {'nome': self.nome,
                'qnt': self.qnt,
                'un': self.un,
                'intervalo': self.intervalo,
                'duracao': self.duracao,
                'condicao': self.condicao}

    def register():
        pass

    def __str__(self):
        qnt = '\t{}'.format(self.qnt) if self.qnt != None else ''
        un = self.un if self.un != None else ''
        intervalo = '\na cada {} horas'.format(self.intervalo) if self.intervalo != None else ''
        duracao = 'durante {} dias'.format(self.duracao) if self.duracao != None else ''
        condicao = '\nquando: {}'.format(self.condicao) if self.condicao != None else ''

        return '{} {} {} {} {} {}'.format(self.nome, qnt, un, intervalo, duracao, condicao)

class Receita:
    def __init__(self, proficional: Proficional, data: date, medicacao: dict):
        self.proficional = proficional
        self.data = data
        self. medicacao = medicacao
    
    def as_dict(self):
        medicacao = {}
        for k in self.medicacao.keys():
            medicacao[k] = self.medicacao[k].as_dict()
        return {'proficional': self.proficional.as_dict(),
                'data': str(self.data),
                'medicacao': medicacao}

    def register():
        pass

    def __str__(self):
        s = '{}\n{}\n\n'.format(self.data, self.proficional)
        for k in self.medicacao.keys():
            s += '- {}\n'.format(self.medicacao[k])
        return s

class Sintoma:
    def __init__(self, nome: str, data: date = date.today(), qnt: float = None, un: str = None, qlt: str = None):
        '''
        Parametros:

        nome: nome
        data: data
        qnt: fator quantitativo
        un: unidade do fator quantitativo
        qlt: fator qualitativo
        '''
        self.nome = nome
        self.data = data
        self.qnt = qnt
        self.un = un
        self.qlt = qlt
    
    def as_dict(self):
        return {'nome': self.nome,
                'data': str(self.data),
                'qnt': self.qnt,
                'un': self.un,
                'qlt': self.qlt}
    
    def register():
        pass

    def __str__(self):
        return self.nome

class Doenca:
    def __init__(self, nome: str, data: date):
        self.nome = nome
        self.data = data
    
    def as_dict(self):
        return {'nome': self.nome,
                'data': str(self.data)}

    def register():
        pass

    def __str__(self):
        return self.nome

class Exame:
    def __init__(self, nome, medico, data=date.today()):
        self.nome = nome
        self.medico = medico
        self.data = data
    
    def as_dict(self):
        return {'nome': self.nome,
                'medico': self.medico,
                'data': str(self.data)}

    def register():
        pass

    def __str__(self):
        return self.nome

class Consulta:
    def __init__(self, proficional: Proficional, local: str, sintomas: dict, data: date = date.today(), receita: Receita = None, diagnostico: Doenca = None, exame: Exame = None):
        self.proficional = proficional
        self.local = local
        self.sintomas = sintomas
        self.data = data
        self.receita = receita
        self.diagnostico = diagnostico
        self.exame = exame
    
    def as_dict(self):
        sintomas = {}
        for k in self.sintomas.keys():
            sintomas[k] = self.sintomas[k].as_dict()
        return {'proficional': self.proficional.as_dict(),
                'local': self.local,
                'sintomas': sintomas,
                'data': str(self.data),
                'receita': self.receita.as_dict(),
                'diagnostico': self.diagnostico.as_dict(),
                'exame': self.exame.as_dict() if self.exame != None else None}

    def register():
        pass

    def __str__(self):
        return '{} | {} | {}'.format(self.data, self.proficional, self.local)

class Paciente:
    peso = {}
    altura = {}
    
    proficionais = {}
    medicamentos = {}
    receitas = {}
    consultas = {}
    
    def __init__(self, nome: str, data_nascimento: date, peso: float = None, altura: float = None):
        self.nome = nome
        self.data_nascimento = data_nascimento
        if peso != None:    self.add_peso(peso)
        if altura != None:  self.add_altura(altura)
    
    def add_peso(self, peso: float, data:date = date.today()):
        self.peso[str(len(self.peso))] = {'data': str(data), 'valor': peso}
    
    def add_altura(self, altura, data = date.today()):
        self.altura[len(self.altura)] = {'data': str(data), 'valor': altura}
    
    def add_proficional(self, proficional: Proficional):
        self.proficionais[len(self.proficionais)] = proficional
    
    def add_medicacao(self, medicacao: Medicacao, data: date = date.today()):
        self.medicamentos[len(self.medicamentos)] = {'medicacao': medicacao, 'data': data}
    
    def add_receita(self, receita: Receita):
        self.receitas[len(self.receitas)] = receita
    
    #def add_sintoma()

    def add_consulta(self, consulta: Consulta):
        self.consultas[len(self.consultas)] = consulta
    
    def register():
        nome = input('Nome: ')
        data_nsc = date(*map(int, input('Data de nascimento (AAAA/MM/DD): ').split('/')))
        peso = float(input('Peso: '))
        altura = float(input('Altura: '))
        return Paciente(nome, data_nsc, peso, altura)

    def as_dict(self):
        consultas = {}
        for k in self.consultas.keys():
            consultas[k] = self.consultas[k].as_dict()
        return {'nome': self.nome,
                'data_nascimento': str(self.data_nascimento),
                'peso': self.peso,
                'altura': self.altura,
                'consultas': consultas}

    def from_dict(dct):
        new = Paciente(dct['nome'], dct['data_nascimento'])
        for k in dct['peso'].keys():
            new.add_peso(dct['peso'][k]['valor'], dct['peso'][k]['data'])
        for k in dct['altura'].keys():
            new.add_altura(dct['altura'][k]['valor'], dct['altura'][k]['data'])
        return new


    def __str__(self):
        
        return  'Nome: ' + self.nome + \
                '\nData de nascimento: ' + str(self.data_nascimento) + \
                '\nPeso: ' + str(self.peso[max(self.peso.keys())]['valor']) + \
                '\nAltura: ' + str(self.altura[max(self.altura.keys())]['valor']) + \
                '\nConsultas: ' + str(len(self.consultas))

def use_case():
    '''
    Caso de uso, registrar consulta
    '''

    paciente = Paciente('Eduardo Machado de Lima', date(1997, 8, 13), 70.9, 1.73)

    data = date(2022, 10, 24)

    sintomas = {}
    sintomas[0] = Sintoma('febre', data, 38.3, un='ºC')
    sintomas[1] = Sintoma('dor de cabeça', data)

    medico = Proficional('Eduarda Dalcin Marques', 'Médica', 'Santa Maria')
    medicamentos = {}
    medicamentos[0] = Medicacao('Amoxicilina 500mg + Clavulanato 125mg',30, 'comp', 8, 10)
    medicamentos[1] = Medicacao('Lisador', 1, 'caixa', 6, condicao='dor ou febre')
    medicamentos[2] = Medicacao('Predisim 20mg', 1, 'caixa', 12, 5)
    medicamentos[3] = Medicacao('Rinosoro Jet', 1, 'frasco', 8, condicao='sintomas')
    medicamentos[4] = Medicacao('Avamys', 1, 'frasco', 24, 30, condicao='noite')
    
    receita = Receita(medico, data, medicamentos)

    diagnostico = Doenca('Sinusite', data)
    
    consulta = Consulta(medico, 'Hospital da Brigada', sintomas, data, receita, diagnostico)

    paciente.add_consulta(consulta)

    print(paciente)
    for k in paciente.consultas.keys():
        print('Consulta:')
        print(paciente.consultas[k])
        print('\nReceita:')
        print(paciente.consultas[k].receita)
        print('Diagnostico:', paciente.consultas[k].diagnostico)

def json_model():
    paciente = Paciente('Eduardo Machado de Lima', date(1997, 8, 13), 70.9, 1.73)

    data = date(2022, 10, 24)

    sintomas = {}
    sintomas[0] = Sintoma('febre', data, 38.3, un='ºC')
    sintomas[1] = Sintoma('dor de cabeça', data)

    medico = Proficional('Eduarda Dalcin Marques', 'Médica', 'Santa Maria')
    medicamentos = {}
    medicamentos[0] = Medicacao('Amoxicilina 500mg + Clavulanato 125mg',30, 'comp', 8, 10)
    medicamentos[1] = Medicacao('Lisador', 1, 'caixa', 6, condicao='dor ou febre')
    medicamentos[2] = Medicacao('Predisim 20mg', 1, 'caixa', 12, 5)
    medicamentos[3] = Medicacao('Rinosoro Jet', 1, 'frasco', 8, condicao='sintomas')
    medicamentos[4] = Medicacao('Avamys', 1, 'frasco', 24, 30, condicao='noite')
    
    receita = Receita(medico, data, medicamentos)

    diagnostico = Doenca('Sinusite', data)
    
    consulta = Consulta(medico, 'Hospital da Brigada', sintomas, data, receita, diagnostico)

    paciente.add_consulta(consulta)

    print('Paciente\n', paciente.as_dict())

def open_json() -> dict:
    f = open('data.json')
    data = json.load(f)
    f.close()
    return data

def save_json(data: dict):
    f = open('data.json', 'w')
    json.dump(data, f)
    f.close()

def main(): 
    print('Importando dados...')
    try:
        data_json = open_json()
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        data_json = {}
        save_json(data_json)
    while True:
        print('\nControle de Saúde:')
        print('Opções: 1- Acessar; 2- Cadastrar')
        inp = input('\n> ')
        if inp == '1': # Acessar
            print('Acessar:\n1- Proficional\n2- Medicação\n3- Receita\n4- Sintoma\n5- Doença\n6- Exame\n7- Consulta\n8- Paciente')
            inp = input('\n> ')
            
            if inp == '8':
                if 'pacientes' in data_json.keys():
                    print('Pacientes:')
                    for k in data_json['pacientes'].keys():
                        print(int(k)+1, data_json['pacientes'][k]['nome'])
                    inp = int(input('\n> ')) - 1
                    p = Paciente.from_dict(data_json['pacientes'][str(inp)])
                    print(p)
                    if len(p.consultas) > 0:
                        print('Ver consultas?')
                        print('1- Sim 2- Não')
                        inp = input('\n> ')
                        if inp == '1':
                            for k in p.consultas.keys():
                                print(int(k)+1, p.consultas[k]['data'], p.consultas[k]['proficional'])
                
                else:
                    print('Não há pacientes cadastrados.')
                
        elif inp == '2': # Cadastrar
            print('Cadastrar:\n1- Proficional\n2- Medicação\n3- Receita\n4- Sintoma\n5- Doença\n6- Exame\n7- Consulta\n8- Paciente')
            inp = input('\n> ')
            if inp == '1': # Proficional
                Proficional.register()
            elif inp == '2': # Medicação
                Medicacao.register()
            elif inp == '3': # Receita
                Receita.register()
            elif inp == '4': # Sintoma
                Sintoma.register()
            elif inp == '5': # Doença
                Doenca.register()
            elif inp == '6': # Exame
                Exame.register()
            elif inp == '7': # Consulta
                Consulta.register()
            elif inp == '8': # Paciente
                new = Paciente.register()
                if 'pacientes' in data_json.keys():
                    data_json['pacientes'][len(data_json.keys())] = new.as_dict()
                else:
                    data_json['pacientes'] = {0 : new.as_dict()}
                save_json(data_json)

main()
#json_model()
#use_case()
#open_json('data.json')


# Falta:
# Funções from_dict()
# Interface
# Funções register()