from datetime import date
import json

class Proficional:
    def __init__(self, nome: str, especialidade: str, cidade: str, telefone: str = None):
        self.nome = nome
        self.especialidade = especialidade
        self.cidade = cidade
        self.telefone = telefone
        
    def as_dict(self):
        return {'nome': self.nome,
                'especialidade': self.especialidade,
                'cidade': self.cidade,
                'telefone': self.telefone}

    def from_dict(dct):
        return Proficional(dct['nome'], dct['especialidade'], dct['cidade'], dct['telefone'])

    def register():
        nome = input('Nome: ')
        especialidade = input('Especialidade: ')
        telefone = input('Telefone: ')
        telefone = telefone if telefone != '' else None
        cidade = input('Cidade: ')
        return Proficional(nome, especialidade, cidade, telefone)

    def __str__(self):
        return '{} {}\n{} {}'.format(self.especialidade, self.nome, self.cidade, self.telefone if self.telefone != None else '')

class Medicamento:
    def __init__(self, nome: str, qnt: int = None, un: str = None, intervalo: float = None, duracao: date = None, condicao: str = None):
        '''
        Parametros:
        
            nome: nome
            qnt: quantidade
            un: unidade da quantidade
            intervalo: intervalo em horas
            duração: duração em dias
            condicao: condição para tomar a Medicamentos
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

    def from_dict(dct):
        return Medicamento(dct['nome'], dct['qnt'], dct['un'], dct['intervalo'], dct['duracao'], dct['condicao'])

    def register():
        nome = input('Nome: ')
        qnt = input('Quantidade: ')
        un = input('Unidade: ')
        intervalo = input('Intervalo: ')
        duracao = input('Duração: ')
        condicao = input('Condição: ')
        return Medicamento(nome, qnt, un, intervalo, duracao, condicao)

    def __str__(self):
        qnt = '\t{}'.format(self.qnt) if self.qnt != None and self.qnt != '' else ''
        un = self.un if self.un != None and self.un != '' else ''
        intervalo = '\na cada {} horas'.format(self.intervalo) if self.intervalo != None and self.intervalo != '' else ''
        duracao = 'durante {} dias'.format(self.duracao) if self.duracao != None and self.duracao != '' else ''
        condicao = '\nquando: {}'.format(self.condicao) if self.condicao != None and self.condicao != '' else ''

        return '{} {} {} {} {} {}'.format(self.nome, qnt, un, intervalo, duracao, condicao)

class Receita:
    def __init__(self, proficional: Proficional, data: date, medicamentos: dict = {}):
        self.proficional = proficional
        self.data = data
        self.medicamentos = medicamentos
    
    def as_dict(self):
        medicamentos = {}
        for k in self.medicamentos.keys():
            medicamentos[k] = self.medicamentos[k].as_dict()
        return {'proficional': self.proficional.as_dict(),
                'data': str(self.data),
                'medicamentos': medicamentos}

    def add_medicamentos(self, medicamentos: Medicamento):
        self.medicamentos[len(self.medicamentos)] = medicamentos

    def from_dict(dct):
        new = Receita(Proficional.from_dict(dct['proficional']), date(*map(int, dct['data'].split('-'))))
        for k in dct['medicamentos'].keys():
            new.add_medicamentos(Medicamento.from_dict(dct['medicamentos'][k]))
        return new
    
    def register(data_json):
        print('Proficional:')
        if 'proficionais' in data_json.keys():
                    print('0 Cadastrar novo')
                    for k in data_json['proficionais'].keys():
                        print(int(k)+1, data_json['proficionais'][k]['nome'])
                    inp = int(input('\n> ')) - 1
                    if inp > -1:
                        proficional = Proficional.from_dict(data_json['proficionais'][str(inp)])
                    else:
                        proficional = Proficional.register()
                        data_json['proficionais'][len(data_json['proficionais'])] = proficional.as_dict()
        else:
            proficional = Proficional.register()
            data_json['proficionais'] = {'0' : proficional.as_dict()}
        data = input('\nData da receita (AAAA/MM/DD) ou vazio para data atual: ')
        if data == '':
            data = date.today()
        else:
            data = date(*map(int, data.split('/')))
        medicamentos = {}
        print('\nMedicamento(s):')
        while True:
            if 'medicamentos' in data_json.keys():
                    print('0 Cadastrar novo')
                    for k in data_json['medicamentos'].keys():
                        print(int(k)+1, data_json['medicamentos'][k]['nome'])
                    inp = int(input('\n> ')) - 1
                    if inp > -1:
                        medicamentos[len(medicamentos)] = Medicamento.from_dict(data_json['medicamentos'][str(inp)])
                    else:
                        medicamentos[len(medicamentos)] = Medicamento.register()
                        data_json['medicamentos'][len(data_json['medicamentos'])] = medicamentos[len(medicamentos)-1].as_dict()
            else:
                medicamentos[len(medicamentos)] = Medicamento.register()
                data_json['medicamentos'] = {'0' : medicamentos[len(medicamentos)-1].as_dict()}
            inp = input('\n1- Adicionar mais; 2- Finalizar\n> ')
            if inp == '2':
                break
        return Receita(proficional, data, medicamentos), data_json

    def __str__(self):
        s = '{}\n{}\n\n'.format(self.data, str(Proficional.from_dict(self.proficional)))
        for k in self.medicamentos.keys():
            s += '- {}\n'.format(self.medicamentos[k])
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
    
    def from_dict(dct):
        return Sintoma(dct['nome'], date(*map(int, dct['data'].split('-'))), dct['qnt'], dct['un'], dct['qlt'])

    def register():
        nome = input('Nome: ')
        data = input('Data do sintoma (AAAA/MM/DD) ou vazio para data atual: ')
        if data == '':
            data = date.today()
        else:
            data = date(*map(int, data.split('/')))
        qnt = input('Quantidade: ')
        un = input('Unidade: ')
        qlt = input('Fator qualitativo: ')
        return Sintoma(nome, data, qnt, un, qlt)

    def __str__(self):
        return (self.nome + ((' ' + self.qlt) if self.qlt != '' and self.qlt != None else '') + \
                (('\n' + self.qlt) if self.qnt != '' and self.qnt != None else '') + \
                ((' ' + self.un) if self.un != '' and self.un != None else '') + \
                '\n' + str(self.data))

class Doenca:
    def __init__(self, nome: str, data: date):
        self.nome = nome
        self.data = data
    
    def as_dict(self):
        return {'nome': self.nome,
                'data': str(self.data)}

    def from_dict(dct):
        return Doenca(dct['nome'], date(*map(int, dct['data'].split('-'))))

    def register():
        nome = input('Nome: ')
        data = input('Data do diagnostico (AAAA/MM/DD) ou vazio para data atual: ')
        if data == '':
            data = date.today()
        else:
            data = date(*map(int, data.split('/')))
        return Doenca(nome, data)
        

    def __str__(self):
        return self.nome + ' ' + str(self.data)

class Exame:
    def __init__(self, nome: str, medico: Proficional, data=date.today()):
        self.nome = nome
        self.medico = medico
        self.data = data
    
    def as_dict(self):
        return {'nome': self.nome,
                'medico': self.medico.as_dict(),
                'data': str(self.data)}

    def from_dict(dct):
        return Exame(dct['nome'], Proficional.from_dict(dct['medico']), date(*map(int, dct['data'].split('-'))))

    def register(data_json: dict):
        nome = input('Nome: ')
        if 'proficionais' in data_json.keys():
                    print('0 Cadastrar novo')
                    for k in data_json['proficionais'].keys():
                        print(int(k)+1, data_json['proficionais'][k]['nome'])
                    inp = int(input('\n> ')) - 1
                    if inp > -1:
                        proficional = Proficional.from_dict(data_json['proficionais'])
                    else:
                        proficional = Proficional.register()
                        data_json['proficionais'][len(data_json['proficionais'])] = proficional.as_dict()
        else:
            print('Cadastrar médico:')
            proficional = Proficional.register()
            data_json['proficionais'] = {'0' : proficional.as_dict()}
        data = input('Data do exame (AAAA/MM/DD) ou vazio para data atual: ')
        if data == '':
            data = date.today()
        else:
            data = date(*map(int, data.split('/')))
        return Exame(nome, proficional, data), data_json

    def __str__(self):
        return self.nome + ' ' + str(self.data)

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

    def from_dict(dct: dict):
        sintomas = {}
        for k in dct['sintomas'].keys():
            sintomas[k] = Sintoma.from_dict(dct['sintomas'][k])
        return Consulta(Proficional.from_dict(dct['proficional']), dct['local'], sintomas, date(*map(int, dct['data'].split('-'))), Receita.from_dict(dct['receita']),
                Doenca.from_dict(dct['diagnostico']) if Doenca.from_dict(dct['diagnostico']) != None else None,
                Exame.from_dict(dct['exame']) if dct['exame'] != None else None)

    def register(data_json: dict):
        if 'proficionais' in data_json.keys():
                    print('Proficional:\n0 Cadastrar novo')
                    for k in data_json['proficionais'].keys():
                        print(int(k)+1, data_json['proficionais'][k]['nome'])
                    inp = int(input('\n> ')) - 1
                    if inp > -1:
                        proficional = Proficional.from_dict(data_json['proficionais'][str(inp)])
                    else:
                        proficional = Proficional.register()
                        data_json['proficionais'][len(data_json['proficionais'])] = proficional.as_dict()
        else:
            print('Cadastrar médico:')
            proficional = Proficional.register()
            data_json['proficionais'] = {'0' : proficional.as_dict()}
        local = input('Local da consulta: ')
        if 'sintomas' in data_json.keys():
                    print('Sintoma:\n0 Cadastrar novo')
                    for k in data_json['sintomas'].keys():
                        print(int(k)+1, data_json['sintomas'][k]['nome'], data_json['sintomas'][k]['qlt'])
                    inp = int(input('\n> ')) - 1
                    if inp > -1:
                        sintoma = Sintoma.from_dict(data_json['sintomas'][str(inp)])
                    else:
                        sintoma = Sintoma.register()
                        data_json['sintomas'][len(data_json['sintomas'])] = sintoma.as_dict()
        else:
            print('Cadastrar sintoma:')
            sintoma = Sintoma.register()
            data_json['sintomas'] = {'0' : sintoma.as_dict()}
        data = input('Data da consulta (AAAA/MM/DD) ou vazio para data atual: ')
        if data == '':
            data = date.today()
        else:
            data = date(*map(int, data.split('/')))
        if 'receitas' in data_json.keys():
                    print('Receita:\n0 Cadastrar nova')
                    for k in data_json['receitas'].keys():
                        print(int(k)+1, data_json['receitas'][k]['proficional']['nome'], data_json['receitas'][k]['data'])
                    inp = int(input('\n> ')) - 1
                    if inp > -1:
                        receita = Receita.from_dict(data_json['receitas'][str(inp)])
                    else:
                        receita, data_json = Receita.register(data_json)
                        data_json['receitas'][len(data_json['receitas'])] = receita.as_dict()
        else:
            print('Cadastrar receita:')
            receita, data_json = Receita.register(data_json)
            data_json['sintomas'] = {'0' : receita.as_dict()}
        if 'doencas' in data_json.keys():
                    print('Diagnostico\n0 Cadastrar novo')
                    for k in data_json['doencas'].keys():
                        print(int(k)+1, data_json['doencas'][k]['nome'])
                    inp = int(input('\n> ')) - 1
                    if inp > -1:
                        doenca = Doenca.from_dict(data_json['doenca'][str(inp)])
                    else:
                        receita = Doenca.register()
                        data_json['doencas'][len(data_json['doencas'])] = doenca.as_dict()
        else:
            print('Cadastrar diagnostico:')
            doenca = Doenca.register()
            data_json['sintomas'] = {'0' : receita.as_dict()}
        if 'exames' in data_json.keys():
                    print('Exame:\n-1 Nenhum\n0 Cadastrar nova')
                    for k in data_json['exames'].keys():
                        print(int(k)+1, data_json['exames'][k]['nome'], data_json['exames'][k]['data'])
                    inp = int(input('\n> ')) - 1
                    if inp > -1:
                        exame = Exame.from_dict(data_json['exames'][str(inp)])
                    elif inp == 0:
                        exame = Exame.register()
                        data_json['exames'][len(data_json['exames'])] = exame.as_dict()
                    else:
                        exame = None
        else:
            inp = input('Cadastrar exame? (s/n): ')
            if inp == 's':
                exame = Exame.register()
                data_json['exames'] = {'0' : exame.as_dict()}
            else:
                exame = None
        return Consulta(proficional, local, {'0': sintoma}, data, receita, doenca, exame), data_json
        

    def __str__(self):
        return '{} | {} | {}'.format(self.data, self.proficional.nome, self.local)

class Paciente:
    peso = {}
    altura = {}
    
    proficionais = {}
    medicamentos = {}
    receitas = {}
    consultas = {}
    sintomas = {}
    diagnosticos = {}
    exames = {}
    
    def __init__(self, nome: str, data_nascimento: date, peso: float = None, altura: float = None):
        self.nome = nome
        self.data_nascimento = data_nascimento
        if peso != None:    self.add_peso(peso)
        if altura != None:  self.add_altura(altura)
    
    def add_peso(self, peso: float, data:date = date.today()):
        self.peso[len(self.peso)] = {'data': str(data), 'valor': peso}
    
    def add_altura(self, altura, data = date.today()):
        self.altura[len(self.altura)] = {'data': str(data), 'valor': altura}
    
    def add_proficional(self, proficional: Proficional):
        self.proficionais[len(self.proficionais)] = proficional
    
    def add_medicamentos(self, medicamento: Medicamento, data: date = date.today()):
        self.medicamentos[len(self.medicamentos)] = medicamento
    
    def add_receita(self, receita: Receita):
        self.receitas[len(self.receitas)] = receita
        if receita.proficional not in self.proficionais.values():
            self.proficionais[len(self.proficionais)] = receita.proficional
        for medicamento in receita.medicamentos:
            self.add_medicamentos(medicamento)
    
    def add_sintoma(self, sintoma: Sintoma):
        self.sintomas[len(self.sintomas)] = sintoma

    def add_diagnostico(self, diagnostico: Doenca):
        self.diagnosticos[len(self.diagnosticos)] = diagnostico

    def add_exame(self, exame: Exame):
        self.exames[len(self.exames)] = exame
    
    def add_consulta(self, consulta: Consulta):
        self.consultas[len(self.consultas)] = consulta
        if consulta.proficional not in self.proficionais.values():
            self.add_proficional(consulta.proficional)
        for sintoma in consulta.sintomas.values():
            self.add_sintoma(sintoma)
        if consulta.receita not in self.receitas.values():
            self.add_receita(consulta.receita)
        self.add_diagnostico(consulta.diagnostico)
        if consulta.exame != None:
            self.add_exame(consulta.exame)

    def as_dict(self):
        proficionais = {}
        medicamentos = {}
        receitas = {}
        consultas = {}
        sintomas = {}
        diagnosticos = {}
        exames = {}
        peso = {}
        altura = {}
        
        for k in self.proficionais.keys():
            if self.proficionais[k] != 0:
                proficionais[k] = self.proficionais[k].as_dict()
 
        for k in self.medicamentos.keys():
            if self.medicamentos[k] != 0:
                medicamentos[k] = self.medicamentos[k].as_dict()
        
        for k in self.receitas.keys():
            if self.receitas[k] != 0:
                receitas[k] = self.receitas[k].as_dict()

        for k in self.consultas.keys():
            if self.consultas[k] != 0:
                consultas[k] = self.consultas[k].as_dict()
        
        for k in self.sintomas.keys():
            if self.sintomas[k] != 0:
                sintomas[k] = self.sintomas[k].as_dict()

        for k in self.diagnosticos.keys():
            if self.diagnosticos[k] != 0:
                diagnosticos[k] = self.diagnosticos[k].as_dict()
        
        for k in self.exames.keys():
            if self.exames[k] != 0:
                exames[k] = self.exames[k].as_dict()
        
        for k in self.peso.keys():
            if self.peso[k] != 0:
                peso[k] = {'data': str(self.peso[k]['data']), 'valor': self.peso[k]['valor']}
        
        for k in self.altura.keys():
            if self.altura[k] != 0:
                altura[k] = {'data': str(self.altura[k]['data']), 'valor': self.altura[k]['valor']}

        
        return {'nome': self.nome,
                'data_nascimento': str(self.data_nascimento),
                'peso': peso,
                'altura': altura,
                'proficionais': proficionais,
                'medicamentos': medicamentos,
                'receitas': receitas,
                'consultas': consultas,
                'sintomas': sintomas,
                'diagnosticos': diagnosticos,
                'exames': exames}

    def from_dict(dct: dict):
        new = Paciente(dct['nome'], dct['data_nascimento'])
        
        print(len(new.proficionais))
        for k in list(dct['proficionais'].keys()):
            new.proficionais[len(new.proficionais)] = Proficional.from_dict(dct['proficionais'][k])
        
        print('medicamentos', len(new.medicamentos))
        for k in list(dct['medicamentos'].keys()):
            new.medicamentos[len(new.medicamentos)] = Medicamento.from_dict(dct['medicamentos'][k])
        
        print('receitas', len(new.receitas))
        for k in list(dct['receitas'].keys()):
            new.receitas[len(new.receitas)] = Receita.from_dict(dct['receitas'][k])
        
        print('consultas', len(new.consultas))
        for k in list(dct['consultas'].keys()):
            new.consultas[len(new.consultas)] = Consulta.from_dict(dct['consultas'][k])
        
        print('sintomas', len(new.sintomas))
        for k in list(dct['sintomas'].keys()):
            new.sintomas[len(new.sintomas)] = Sintoma.from_dict(dct['sintomas'][k])

        print('diagnosticos', len(new.diagnosticos))
        for k in list(dct['diagnosticos'].keys()):
            new.diagnosticos[len(new.diagnosticos)] = Doenca.from_dict(dct['diagnosticos'][k])
        
        print('exames', len(new.exames))
        for k in list(dct['exames'].keys()):
            new.exames[len(new.exames)] = Exame.from_dict(dct['exames'][k])

        print('peso', len(new.peso))
        for k in list(dct['peso'].keys()):
            new.peso[len(new.peso)] = {'data': date(*map(int, dct['peso'][k]['data'].split('-'))), 'valor': dct['peso'][k]['valor']}

        print('altura', len(new.altura))
        for k in list(dct['altura'].keys()):
            new.altura[len(new.altura)] = {'data': date(*map(int, dct['altura'][k]['data'].split('-'))), 'valor': dct['altura'][k]['valor']}  

        return new

    def register():
        nome = input('Nome: ')
        data_nsc = date(*map(int, input('Data de nascimento (AAAA/MM/DD): ').split('/')))
        peso = float(input('Peso: '))
        altura = float(input('Altura: '))
        return Paciente(nome, data_nsc, peso, altura)

    def __str__(self): 
        return  'Nome: ' + self.nome + \
                '\nData de nascimento: ' + str(self.data_nascimento) + \
                '\nPeso: ' + str(self.peso[max(self.peso.keys())]['valor']) + \
                '\nAltura: ' + str(self.altura[max(self.altura.keys())]['valor']) + \
                '\nConsultas: ' + str(len(self.consultas)) + \
                '\nProficionais: ' + str(len(self.proficionais)) + \
                '\nMedicamentos: ' + str(len(self.medicamentos)) + \
                '\nReceitas: ' + str(len(self.receitas)) + \
                '\nSintomas: ' + str(len(self.sintomas))

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
    medicamentos[0] = Medicamento('Amoxicilina 500mg + Clavulanato 125mg',30, 'comp', 8, 10)
    medicamentos[1] = Medicamento('Lisador', 1, 'caixa', 6, condicao='dor ou febre')
    medicamentos[2] = Medicamento('Predisim 20mg', 1, 'caixa', 12, 5)
    medicamentos[3] = Medicamento('Rinosoro Jet', 1, 'frasco', 8, condicao='sintomas')
    medicamentos[4] = Medicamento('Avamys', 1, 'frasco', 24, 30, condicao='noite')
    
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
    medicamentos[0] = Medicamento('Amoxicilina 500mg + Clavulanato 125mg',30, 'comp', 8, 10)
    medicamentos[1] = Medicamento('Lisador', 1, 'caixa', 6, condicao='dor ou febre')
    medicamentos[2] = Medicamento('Predisim 20mg', 1, 'caixa', 12, 5)
    medicamentos[3] = Medicamento('Rinosoro Jet', 1, 'frasco', 8, condicao='sintomas')
    medicamentos[4] = Medicamento('Avamys', 1, 'frasco', 24, 30, condicao='noite')
    
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
        print('Opções: 1- Acessar; 2- Cadastrar; 3- Sair')
        inp = input('\n> ')
        if inp == '1': # Acessar
            print('Acessar:\n0- Pular\n1- Proficional\n2- Medicamentos\n3- Receita\n4- Sintoma\n5- Doença\n6- Exame\n7- Consulta\n8- Paciente')
            inp = input('\n> ')
            
            if inp == '0': # Pular
                pass
            elif inp == '1': # Proficional
                if 'proficionais' in data_json.keys():
                    print('Proficionais:\n0 Pular')
                    for k in data_json['proficionais'].keys():
                        print(int(k)+1, data_json['proficionais'][k]['nome'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['proficionais'].keys():
                        p = Proficional.from_dict(data_json['proficionais'][str(inp)])
                        print(p)
                        inp = input('Atribuir à paciente? (s/n)\n> ')
                        if inp == 's':
                            if 'pacientes' in data_json.keys():
                                print('Pacientes:\n0 Pular')
                                for k in data_json['pacientes'].keys():
                                    print(int(k)+1, data_json['pacientes'][k]['nome'])
                                inp = str(int(input('\n> ')) - 1)
                                if inp in data_json['pacientes'].keys():
                                    paciente = Paciente.from_dict(data_json['pacientes'][str(inp)])
                                    paciente.add_proficional(p)
                                    data_json['pacientes'][str(inp)] = paciente.as_dict()
                                    save_json(data_json)
                            else:
                                print('Não há pacientes cadastrados.')          
                else:
                    print('Não há proficionais cadastrados.')
            elif inp == '2': # Medicamento
                if 'medicamentos' in data_json.keys():
                    print('Medicamentos:\n0 Pular')
                    for k in data_json['medicamentos'].keys():
                        print(int(k)+1, data_json['medicamentos'][k]['nome'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['medicamentos'].keys():
                        p = Medicamento.from_dict(data_json['medicamentos'][str(inp)])
                        print(p)
                        inp = input('Atribuir à paciente? (s/n)\n> ')
                        if inp == 's':
                            if 'pacientes' in data_json.keys():
                                print('Pacientes:\n0 Pular')
                                for k in data_json['pacientes'].keys():
                                    print(int(k)+1, data_json['pacientes'][k]['nome'])
                                inp = str(int(input('\n> ')) - 1)
                                if inp in data_json['pacientes'].keys():
                                    paciente = Paciente.from_dict(data_json['pacientes'][str(inp)])
                                    paciente.add_medicamentos(p)
                                    data_json['pacientes'][str(inp)] = paciente.as_dict()
                                    save_json(data_json)
                            else:
                                print('Não há pacientes cadastrados.')
                else:
                    print('Não há medicamentos cadastrados.')
            elif inp == '3': # Receita
                if 'receitas' in data_json.keys():
                    print('Receitas:\n0 Pular')
                    for k in data_json['receitas'].keys():
                        print(int(k)+1, data_json['receitas'][k]['proficional']['nome'], data_json['receitas'][k]['data'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['receitas'].keys():
                        p = Receita.from_dict(data_json['receitas'][str(inp)])
                        print(p)
                        inp = input('Atribuir à paciente? (s/n)\n> ')
                        if inp == 's':
                            if 'pacientes' in data_json.keys():
                                print('Pacientes:\n0 Pular')
                                for k in data_json['pacientes'].keys():
                                    print(int(k)+1, data_json['pacientes'][k]['nome'])
                                inp = str(int(input('\n> ')) - 1)
                                if inp in data_json['pacientes'].keys():
                                    paciente = Paciente.from_dict(data_json['pacientes'][str(inp)])
                                    paciente.add_receita(p)
                                    data_json['pacientes'][str(inp)] = paciente.as_dict()
                                    save_json(data_json)
                            else:
                                print('Não há pacientes cadastrados.')
                else:
                    print('Não há receitas cadastradas.')
            elif inp == '4': # Sintoma
                if 'sintomas' in data_json.keys():
                    print('Sintomas:\n0 Pular')
                    for k in data_json['sintomas'].keys():
                        print(int(k)+1, data_json['sintomas'][k]['nome'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['sintomas'].keys():
                        p = Sintoma.from_dict(data_json['sintomas'][str(inp)])
                        print(p)
                        inp = input('Atribuir à paciente? (s/n)\n> ')
                        if inp == 's':
                            if 'pacientes' in data_json.keys():
                                print('Pacientes:\n0 Pular')
                                for k in data_json['pacientes'].keys():
                                    print(int(k)+1, data_json['pacientes'][k]['nome'])
                                inp = str(int(input('\n> ')) - 1)
                                if inp in data_json['pacientes'].keys():
                                    paciente = Paciente.from_dict(data_json['pacientes'][str(inp)])
                                    paciente.add_sintoma(p)
                                    data_json['pacientes'][str(inp)] = paciente.as_dict()
                                    save_json(data_json)
                            else:
                                print('Não há pacientes cadastrados.')
                else:
                    print('Não há sintomas cadastrados.')
            elif inp == '5': # Doenca
                if 'doencas' in data_json.keys():
                    print('Doenças:\n0 Pular')
                    for k in data_json['doencas'].keys():
                        print(int(k)+1, data_json['doencas'][k]['nome'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['doencas'].keys():
                        p = Doenca.from_dict(data_json['doencas'][str(inp)])
                        print(p)
                        inp = input('Atribuir à paciente? (s/n)\n> ')
                        if inp == 's':
                            if 'pacientes' in data_json.keys():
                                print('Pacientes:\n0 Pular')
                                for k in data_json['pacientes'].keys():
                                    print(int(k)+1, data_json['pacientes'][k]['nome'])
                                inp = str(int(input('\n> ')) - 1)
                                if inp in data_json['pacientes'].keys():
                                    paciente = Paciente.from_dict(data_json['pacientes'][str(inp)])
                                    paciente.add_doenca(p)
                                    data_json['pacientes'][str(inp)] = paciente.as_dict()
                                    save_json(data_json)
                            else:
                                print('Não há pacientes cadastrados.')
                else:
                    print('Não há doenças cadastradas.')
            elif inp == '6': # Exame
                if 'exames' in data_json.keys():
                    print('Exames:\n0 Pular')
                    for k in data_json['exames'].keys():
                        print(int(k)+1, data_json['exames'][k]['nome'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['exames'].keys():
                        p = Exame.from_dict(data_json['exames'][str(inp)])
                        print(p)
                        inp = input('Atribuir à paciente? (s/n)\n> ')
                        if inp == 's':
                            if 'pacientes' in data_json.keys():
                                print('Pacientes:\n0 Pular')
                                for k in data_json['pacientes'].keys():
                                    print(int(k)+1, data_json['pacientes'][k]['nome'])
                                inp = str(int(input('\n> ')) - 1)
                                if inp in data_json['pacientes'].keys():
                                    paciente = Paciente.from_dict(data_json['pacientes'][str(inp)])
                                    paciente.add_exame(p)
                                    data_json['pacientes'][str(inp)] = paciente.as_dict()
                                    save_json(data_json)
                            else:
                                print('Não há pacientes cadastrados.')
                else:
                    print('Não há exames cadastrados.')
            elif inp == '7': # Consulta
                if 'consultas' in data_json.keys():
                    print('Consultas:\n0 Pular')
                    for k in data_json['consultas'].keys():
                        print(int(k)+1, data_json['consultas'][k]['proficional']['nome'], data_json['consultas'][k]['data'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['consultas'].keys():
                        p = Consulta.from_dict(data_json['consultas'][str(inp)])
                        print(p)
                        inp = input('Atribuir à paciente? (s/n)\n> ')
                        if inp == 's':
                            if 'pacientes' in data_json.keys():
                                print('Pacientes:\n0 Pular')
                                for k in data_json['pacientes'].keys():
                                    print(int(k)+1, data_json['pacientes'][k]['nome'])
                                inp = str(int(input('\n> ')) - 1)
                                if inp in data_json['pacientes'].keys():
                                    paciente = Paciente.from_dict(data_json['pacientes'][str(inp)])
                                    paciente.add_consulta(p)
                                    data_json['pacientes'][str(inp)] = paciente.as_dict()
                                    save_json(data_json)
                            else:
                                print('Não há pacientes cadastrados.')
                else:
                    print('Não há consultas cadastradas.')
            elif inp == '8': # Paciente
                if 'pacientes' in data_json.keys():
                    print('Pacientes:\n0 Pular')
                    for k in data_json['pacientes'].keys():
                        print(int(k)+1, data_json['pacientes'][k]['nome'])
                    inp = int(input('\n> ')) - 1
                    p = Paciente.from_dict(data_json['pacientes'][str(inp)])
                    print(p)
                    if len(p.consultas) + len(p.proficionais) + len(p.medicamentos) + len(p.receitas) + len(p.sintomas) > 0:
                        print('Listar:\n0 Pular\n1 Consultas\n2 Proficionais\n3 Medicamentos\n4 Receitas\n5 Sintomas')
                        inp = input('\n> ')
                        if inp == '0':
                            pass
                        elif inp == '1':
                            for k in p.consultas.keys():
                                print(int(k)+1, p.consultas[k].data, p.consultas[k].proficional.nome)
                        elif inp == '2':
                            for k in p.proficionais.keys():
                                print(int(k)+1, p.proficionais[k].nome)
                        elif inp == '3':
                            for k in p.medicamentos.keys():
                                print(int(k)+1, p.medicamentos[k].nome, p.medicamentos[k].data)
                        elif inp == '4':
                            for k in p.receitas.keys():
                                print(int(k)+1, p.receitas[k].nome)
                        elif inp == '5':
                            for k in p.sintomas.keys():
                                print(int(k)+1, p.sintomas[k].nome, p.sintomas[k].data)
                    input()
                else:
                    print('Não há pacientes cadastrados.')
         
        elif inp == '2': # Cadastrar
            print('Cadastrar:\n0- Pular\n1- Proficional\n2- Medicamentos\n3- Receita\n4- Sintoma\n5- Doença\n6- Exame\n7- Consulta\n8- Paciente')
            inp = input('\n> ')
            if inp  == '0':
                pass
            elif inp == '1': # Proficional
                new = Proficional.register()
                if 'proficionais' in data_json.keys():
                    data_json['proficionais'][len(data_json['proficionais'].keys())] = new.as_dict()
                else:
                    data_json['proficionais'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '2': # Medicamentos
                new = Medicamento.register()
                if 'medicamentos' in data_json.keys():
                    data_json['medicamentos'][len(data_json['medicamentos'].keys())] = new.as_dict()
                else:
                    data_json['medicamentos'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '3': # Receita
                new, data_json = Receita.register(data_json)
                if 'receitas' in data_json.keys():
                    data_json['receitas'][len(data_json['receitas'].keys())] = new.as_dict()
                else:
                    data_json['receitas'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '4': # Sintoma
                new = Sintoma.register()
                if 'sintomas' in data_json.keys():
                    data_json['sintomas'][len(data_json['sintomas'].keys())] = new.as_dict()
                else:
                    data_json['sintomas'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '5': # Doença
                new = Doenca.register()
                if 'doencas' in data_json.keys():
                    data_json['doencas'][len(data_json['doencas'].keys())] = new.as_dict()
                else:
                    data_json['doencas'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '6': # Exame
                new, data_json = Exame.register(data_json)
                if 'exames' in data_json.keys():
                    data_json['exames'][len(data_json['exames'].keys())] = new.as_dict()
                else:
                    data_json['exames'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '7': # Consulta
                new, data_json = Consulta.register(data_json)
                if 'consultas' in data_json.keys():
                    data_json['consultas'][len(data_json['consultas'].keys())] = new.as_dict()
                else:
                    data_json['consultas'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '8': # Paciente
                new = Paciente.register()
                if 'pacientes' in data_json.keys():
                    data_json['pacientes'][len(data_json['pacientes'].keys())] = new.as_dict()
                else:
                    data_json['pacientes'] = {'0' : new.as_dict()}
                save_json(data_json)

        elif inp == '3': # Sair
            break

if __name__ == '__main__':
    main()

# Falta:

# Interface

# Opções para adicionar ao paciente