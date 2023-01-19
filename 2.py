import json
import os

# Classe base para representar um objeto no CRUD
class Object:
    def create(self):
        pass
    
    def read(self):
        pass
    
    def update(self):
        pass
    
    def delete(self):
        pass
    
    def __dict__(self):
        pass

    def __str__(self):
        pass

# Classe para representar um profissional
class Professional(Object):
    def __init__(self, name, specialty, city, phone):
        self.name = name
        self.specialty = specialty
        self.city = city
        self.phone = phone
    
    def create(self):
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para adicionar um novo profissional aos dados
        data['professionals'].append(self.__dict__())
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)

        return self

    def read(self):
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um profissional com o nome especificado
        for professional in data['professionals']:
            if professional['name'] == self.name and professional['specialty'] == self.specialty and professional['city'] == self.city:
                return professional
        
        # Caso o profissional não seja encontrado, retornar None
        return None

    def update(self, new_name=None, new_specialty=None, new_city=None, new_phone=None):
        if new_name is None:
            new_name = self.name
        if new_specialty is None:
            new_specialty = self.specialty
        if new_city is None:
            new_city = self.city
        if new_phone is None:
            new_phone = self.phone
        
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um profissional com o nome especificado
        # e atualizar os dados do profissional
        
        for i, professional in enumerate(data['professionals']):
            if professional['name'] == self.name and professional['specialty'] == self.specialty and professional['city'] == self.city:
                self = Professional(new_name, new_specialty, new_city, new_phone)
                data['professionals'][i] = self.__dict__()
                print('Professional updated successfully!')
                
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def delete(self):
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um profissional com o nome especificado
        # e excluir o profissional dos dados
        for i, professional in enumerate(data['professionals']):
            if professional['name'] == self.name and professional['specialty'] == self.specialty and professional['city'] == self.city:
                del data['professionals'][i]
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def __dict__(self):
        return {
            'name': self.name,
            'specialty': self.specialty,
            'city': self.city,
            'phone': self.phone
        }
    
    def __str__(self):
        return f'{self.name} ({self.specialty}) - {self.city} - {self.phone}'

# Classe para representar um medicamento
class Medicine(Object):
    def __init__(self, name, qnt, un, interval, duration, condition):
        '''
        name: Armazena o nome do medicamento. Esse atributo é utilizado para identificar o medicamento.
        qnt: Armazena a quantidade do medicamento. Esse atributo é utilizado para informar a quantidade de medicamento que deve ser tomada em cada dose.
        un: Armazena a unidade da quantidade do medicamento. Esse atributo é utilizado para informar a unidade de medida da quantidade de medicamento (por exemplo, comprimidos, ml, etc.).
        interval: Armazena o intervalo em horas em que o medicamento deve ser tomado. Esse atributo é utilizado para informar quanto tempo deve passar entre as doses de medicamento.
        duration: Armazena a duração em dias em que o medicamento deve ser tomado. Esse atributo é utilizado para informar por quantos dias o medicamento deve ser tomado.
        condition: Armazena a condição para tomar o medicamento. Esse atributo é utilizado para informar quais são as condições específicas em que o medicamento deve ser utilizado.
        '''
        self.name = name
        self.qnt = qnt
        self.un = un
        self.interval = interval
        self.duration = duration
        self.condition = condition
    
    def create(self):
        # Código para criar um novo medicamento no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para adicionar um novo medicamento aos dados
        data['medicines'].append(self.__dict__())

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def read(self):
        # Código para ler um medicamento existente do sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um medicamento com o nome especificado
        for medicine in data['medicines']:
            if medicine['name'] == self.name and medicine['qnt'] == self.qnt and medicine['un'] == self.un and medicine['interval'] == self.interval and medicine['duration'] == self.duration and medicine['condition'] == self.condition:
                return medicine
        
        # Caso o medicamento não seja encontrado, retornar None
        return None
    
    def update(self, new_name=None, new_qnt=None, new_un=None, new_interval=None, new_duration=None, new_condition=None):
        # Código para atualizar um medicamento existente no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        if new_name is None:
            new_name = self.name
        if new_qnt is None:
            new_qnt = self.qnt
        if new_un is None:
            new_un = self.un
        if new_interval is None:
            new_interval = self.interval
        if new_duration is None:
            new_duration = self.duration
        if new_condition is None:
            new_condition = self.condition

        # Código para procurar um medicamento com o nome especificado
        # e atualizar os dados do medicamento
        for i, medicine in enumerate(data['medicines']):
            if medicine['name'] == self.name and medicine['qnt'] == self.qnt and medicine['un'] == self.un and medicine['interval'] == self.interval and medicine['duration'] == self.duration and medicine['condition'] == self.condition:
                self = Medicine(new_name, new_qnt, new_un, new_interval, new_duration, new_condition)
                data['medicines'][i] = self.__dict__()
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def delete(self):
        # Código para excluir um medicamento existente do sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um medicamento com o nome especificado
        # e excluir o medicamento dos dados
        for i, medicine in enumerate(data['medicines']):
            if medicine['name'] == self.name and medicine['qnt'] == self.qnt and medicine['un'] == self.un and medicine['interval'] == self.interval and medicine['duration'] == self.duration and medicine['condition'] == self.condition:
                del data['medicines'][i]
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def __dict__(self):
        return {
            'name': self.name,
            'qnt': self.qnt,
            'un': self.un,
            'interval': self.interval,
            'duration': self.duration,
            'condition': self.condition
        }

    def __str__(self):
        return f'{self.name} - {self.qnt} {self.un}\n   {self.interval}h - {self.duration}d\n   {self.condition}'

# Classe para representar uma receita
class Prescription(Object):
    def __init__(self, professional: str, patient: str, medicines: list, date: str):
        self.professional = professional
        self.patient = patient
        self.medicines = medicines
        self.date = date
    
    def create(self):
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para adicionar uma nova receita aos dados
        data['prescriptions'].append(self.__dict__())
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def read(self):
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar uma receita com o nome do paciente especificado
        for prescription in data['prescriptions']:
            if prescription['patient'] == self.patient:
                return prescription
        
        # Caso a receita não seja encontrada, retornar None
        return None
    
    def update(self, new_professional=None, new_patient=None, new_medicines=None, new_date=None):
        if new_professional is None:
            new_professional = self.professional
        if new_patient is None:
            new_patient = self.patient
        if new_medicines is None:
            new_medicines = self.medicines
        if new_date is None:
            new_date = self.date

        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar uma receita com o nome do paciente especificado
        # e atualizar os dados da receita
        for i, prescription in enumerate(data['prescriptions']):
            if prescription['patient'] == self.patient:
                self = Prescription(new_professional, new_patient, new_medicines, new_date)
                data['prescriptions'][i] = self.__dict__()
                
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def delete(self):
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar uma receita com o nome do paciente especificado
        # e excluir a receita dos dados
        for i, prescription in enumerate(data['prescriptions']):
            if prescription['patient'] == self.patient:
                del data['prescriptions'][i]
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def __dict__(self):
        return {
            'professional': self.professional,
            'patient': self.patient,
            'medicines': self.medicines,
            'date': self.date
        }
    
    def __str__(self):
        s = f'{self.professional}\nPaciente: {self.patient}\n{self.date}\n'
        for medicine_dict in self.medicines:
            medicine = Medicine(medicine_dict['name'], medicine_dict['qnt'], medicine_dict['un'], medicine_dict['interval'], medicine_dict['duration'], medicine_dict['condition'])
            s += medicine.__str__() + '\n'
        return s
        
# Classe para representar um sintoma
class Symptom(Object):
    def __init__(self, name, date):
        self.name = name
        self.date = date
    
    def create(self):
        # Código para criar um novo sintoma no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para adicionar um novo sintoma aos dados
        data['symptoms'].append(self.__dict__())

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
            
    def read(self):
        # Código para ler um sintoma existente do sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um sintoma com o nome especificado
        for symptom in data['symptoms']:
            if symptom['name'] == self.name:
                return symptom
        
        # Caso o sintoma não seja encontrado, retornar None
        return None
    
    def update(self, new_name=None, new_date=None):
        if new_name is None:
            new_name = self.name
        if new_date is None:
            new_date = self.date

        # Código para atualizar um sintoma existente no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um sintoma com o nome especificado
        # e atualizar os dados do sintoma
        for i, symptom in enumerate(data['symptoms']):
            if symptom['name'] == self.name:
                self = Symptom(new_name, new_date)
                data['symptoms'][i] = self.__dict__()
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def delete(self):
        # Código para excluir um sintoma existente do sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um sintoma com o nome especificado
        # e excluir o sintoma dos dados
        for i, symptom in enumerate(data['symptoms']):
            if symptom['name'] == self.name:
                del data['symptoms'][i]
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def __dict__(self):
        return {
            'name': self.name,
            'date': self.date
        }

    def __str__(self):
        return f'{self.name} - {self.date}'

# Classe para representar uma doença
class Disease(Object):
    def __init__(self, name, symptoms, date):
        self.name = name
        self.symptoms = symptoms
        self.date = date
    
    def create(self):
        # Código para criar uma nova doença no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Código para adicionar uma nova doença aos dados
        data['diseases'].append(self.__dict__())

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def read(self):
        # Código para ler uma doença existente do sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar uma doença com o nome especificado
        for disease in data['diseases']:
            if disease['name'] == self.name:
                return disease
        
        # Caso a doença não seja encontrada, retornar None
        return None
    
    def update(self, new_name=None, new_symptoms=None, new_date=None):
        if new_name is None:
            new_name = self.name
        if new_symptoms is None:
            new_symptoms = self.symptoms
        if new_date is None:
            new_date = self.date
        
        # Código para atualizar uma doença existente no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar uma doença com o nome especificado
        # e atualizar os dados da doença
        for i, disease in enumerate(data['diseases']):
            if disease['name'] == self.name:
                self = Disease(new_name, new_symptoms, new_date)
                data['diseases'][i] = self.__dict__()
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def delete(self):
        # Código para excluir uma doença existente do sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar uma doença com o nome especificado
        # e excluir a doença dos dados
        for i, disease in enumerate(data['diseases']):
            if disease['name'] == self.name:
                del data['diseases'][i]
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def __dict__(self):
        return {
            'name': self.name,
            'symptoms': self.symptoms,
            'date': self.date
        }

    def __str__(self):
        return f'{self.name} - {self.symptoms} - {self.date}'

# Classe para representar um exame
class Exam(Object):
    def __init__(self, name, results, professional, date):
        self.name = name
        self.results = results
        self.professional = professional
        self.date = date
    
    def create(self):
        # Código para criar um novo exame no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para adicionar um novo exame aos dados
        data['exams'].append(self.__dict__())

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def read(self):
        # Código para ler um exame existente do sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um exame com o nome especificado
        for exam in data['exams']:
            if exam['name'] == self.name:
                return exam
        
        # Caso o exame não seja encontrado, retornar None
        return None
    
    def update(self, new_name=None, new_results=None, new_professional=None, new_date=None):
        # Código para atualizar um exame existente no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um exame com o nome especificado
        # e atualizar os dados do exame
        for i, exam in enumerate(data['exams']):
            if exam['name'] == self.name:
                self = Exam(new_name, new_results, new_professional, new_date)
                data['exams'][i] = self.__dict__()
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def delete(self):
        # Código para excluir um exame existente do sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um exame com o nome especificado
        # e excluir o exame dos dados
        for i, exam in enumerate(data['exams']):
            if exam['name'] == self.name:
                del data['exams'][i]
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def __dict__(self):
        return {
            'name': self.name,
            'results': self.results,
            'professional': self.professional,
            'date': self.date
        }

    def __str__(self):
        return f'{self.name} - {self.results} - {self.professional} - {self.date}'

# Classe para representar uma consulta
class Consultation(Object):
    def __init__(self, professional, symptoms, diagnoses, exams, date):
        self.professional = professional
        self.symptoms = symptoms
        self.diagnoses = diagnoses
        self.exams = exams
        self.date = date
    
    def create(self):
        # Código para criar uma nova consulta no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para adicionar uma nova consulta aos dados
        data['consultations'].append(self.__dict__())

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def read(self):
        # Código para ler uma consulta existente do sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar uma consulta com o nome do paciente especificado
        for consultation in data['consultations']:
            if consultation['professional'] == self.patient and consultation['data'] == self.data:
                return consultation
        
        # Caso a consulta não seja encontrada, retornar None
        return None
    
    def update(self, new_professional=None, new_symptoms=None, new_diagnoses=None, new_exams=None, new_date=None):
        # Código para atualizar uma consulta existente no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar uma consulta com o nome do paciente especificado
        # e atualizar os dados da consulta
        for i, consultation in enumerate(data['consultations']):
            if consultation['professional'] == self.patient and consultation['data'] == self.data:
                self = Consultation(new_professional, new_symptoms, new_diagnoses, new_exams, new_date)
                data['consultations'][i] = self.__dict__()
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
              
    def delete(self):
        # Código para excluir uma consulta existente do sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar uma consulta com o nome do paciente especificado
        # e excluir a consulta dos dados
        for i, consultation in enumerate(data['consultations']):
            if consultation['professional'] == self.patient and consultation['data'] == self.data:
                del data['consultations'][i]
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def __dict__(self):
        return {
            'professional': self.professional,
            'symptoms': self.symptoms,
            'diagnoses': self.diagnoses,
            'exams': self.exams,
            'date': self.date
        }

    def __str__(self):
        return f'{self.professional} - {self.symptoms} - {self.diagnoses} - {self.exams} - {self.date}'

# Classe para representar um paciente
class Patient(Object):
    weight = []
    height = []

    professionals = []
    medicines = []
    perscriptions = []
    symptoms = []
    diseases = []
    exams = []

    def __init__(self, name, birth_date, gender):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
    
    def create(self):
        # Código para criar um novo paciente no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para adicionar um novo paciente aos dados
        data['patients'].append(self.__dict__())

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def read(self):
        # Código para ler um paciente existente do sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um paciente com o nome especificado
        for patient in data['patients']:
            if patient['name'] == self.name:
                return patient
        
        # Caso o paciente não seja encontrado, retornar None
        return None
    
    def update(self):
        # Código para atualizar um paciente existente no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um paciente com o nome especificado
        # e atualizar os dados do paciente
        for i, patient in enumerate(data['patients']):
            if patient['name'] == self.name:
                data['patients'][i] = self.__dict__()
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)
        
        return self
    
    def delete(self):
        # Código para excluir um paciente existente do
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar um paciente com o nome especificado
        # e excluir o paciente dos dados
        for i, patient in enumerate(data['patients']):
            if patient['name'] == self.name:
                del data['patients'][i]
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def __dict__(self):
        return {
            'name': self.name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'weight': self.weight,
            'height': self.height,
            'professionals': self.professionals,
            'medicines': self.medicines,
            'perscriptions': self.perscriptions,
            'symptoms': self.symptoms,
            'diseases': self.diseases,
            'exams': self.exams
        }

    def __str__(self):
        return f'{self.name} - {self.birth_date}'

# ------ Função principal ------
def main():
    # Verifica se o arquivo JSON existe
    if not os.path.exists('data.json'):
        # Cria um arquivo JSON vazio
        with open('data.json', 'w') as f:
            json.dump({}, f)

    # Inicialização dos dados
    with open('data.json', 'r+') as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            data = {}
            json.dump(data, f)
    
    # Verifica se todas as chaves necessárias existem no arquivo JSON
    if 'professionals' not in data:
        data['professionals'] = []
    if 'medicines' not in data:
        data['medicines'] = []
    if 'prescriptions' not in data:
        data['prescriptions'] = []
    if 'symptoms' not in data:
        data['symptoms'] = []
    if 'diseases' not in data:
        data['diseases'] = []
    if 'exams' not in data:
        data['exams'] = []
    if 'consultations' not in data:
        data['consultations'] = []
    if 'patients' not in data:
        data['patients'] = []
    
    # Código para escrever os dados de volta para o arquivo JSON
    with open('data.json', 'w') as f:
        json.dump(data, f)

    while True:
        print("\nMenu de opções:")
        print("1. Gerenciar profissionais de saúde")
        print("2. Gerenciar medicamentos")
        print("3. Gerenciar receitas médicas")
        print("4. Gerenciar sintomas")
        print("5. Gerenciar doenças")
        print("6. Gerenciar exames")
        print("7. Gerenciar consultas")
        print("8. Gerenciar pacientes")
        print("9. Sair")
        
        option = input("\nEscolha uma opção: ")
        
        if option == "1":
            # Chama a função responsável por gerenciar profissionais de saúde
            manage_professionals()
        elif option == "2":
            # Chame a função responsável por gerenciar medicamentos
            manage_medicines()
        elif option == "3":
            # Chama a função responsável por gerenciar receitas médicas
            manage_prescriptions()
        elif option == "4":
            # Chama a função responsável por gerenciar sintomas
            manage_symptoms()
        elif option == "5":
            # Chama a função responsável por gerenciar doenças
            manage_diseases()
        elif option == "6":
            # Chama a função responsável por gerenciar exames
            manage_exams()
        elif option == "7":
            # Chama a função responsável por gerenciar consultas
            manage_consultations()
        elif option == "8":
            # Chama a função responsável por gerenciar pacientes
            manage_patients()
        elif option == "9":
            break
        else:
            print("Opção inválida. Tente novamente.")

# ------ Funções para manipular os dados de profissionais de saúde ------
def manage_professionals():
    print("\nMenu de opções para profissionais de saúde:")
    print("1. Cadastrar novo profissional")
    print("2. Listar profissionais")
    print("3. Atualizar profissional")
    print("4. Excluir profissional")
    print("5. Voltar ao menu principal")
    
    option = input("\nEscolha uma opção: ")

    if option == "1":
        # Chama a função para cadastrar profissionais
        register_professional()
    elif option == "2":
        # Chama a função para listar profissionais
        list_professionals()
    elif option == "3":
        # Chama a função para atualizar profissionais
        update_professional()
    elif option == "4":
        # Chama a função para excluir profissionais
        delete_professional()
    elif option == "5":
        # Volta ao menu principal
        return
    else:
        print("Opção inválida. Tente novamente.")
        manage_professionals()

def register_professional() -> Professional:
        # Código para cadastrar um novo profissional da saúde
        name = input("\nInsira o nome do profissional: ")
        specialty = input("Insira a especialidade do profissional: ")
        city = input("Insira a cidade do profissional: ")
        phone = input("Insira o telefone do profissional: ")
        professional = Professional(name, specialty, city, phone).create()
        print("\nProfissional cadastrado com sucesso!")
        print(professional)
        return professional

def list_professionals(l=None):
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['professionals'] = l

    # Verifica se existem profissionais cadastrados
    if len(data['professionals']) == 0:
        print("\nNão há profissionais registrados.")
        return None

    # Imprime os profissionais cadastrados
    print("\nProfissionais cadastrados:")
    for i, professional in enumerate(data['professionals']):
        print(f"{i+1}. {Professional(professional['name'], professional['specialty'], professional['city'], professional['phone'])}")

def choose_professional(l=None) -> int:
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['professionals'] = l
    
    # Verifica se existem profissionais cadastrados
    if len(data['professionals']) == 0:
        print("\nNão há profissionais registrados.")
        return None
    
    # Imprime os profissionais cadastrados
    list_professionals(l)
    
    # Código para escolher um profissional cadastrado no sistema
    option = input("\nEscolha o profissional: ")

    if option.isnumeric() and int(option) > 0 and int(option) <= len(data['professionals']):        
        return int(option) - 1
    else:
        print("Opção inválida. Tente novamente.")
        return choose_professional(l)

def update_professional(l=None) -> list[Professional]:
    # Código para atualizar um profissional cadastrado no sistema
    option = choose_professional(l)

    if option is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['professionals'] = l

        # Lê os novos dados do profissional
        name = input("\nInsira o nome do profissional (deixe em branco para manter o nome atual: {}): ".format(data['professionals'][option]['name']))
        if name == "":
            name = None
        specialty = input("Insira a especialidade do profissional (deixe em branco para manter a especialidade atual: {}): ".format(data['professionals'][option]['specialty']))
        if specialty == "":
            specialty = None
        city = input("Insira a cidade do profissional (deixe em branco para manter a cidade atual: {}): ".format(data['professionals'][option]['city']))
        if city == "":
            city = None
        phone = input("Insira o telefone do profissional: (deixe em branco para manter o telefone atual: {}): ".format(data['professionals'][option]['phone']))
        if phone == "":
            phone = None
        
        # Cria um objeto profissional e chama a função update
        professional = Professional(data['professionals'][option]['name'], data['professionals'][option]['specialty'], data['professionals'][option]['city'], data['professionals'][option]['phone'])
        professional = professional.update(name, specialty, city, phone)
        
        data['professionals'][option] = professional.__dict__()

        print("\nProfissional atualizado com sucesso!")
        print(professional)
        return data['professionals']

def delete_professional(l=None) -> list[Professional]:
    # Código para excluir um profissional existente no sistema
    option = choose_professional(l)

    if option is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['professionals'] = l

        # Imprime o profissional que será excluído e pede confirmação
        professional = Professional(data['professionals'][option]['name'], data['professionals'][option]['specialty'], data['professionals'][option]['city'], data['professionals'][option]['phone'])
        print(f"\nVocê deseja excluir o profissional abaixo?\n{professional}")
        confirm = input("Digite 'sim' para confirmar: ")
        if confirm != 'sim':
            print("\nExclusão cancelada.")
            return data['professionals']

        # Exclui o profissional
        professional.delete()
        if l is not None:
            data['professionals'].pop(option)
        print("\nProfissional excluído com sucesso!")
        return data['professionals']

# ------ Funções para manipular os dados de medicamentos ------
def manage_medicines():
    # Código para gerenciar os medicamentos
    print("\nMenu de opções para medicamentos:")
    print("1. Cadastrar novo medicamento")
    print("2. Listar medicamentos")
    print("3. Atualizar medicamento")
    print("4. Excluir medicamento")
    print("5. Voltar ao menu principal")

    option = input("\nEscolha uma opção: ")

    if option == "1":
        # Chama a função para cadastrar um novo medicamento
        register_medicine()
    elif option == "2":
        # Chama a função para listar os medicamentos
        list_medicines()
    elif option == "3":
        # Chama a função para atualizar um medicamento
        update_medicine()
    elif option == "4":
        # Chama a função para excluir um medicamento
        delete_medicine()
    elif option == "5":
        # Volta ao menu principal
        return
    else:
        print("Opção inválida. Tente novamente.")
        manage_medicines()

def register_medicine() -> Medicine:
    # Código para cadastrar um novo medicamento
    name = input("\nInsira o nome do medicamento: ")
    qnt = input("Insira a quantidade do medicamento: ")
    un = input("Insira a unidade de medida do medicamento: ")
    interval = input("Insira o intervalo de horas para tomar o medicamento: ")
    duration = input("Insira a duração do tratamento com o medicamento: ")
    condition = input("Insira as condições de uso do medicamento: ")

    medicine = Medicine(name, qnt, un, interval, duration, condition).create()

    print("\nMedicamento cadastrado com sucesso!")
    print(medicine)
    return medicine

def list_medicines(l=None, string=None):
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['medicines'] = l

    # Verifique se há medicamentos cadastrados
    if len(data['medicines']) == 0:
        print("\nNão há medicamentos cadastrados.")
        return None
    
    # Imprime as informações de cada medicamento
    if string == None:
        print("\nMedicamentos cadastrados:")
    else:
        print(string)
    for i, medicine in enumerate(data['medicines']):
        print(f"{i+1}. {Medicine(medicine['name'], medicine['qnt'], medicine['un'], medicine['interval'], medicine['duration'], medicine['condition'])}")

def choose_medicine(l=None, string=None) -> int:
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['medicines'] = l

    # Verifica se há medicamentos cadastrados
    if len(data['medicines']) == 0:
        print("\nNão há medicamentos cadastrados.")
        return None

    # Imprime os medicamentos cadastrados
    list_medicines(l, string)

    # Lê o índice do medicamento escolhido
    option = input("\nEscolha o medicamento: ")

    # Verifica se a opção é válida
    if option.isnumeric() and int(option) > 0 and int(option) <= len(data['medicines']):
        return int(option) - 1
    else:
        print("\nOpção inválida. Tente novamente.")
        return choose_medicine(l)

def update_medicine(l=None) -> list[Medicine]:
    # Código para atualizar um medicamento existente no sistema
    option = choose_medicine(l)

    if option is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['medicines'] = l

        # Lê os novos dados do medicamento
        name = input("\nInsira o novo nome do medicamento (deixe em branco para manter o nome atual: {}): ".format(data['medicines'][option]['name']))
        if name == "":
            name = None
        qnt = input("Insira a nova quantidade do medicamento (deixe em branco para manter a quantidade atual: {}): ".format(data['medicines'][option]['qnt']))
        if qnt == "":
            qnt = None
        un = input("Insira a nova unidade de medida do medicamento (deixe em branco para manter a unidade atual: {}): ".format(data['medicines'][option]['un']))
        if un == "":
            un = None
        interval = input("Insira o novo intervalo de horas para tomar o medicamento (deixe em branco para manter o intervalo atual: {}): ".format(data['medicines'][option]['interval']))
        if interval == "":
            interval = None
        duration = input("Insira a nova duração do tratamento com o medicamento (deixe em branco para manter a duração atual: {}): ".format(data['medicines'][option]['duration']))
        if duration == "":
            duration = None
        condition = input("Insira as novas condições de uso do medicamento (deixe em branco para manter as condições atuais: {}): ".format(data['medicines'][option]['condition']))
        if condition == "":
            condition = None
        
        # Cria um objeto do tipo Medicine e chamada a função update
        medicine = Medicine(data['medicines'][option]['name'], data['medicines'][option]['qnt'], data['medicines'][option]['un'], data['medicines'][option]['interval'], data['medicines'][option]['duration'], data['medicines'][option]['condition'])
        medicine = medicine.update(name, qnt, un, interval, duration, condition)
        
        data['medicines'][option] = medicine.__dict__()

        print("\nMedicamento atualizado com sucesso!")
        print(medicine)
        return data['medicines']
    else:
        print("\nMedicamento não atualizado.")
        return data['medicines']

def delete_medicine(l=None) -> list[Medicine]:
    # Código para excluir um medicamento existente no sistema
    option = choose_medicine(l)

    if option is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['medicines'] = l
            
        # Imprime o medicamento que será excluído e pede confirmação
        medicine = Medicine(data['medicines'][option]['name'], data['medicines'][option]['qnt'], data['medicines'][option]['un'], data['medicines'][option]['interval'], data['medicines'][option]['duration'], data['medicines'][option]['condition'])
        print(f"Você deseja excluit o medicamento abaixo?\n{medicine}")
        confirm = input("Digite 'sim' para confirmar: ")
        if confirm != "sim":
            print("\nExclusão cancelada.")
            return data['medicines']

        # Exclui o medicamento
        medicine.delete()
        if l is not None:
            data['medicines'].pop(option)
        print("\nMedicamento deletado com sucesso!")
        return data['medicines']

# ------ Funçõoes para manipular os dados de receitas ------
def manage_prescriptions():
    # Código para gerenciar as receitas
    print("\nMenu de opções para receitas:")
    print("1. Cadastrar nova receita")
    print("2. Listar receitas")
    print("3. Atualizar receita")
    print("4. Excluir receita")
    print("5. Voltar ao menu principal")

    option = input("\nEscolha uma opção: ")

    if option == "1":
        # Chama a função para cadastrar uma nova receita
        register_prescription()
    elif option == "2":
        # Chama a função para listar as receitas
        list_prescriptions()
    elif option == "3":
        # Chama a função para atualizar uma receita
        update_prescription()
    elif option == "4":
        # Chama a função para excluir uma receita
        delete_prescription()
    elif option == "5":
        # Volta ao menu principal
        return
    else:
        print("\nOpção inválida. Tente novamente.")
        manage_prescriptions()

def register_prescription() -> Prescription:
    # Código para cadastrar uma nova receita
    professional = input("Insira o nome do profissional que emitiu a receita: ")
    patient = input("Insira o nome do paciente: ")
    date = input("Insira a data da receita (dd/mm/aaaa): ")
    medicines = []

    # Lê os dados dos medicamentos
    while True:        
        print("\n1. Adicionar medicamento cadastrado")
        print("2. Cadastrar novo medicamento")
        print("3. Visualizar medicamentos adicionados")
        print("4. Editar medicamentos adicionados")
        print("5. Remover medicamentos adicionados")
        print("6. Finalizar cadastro da receita")

        option = input("\nEscolha uma opção: ")

        if option == "1":
            # Adiciona um medicamento cadastrado
            option = choose_medicine()
            if option is not None:
                # Código para ler os dados do arquivo JSON
                with open('data.json', 'r') as f:
                    data = json.load(f)
                
                medicine = Medicine(data['medicines'][option]['name'], data['medicines'][option]['qnt'], data['medicines'][option]['un'], data['medicines'][option]['interval'], data['medicines'][option]['duration'], data['medicines'][option]['condition'])
                medicines.append(medicine.__dict__())
                print("\nMedicamento {} adicionado com sucesso!".format(medicine.name))
        elif option == "2":
            # Cadastra um novo medicamento
            medicine = register_medicine()
            medicines.append(medicine.__dict__())
            print("\nMedicamento {} adicionado com sucesso!".format(medicine.name))
        elif option == "3":
            # Imprime os medicamentos adicionados
            list_medicines(medicines, "\nMedicamentos adicionados:")
        elif option == "4":
            # Edita os medicamentos adicionados
            medicines = update_medicine(medicines)
        elif option == "5":
            # Remove os medicamentos adicionados
            option = choose_medicine(medicines, "\nMedicamentos adicionados:")
            if option is not None:
                option_exclude = input("\nDeseja remover o medicamento {} do cadastro também? (s/n): ".format(medicines[option]['name']))
                if option_exclude == "s":
                    confirm = input("\nTem certeza que deseja remover o medicamento {} do cadastro? (s/n): ".format(medicines[option]['name']))
                    if confirm == "sim":
                        # Remove o medicamento do cadastro
                        Medicine(medicines[option]['name'], medicines[option]['qnt'], medicines[option]['un'], medicines[option]['interval'], medicines[option]['duration'], medicines[option]['condition']).delete()
                        print("\nMedicamento removido do cadastro com sucesso!")
                    medicines.pop(option)
                else:
                    # Remove o medicamento apenas da receita
                    medicines.pop(option)
                print("\nMedicamento removido da receita com sucesso!")
        elif option == "6":
            # Finaliza o cadastro da receita
            break
        else:
            print("\nOpção inválida.")
    
    # Cria um objeto do tipo Prescription e chama a função create
    prescription = Prescription(professional, patient, medicines, date)
    prescription.create()
    print("\nReceita cadastrada com sucesso!")
    print(prescription)

def list_prescriptions(l=None):
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['prescriptions'] = l
        
    # Verifica se existem receitas cadastradas
    if len(data['prescriptions']) == 0:
        print("\nNão existem receitas cadastradas no sistema.")
        return
    
    # Imprime as receitas cadastradas
    print("\nReceitas cadastradas:")
    for i, prescription in enumerate(data['prescriptions']):
        print(f"{i+1}. {Prescription(prescription['professional'], prescription['patient'], prescription['medicines'], prescription['date'])}")
    
def choose_prescription(l=None) -> int:
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['prescriptions'] = l
    
    # Verifica se existem receitas cadastradas
    if len(data['prescriptions']) == 0:
        print("\nNão existem receitas cadastradas no sistema.")
        return None
    
    # Imprime as receitas cadastradas
    print("\nReceitas cadastradas:")
    list_prescriptions(l)

    # Código para escolher uma receita cadastrada no sistema
    option = input("\nEscolha uma receita: ")

    # Verifica se a opção escolhida é válida
    if option.isnumeric() and int(option) > 0 and int(option) <= len(data['prescriptions']):
        return int(option) - 1
    else:
        print("\nOpção inválida. Tente novamente.")
        return choose_prescription(l)

def update_prescription(l=None) -> list[Prescription]:
    # Código para atualizar uma receita cadastrada no sistema
    choosed_prescription = choose_prescription(l)

    if choosed_prescription is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['prescriptions'] = l

        # Lê os novos dados da receita
        professional = input("Insira o nome do profissional que emitiu a receita (deixe em branco para manter o valor atual: {}): ".format(data['prescriptions'][choosed_prescription]['professional']))
        if professional == "":
            professional = None
        patient = input("Insira o nome do paciente (deixe em branco para manter o valor atual: {}): ".format(data['prescriptions'][choosed_prescription]['patient']))
        if patient == "":
            patient = None
        date = input("Insira a data da receita (dd/mm/aaaa) (deixe em branco para manter o valor atual: {}): ".format(data['prescriptions'][choosed_prescription]['date']))
        if date == "":
            date = None
        confirmation = input("Deseja alterar os medicamentos da receita? (s/n): ")
        if confirmation == "s":
            medicines = data['prescriptions'][choosed_prescription]['medicines']
            while True:
                print("\n1. Adicionar medicamento cadastrado")
                print("2. Cadastrar novo medicamento")
                print("3. Visualizar medicamentos na receita")
                print("4. Remover medicamento da receita")
                print("5. Finalizar edição da receita")

                option = input("\nEscolha uma opção: ")

                if option == "1":
                    # Adiciona um medicamento cadastrado
                    choosed_medicine = choose_medicine()
                    if choosed_medicine is not None:
                        with open('data.json', 'r') as f:
                            data = json.load(f)
                        medicine = {'name': data['medicines'][choosed_medicine]['name'], 'qnt': data['medicines'][choosed_medicine]['qnt'], 'un': data['medicines'][choosed_medicine]['un'], 'interval': data['medicines'][choosed_medicine]['interval'], 'duration': data['medicines'][choosed_medicine]['duration'], 'condition': data['medicines'][choosed_medicine]['condition']}
                        medicines.append(medicine)
                        print("\nMedicamento adicionado com sucesso!")
                elif option == "2":
                    # Cadastra um novo medicamento
                    register_medicine()
                elif option == "3":
                    # Visualiza os medicamentos adicionados
                    if len(medicines) == 0:
                        print("\nNão há medicamentos adicionados.")
                    else:
                        for medicine in medicines:
                            print(Medicine(medicine['name'], medicine['qnt'], medicine['un'], medicine['interval'], medicine['duration'], medicine['condition']))        
                elif option == "4":
                    # Remove um medicamento da receita
                    if len(medicines) == 0:
                        print("\nNão há medicamentos adicionados.")
                    else:
                        for i, medicine in enumerate(medicines):
                            print(f"{i+1}. {Medicine(medicine['name'], medicine['qnt'], medicine['un'], medicine['interval'], medicine['duration'], medicine['condition'])}")
                        option = input("\nEscolha um medicamento: ")
                        if option.isnumeric() and int(option) > 0 and int(option) <= len(medicines):
                            medicines.pop(int(option) - 1)
                        else:
                            print("\nOpção inválida. Tente novamente.")
                elif option == "5":
                    # Finaliza a edição da receita
                    break
                else:
                    print("\nOpção inválida.")
        elif confirmation == "n":
            medicines = None
        else:
            print("\nOpção inválida. Tente novamente.")
            return None
        
        # Atualiza os dados da receita
        prescription = Prescription(data['prescriptions'][choosed_prescription]['professional'], data['prescriptions'][choosed_prescription]['patient'], data['prescriptions'][choosed_prescription]['medicines'], data['prescriptions'][choosed_prescription]['date'])
        prescription = prescription.update(professional, patient, medicines, date)
        
        data['prescriptions'][choosed_prescription] = prescription.__dict__()

        print("\nReceita atualizada com sucesso.")
        print(prescription)
        return data['medicines']
    else:
        print("\nReceita não atualizada.")
        try:
            return data['medicines']
        except:
            pass

def delete_prescription(l=None) -> list[Prescription]:
    # Código para deletar uma receita cadastrada no sistema
    option = choose_prescription(l)

    if option is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['prescriptions'] = l
        
        # Imprime a receita a ser deletada
        prescription = Prescription(data['prescriptions'][option]['professional'], data['prescriptions'][option]['patient'], data['prescriptions'][option]['medicines'], data['prescriptions'][option]['date'])
        print(f"Você deseja deletar a receita abaixo?\n{prescription}")
        confirm = input("Digite 'sim' para confirmar: ")
        if confirm != "sim":
            print("\nOperação cancelada.")
            return data['prescriptions']

        # Exclui a receita
        prescription.delete()
        if l is not None:
            data['prescriptions'].pop(option)
        print("\nReceita deletada com sucesso.")
        return data['prescriptions']

# ------ Funçõoes para manipular os dados de sintomas ------
def manage_symptoms():
    # Código para gerenciar os sintomas
    print("\nMenu de opções para sintomas:")
    print("1. Cadastrar novo sintoma")
    print("2. Listar sintomas")
    print("3. Atualizar sintoma")
    print("4. Excluir sintoma")
    print("5. Voltar ao menu principal")

    option = input("\nEscolha uma opção: ")

    if option == "1":
        # Chama a função para cadastrar um novo sintoma
        register_symptom()
    elif option == "2":
        # Chama a função para listar os sintomas
        list_symptoms()
    elif option == "3":
        # Chama a função para atualizar um sintoma
        update_symptom()
    elif option == "4":
        # Chama a função para excluir um sintoma
        delete_symptom()
    elif option == "5":
        # Volta ao menu principal
        return
    else:
        print("\nOpção inválida. Tente novamente.")
        manage_symptoms()    

def register_symptom(l=None) -> Symptom:
    # Código para cadastrar um novo sintoma
    name = input("Digite o nome do sintoma: ")
    date = input("Digite a data em que o sintoma começou: ")
    
    symptom = Symptom(name, date).create()
    
    print("\nSintoma cadastrado com sucesso.")
    print(symptom)
    return symptom

def list_symptoms(l=None, string=None) -> int:
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['symptoms'] = l

    # Verifica se há sintomas cadastrados
    if len(data['symptoms']) == 0:
        print("\nNão há sintomas cadastrados.")
        return None

    # Imprime os sintomas cadastrados
    if string is None:
        print("\nSintomas cadastrados:")
    else:
        print(string)
    for i, symptom in enumerate(data['symptoms']):
        print(f"{i+1}. {Symptom(symptom['name'], symptom['date'])}")

def choose_symptom(l=None) -> int:
    # Código para escolher um sintoma cadastrado no sistema
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['symptoms'] = l

    # Verifica se há sintomas cadastrados
    if len(data['symptoms']) == 0:
        print("\nNão há sintomas cadastrados.")
        return None

    # Imprime os sintomas cadastrados
    print("\nSintomas cadastrados:")
    list_symptoms(l)

    # Lê o índice do sintoma escolhido
    option = input("\nEscolha um sintoma: ")

    # Verifica se o índice é válido
    if option.isnumeric() and 1 <= int(option) <= len(data['symptoms']):
        return int(option) - 1
    else:
        print("\nOpção inválida. Tente novamente.")
        return choose_symptom(l)

def update_symptom(l=None) -> list[Symptom]:
    # Código para atualizar um sintoma cadastrado no sistema
    option = choose_symptom(l)

    if option is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['symptoms'] = l

        # Lê os novos dados do sintoma
        name = input("Insira o novo nome do sintoma: (deixe em branco para manter o nome atual: {}) ".format(data['symptoms'][option]['name']))
        if name == "":
            name = None
        date = input("Insira a nova data do sintoma: (deixe em branco para manter a data atual: {}) ".format(data['symptoms'][option]['date']))
        if date == "":
            date = None
        
        # Cria um novo objeto Symptom e chama o método update
        symptom = Symptom(data['symptoms'][option]['name'], data['symptoms'][option]['date'])
        symptom = symptom.update(name, date)
        
        data['symptoms'][option] = symptom.__dict__()

        print("\nSintoma atualizado com sucesso.")
        print(symptom)
        return data['symptoms']
        
def delete_symptom():
    # Código para excluir um sintoma cadastrado no sistema
    choosed_symptom = choose_symptom()

    if choosed_symptom is not None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Cria um novo objeto Symptom e chama o método delete
        symptom = Symptom(data['symptoms'][choosed_symptom]['name'], data['symptoms'][choosed_symptom]['date'])
        symptom.delete()

        # Remove o sintoma do arquivo JSON
        data['symptoms'].pop(choosed_symptom)

        print("\nSintoma excluído com sucesso.")
        print(symptom)

# ------ Funçõoes para manipular os dados de doenças ------
def manage_diseases():
    # Código para gerenciar as doenças
    print("\nMenu de opções para doenças:")
    print("1. Cadastrar doença")
    print("2. Listar doenças")
    print("3. Atualizar doença")
    print("4. Excluir doença")
    print("5. Voltar ao menu principal")

    option = input("\nEscolha uma opção: ")

    if option == "1":
        # Chama a função para cadastrar uma doença
        register_disease()
    elif option == "2":
        # Chama a função para listar as doenças
        list_diseases()
    elif option == "3":
        # Chama a função para atualizar uma doença
        update_disease()
    elif option == "4":
        # Chama a função para excluir uma doença
        delete_disease()
    elif option == "5":
        # Volta ao menu principal
        return
    else:
        print("\nOpção inválida. Tente novamente.")
        manage_diseases()

def register_disease(l=None) -> Disease:
    # Código para cadastrar uma doença
    name = input("Insira o nome da doença: ")

    symptoms = []
    # Lê os sintomas da doença
    while True:
        print("\n1. Adicionar sintoma cadastrado")
        print("2. Cadastrar novo sintoma")
        print("3. Visualizar sintomas adicionados")
        print("4. Editar sintomas adicionados")
        print("5. Remover sintomas adicionados")
        print("6. Terminar adição de sintomas")

        option = input("\nEscolha uma opção: ")

        if option == "1":
            # Chama a função para escolher um sintoma cadastrado
            choosed_symptom = choose_symptom()
            if choosed_symptom is not None:
                # Código para ler os dados do arquivo JSON
                with open('data.json', 'r') as f:
                    data = json.load(f)
                
                symptom = Symptom(data['symptoms'][choosed_symptom]['name'], data['symptoms'][choosed_symptom]['date'])
                symptoms.append(symptom)
                print("\nSintoma {} adicionado com sucesso.".format(symptom.name))
        elif option == "2":
            # Cadastra um novo sintoma
            symptom = register_symptom()
            symptoms.append(symptom.__dict__())
            print("\nSintoma {} adicionado com sucesso.".format(symptom.name))
        elif option == "3":
            # Imprime os sintomas adicionados
            list_symptoms(symptoms, "\nSintomas adicionados:")

def list_diseases():
    pass

def choose_disease():
    pass

def update_disease():
    pass

def delete_disease():
    pass

# ------ Funçõoes para manipular os dados de exames ------
def manage_exams():
    pass

def register_exam():
    pass

def list_exams():
    pass

def choose_exam():
    pass

def update_exam():
    pass

def delete_exam():
    pass

# ------ Funçõoes para manipular os dados de consultas ------
def manage_consultations():
    pass

def register_consultation():
    pass

def choose_consultation():
    pass

def update_consultation():
    pass

def delete_consultation():
    pass

# ------ Funçõoes para manipular os dados de pacientes ------
def manage_patients():
    pass

def register_patient():
    pass

def choose_patient():
    pass

def update_patient():
    pass

def delete_patient():
    pass

if __name__ == "__main__":
    main()