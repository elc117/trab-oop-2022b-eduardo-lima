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

    def from_dict(dct):
        return Medicacao(dct['nome'], dct['qnt'], dct['un'], dct['intervalo'], dct['duracao'], dct['condicao'])

    def register():
        nome = input('Nome: ')
        qnt = input('Quantidade: ')
        un = input('Unidade: ')
        intervalo = input('Intervalo: ')
        duracao = input('Duração: ')
        condicao = input('Condição: ')
        return Medicacao(nome, qnt, un, intervalo, duracao, condicao)

    def __str__(self):
        qnt = '\t{}'.format(self.qnt) if self.qnt != None and self.qnt != '' else ''
        un = self.un if self.un != None and self.un != '' else ''
        intervalo = '\na cada {} horas'.format(self.intervalo) if self.intervalo != None and self.intervalo != '' else ''
        duracao = 'durante {} dias'.format(self.duracao) if self.duracao != None and self.duracao != '' else ''
        condicao = '\nquando: {}'.format(self.condicao) if self.condicao != None and self.condicao != '' else ''

        return '{} {} {} {} {} {}'.format(self.nome, qnt, un, intervalo, duracao, condicao)

class Receita:
    def __init__(self, proficional: Proficional, data: date, medicacao: dict = {}):
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

    def add_medicacao(self, medicacao: Medicacao):
        self.medicacao[len(self.medicacao)] = medicacao

    def from_dict(dct):
        new = Receita(Proficional.from_dict(dct['proficional']), date(*map(int, dct['data'].split('-'))))
        for k in dct['medicacao'].keys():
            new.add_medicacao(Medicacao.from_dict(dct['medicacao'][k]))
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
                        data_json['proficionais'][str(len(data_json['proficionais']))] = proficional.as_dict()
        else:
            proficional = Proficional.register()
            data_json['proficionais'] = {'0' : proficional.as_dict()}
        data = input('\nData da receita (AAAA/MM/DD) ou vazio para data atual: ')
        if data == '':
            data = date.today()
        else:
            data = date(*map(int, data.split('/')))
        medicacao = {}
        print('\nMedicamento(s):')
        while True:
            if 'medicamentos' in data_json.keys():
                    print('0 Cadastrar novo')
                    for k in data_json['medicamentos'].keys():
                        print(int(k)+1, data_json['medicamentos'][k]['nome'])
                    inp = int(input('\n> ')) - 1
                    if inp > -1:
                        medicacao[str(len(medicacao))] = Medicacao.from_dict(data_json['medicamentos'][str(inp)])
                    else:
                        medicacao[str(len(medicacao))] = Medicacao.register()
                        data_json['medicamentos'][str(len(data_json['medicamentos']))] = medicacao[str(len(medicacao)-1)].as_dict()
            else:
                medicacao[str(len(medicacao))] = Medicacao.register()
                data_json['medicamentos'] = {'0' : medicacao[str(len(medicacao)-1)].as_dict()}
            inp = input('\n1- Adicionar mais; 2- Finalizar\n> ')
            if inp == '2':
                break
        return Receita(proficional, data, medicacao), data_json

    def __str__(self):
        s = '{}\n{}\n\n'.format(self.data, str(Proficional.from_dict(self.proficional)))
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
                        proficional = Proficional.from_dict(data_json['proficionais'][str(inp)])
                    else:
                        proficional = Proficional.register()
                        data_json['proficionais'][str(len(data_json['proficionais']))] = proficional.as_dict()
        else:
            print('Cadastrar médico:')
            proficional = Proficional.register()
            data_json['proficionais'] = {'0' : proficional.as_dict()}
        data = input('Data do exame (AAAA/MM/DD) ou vazio para data atual: ')
        if data == '':
            data = date.today()
        else:
            data = date(*map(int, data.split('/')))
        return Exame(nome, proficional, data)

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

    def from_dict(dct):
        sintomas = {}
        for k in dct['sintomas'].keys():
            sintomas[k] = dct['sintomas'][k].from_dict()
        return Consulta(dct['proficional'], dct['local'], sintomas, date(dct['data']), dct['receita'].from_dict(),
                dct['diagnostico'].from_dict() if dct['diagnostico'].from_dict() != None else None,
                dct['exame'].from_dict() if dct['exame'].from_dict() != None else None)

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
        print('Opções: 1- Acessar; 2- Cadastrar; 3- Sair')
        inp = input('\n> ')
        if inp == '1': # Acessar
            print('Acessar:\n0- Pular\n1- Proficional\n2- Medicação\n3- Receita\n4- Sintoma\n5- Doença\n6- Exame\n7- Consulta\n8- Paciente')
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
                        p = Proficional.from_dict(data_json['proficionais'][inp])
                        print(p)
                else:
                    print('Não há proficionais cadastrados.')
            elif inp == '2': # Medicamento
                if 'medicamentos' in data_json.keys():
                    print('Medicamentos:\n0 Pular')
                    for k in data_json['medicamentos'].keys():
                        print(int(k)+1, data_json['medicamentos'][k]['nome'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['medicamentos'].keys():
                        p = Medicacao.from_dict(data_json['medicamentos'][inp])
                        print(p)
                else:
                    print('Não há medicamentos cadastrados.')
            elif inp == '3': # Receita
                if 'receitas' in data_json.keys():
                    print('Receitas:\n0 Pular')
                    for k in data_json['receitas'].keys():
                        print(int(k)+1, data_json['receitas'][k]['proficional']['nome'], data_json['receitas'][k]['data'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['receitas'].keys():
                        p = Receita.from_dict(data_json['receitas'][inp])
                        print(p)
                else:
                    print('Não há receitas cadastradas.')
            elif inp == '4': # Sintoma
                if 'sintomas' in data_json.keys():
                    print('Sintomas:\n0 Pular')
                    for k in data_json['sintomas'].keys():
                        print(int(k)+1, data_json['sintomas'][k]['nome'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['sintomas'].keys():
                        p = Sintoma.from_dict(data_json['sintomas'][inp])
                        print(p)
                else:
                    print('Não há sintomas cadastrados.')
            elif inp == '5': # Doenca
                if 'doencas' in data_json.keys():
                    print('Doenças:\n0 Pular')
                    for k in data_json['doencas'].keys():
                        print(int(k)+1, data_json['doencas'][k]['nome'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['doencas'].keys():
                        p = Doenca.from_dict(data_json['doencas'][inp])
                        print(p)
                else:
                    print('Não há doenças cadastradas.')
            elif inp == '6': # Exame
                if 'exames' in data_json.keys():
                    print('Exames:\n0 Pular')
                    for k in data_json['exames'].keys():
                        print(int(k)+1, data_json['exames'][k]['nome'])
                    inp = str(int(input('\n> ')) - 1)
                    if inp in data_json['exames'].keys():
                        p = Exame.from_dict(data_json['exames'][inp])
                        print(p)
                else:
                    print('Não há exames cadastrados.')
            elif inp == '7': # Consulta
                if 'consultas' in data_json.keys():
                    print('Consultas:')
                    for k in data_json['consultas'].keys():
                        print(int(k)+1, data_json['consultas'][k]['nome'])
                    inp = int(input('\n> ')) - 1
                    p = Consulta.from_dict(data_json['consultas'][str(inp)])
                    print(p)
                else:
                    print('Não há consultas cadastradas.')
            elif inp == '8': # Paciente
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
            print('Cadastrar:\n0- Pular\n1- Proficional\n2- Medicação\n3- Receita\n4- Sintoma\n5- Doença\n6- Exame\n7- Consulta\n8- Paciente')
            inp = input('\n> ')
            if inp  == '0':
                pass
            elif inp == '1': # Proficional
                new = Proficional.register()
                if 'proficionais' in data_json.keys():
                    data_json['proficionais'][str(len(data_json['proficionais'].keys()))] = new.as_dict()
                else:
                    data_json['proficionais'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '2': # Medicação
                new = Medicacao.register()
                if 'medicamentos' in data_json.keys():
                    data_json['medicamentos'][str(len(data_json['medicamentos'].keys()))] = new.as_dict()
                else:
                    data_json['medicamentos'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '3': # Receita
                new, data_json = Receita.register(data_json)
                if 'receitas' in data_json.keys():
                    data_json['receitas'][str(len(data_json['receitas'].keys()))] = new.as_dict()
                else:
                    data_json['receitas'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '4': # Sintoma
                new = Sintoma.register()
                if 'sintomas' in data_json.keys():
                    data_json['sintomas'][str(len(data_json['sintomas'].keys()))] = new.as_dict()
                else:
                    data_json['sintomas'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '5': # Doença
                new = Doenca.register()
                if 'doencas' in data_json.keys():
                    data_json['doencas'][str(len(data_json['doencas'].keys()))] = new.as_dict()
                else:
                    data_json['doencas'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '6': # Exame
                new = Exame.register(data_json)
                if 'exames' in data_json.keys():
                    data_json['exames'][str(len(data_json['exames'].keys()))] = new.as_dict()
                else:
                    data_json['exames'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '7': # Consulta
                new = Consulta.register()
                if 'consultas' in data_json.keys():
                    data_json['exames'][str(len(data_json['consultas'].keys()))] = new.as_dict()
                else:
                    data_json['consultas'] = {'0' : new.as_dict()}
                save_json(data_json)
            elif inp == '8': # Paciente
                new = Paciente.register()
                if 'pacientes' in data_json.keys():
                    data_json['pacientes'][str(len(data_json['pacientes'].keys()))] = new.as_dict()
                else:
                    data_json['pacientes'] = {'0' : new.as_dict()}
                save_json(data_json)

        elif inp == '3': # Sair
            break

main()

# Falta:

# Interface
#   Doença
#   Exame

# Funções register()
#   Consulta