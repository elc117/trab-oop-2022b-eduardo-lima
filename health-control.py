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
        data['professionals'].append(self.__dict__)
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

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
                data['professionals'][i] = self.__dict__
                print('Professional updated successfully!')
                
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
            json.dump(data, f, indent=4)

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
        data['medicines'].append(self.__dict__)

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
                data['medicines'][i] = self.__dict__
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
            json.dump(data, f, indent=4)

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
        data['prescriptions'].append(self.__dict__)
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
                data['prescriptions'][i] = self.__dict__
                
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
            json.dump(data, f, indent=4)

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
        data['symptoms'].append(self.__dict__)

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
                data['symptoms'][i] = self.__dict__
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
            json.dump(data, f, indent=4)

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
        data['diseases'].append(self.__dict__)

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
                data['diseases'][i] = self.__dict__
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
            json.dump(data, f, indent=4)

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
        data['exams'].append(self.__dict__)

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
                data['exams'][i] = self.__dict__
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
            json.dump(data, f, indent=4)

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
    def __init__(self, professional, patient, symptoms, diagnose, exams, date):
        self.professional = professional
        self.patient = patient
        self.symptoms = symptoms
        self.diagnose = diagnose
        self.exams = exams
        self.date = date
    
    def create(self):
        # Código para criar uma nova consulta no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para adicionar uma nova consulta aos dados
        data['consultations'].append(self.__dict__)

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
    
    def update(self, new_professional=None, new_symptoms=None, new_diagnose=None, new_exams=None, new_date=None):
        # Código para atualizar uma consulta existente no sistema
        with open('data.json', 'r') as f:
            data = json.load(f)
        
        # Código para procurar uma consulta com o nome do paciente especificado
        # e atualizar os dados da consulta
        for i, consultation in enumerate(data['consultations']):
            if consultation['professional'] == self.patient and consultation['data'] == self.data:
                self = Consultation(new_professional, new_symptoms, new_diagnose, new_exams, new_date)
                data['consultations'][i] = self.__dict__
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
            json.dump(data, f, indent=4)

    def __dict__(self):
        return {
            'professional': self.professional,
            'symptoms': self.symptoms,
            'diagnose': self.diagnose,
            'exams': self.exams,
            'date': self.date
        }

    def __str__(self):
        return f'{self.professional} - {self.symptoms} - {self.diagnose} - {self.exams} - {self.date}'

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
        data['patients'].append(self.__dict__)

        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
                data['patients'][i] = self.__dict__
        
        # Código para escrever os dados de volta para o arquivo JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        
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
            json.dump(data, f, indent=4)

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
            json.dump(data, f, indent=4)
    
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
        json.dump(data, f, indent=4)

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
                option_exclusion = input("\nDeseja remover o medicamento {} do cadastro também? (s/n): ".format(medicines[option]['name']))
                if option_exclusion == "s":
                    confirm = input("\nTem certeza que deseja remover o medicamento {} do cadastro? (sim/n): ".format(medicines[option]['name']))
                    if confirm == "sim":
                        # Remove o medicamento do cadastro
                        Medicine(medicines[option]['name'], medicines[option]['qnt'], medicines[option]['un'], medicines[option]['interval'], medicines[option]['duration'], medicines[option]['condition']).delete()
                        print("\nMedicamento removido do cadastro com sucesso!")
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
    return prescription

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
    
def choose_prescription(l=None, string="\nReceitas cadastradas:") -> int:
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
    list_prescriptions(l, string)

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
                        list_medicines(medicines, "Medicamentos adicionados:")
                elif option == "4":
                    # Remove um medicamento da receita
                    if len(medicines) == 0:
                        print("\nNão há medicamentos adicionados.")
                    else:
                        choosed_medicine = choose_medicine(medicines, "Medicamentos adicionados:")
                        if choosed_medicine is not None:
                            medicines.pop(choosed_medicine)
                            print("\nMedicamento removido com sucesso!")
                        else: 
                            print("\nOpção inválida. Tente novamente.")
                elif option == "5":
                    # Finaliza a edição da receita
                    break
                else:
                    print("\nOpção inválida.")
        else:
            medicines = None
        
        
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

def register_symptom() -> Symptom:
    # Código para cadastrar um novo sintoma
    name = input("Digite o nome do sintoma: ")
    date = input("Digite a data em que o sintoma começou: ")
    
    symptom = Symptom(name, date).create()
    
    print("\nSintoma cadastrado com sucesso.")
    print(symptom)
    return symptom

def list_symptoms(l=None, string=None):
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

def choose_symptom(l=None,string="\nSintomas cadastrados:") -> int:
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
    list_symptoms(l, string)

    # Lê o índice do sintoma escolhido
    choosed_symptom = input("\nEscolha um sintoma: ")

    # Verifica se o índice é válido
    if choosed_symptom.isnumeric() and 1 <= int(choosed_symptom) <= len(data['symptoms']):
        return int(choosed_symptom) - 1
    else:
        print("\nOpção inválida. Tente novamente.")
        return choose_symptom(l, string)

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
        
def delete_symptom(l=None):
    # Código para excluir um sintoma cadastrado no sistema
    choosed_symptom = choose_symptom()

    if choosed_symptom is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['symptoms'] = l

        # Cria um novo objeto Symptom e chama o método delete
        symptom = Symptom(data['symptoms'][choosed_symptom]['name'], data['symptoms'][choosed_symptom]['date'])
        symptom.delete()

        # Remove o sintoma da lista de sintomas
        data['symptoms'].pop(choosed_symptom)

        print("\nSintoma excluído com sucesso.")

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
        elif option == "4":
            # Edita os sintomas adicionados
            symptoms = update_symptom(symptoms)
        elif option == "5":
            # Remove um sintoma adicionado
            choosed_symptom = choose_symptom(symptoms, "\nSintomas adicionados:")
            if choosed_symptom is not None:
                option_exclusion = input("\nDeseja realmente excluir o sintoma {}? (s/n): ".format(symptoms[choosed_symptom]['name']))
                if option_exclusion == "s":
                    confirmation = input("Tem certeza que deseja excluir o sintoma {} do cadastro? (sim/n): ".format(symptoms[choosed_symptom]['name']))
                    if confirmation == "sim":
                        # Remove o sintoma do cadastro
                        Symptom(symptoms[choosed_symptom]['name'], symptoms[choosed_symptom]['date']).delete()
                        print("\nSintoma excluído do cadastro com sucesso!".format(symptoms[choosed_symptom]['name']))
                    symptoms.pop(choosed_symptom)
                    print("\nSintoma removido da doença com sucesso!")
        elif option == "6":
            # Finaliza a adição de sintomas
            break
        else:
            print("\nOpção inválida.")
    
    date = input("Insira a data de início da doença: ")

    # Cria um objeto da classe Disease
    disease = Disease(name, symptoms, date)
    disease.create()
    print("\nDoença cadastrada com sucesso!")
    print(disease)
            
def list_diseases(l=None, string="\nDoenças cadastradas:"):
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['diseases'] = l
    
    # Verifica se há doenças cadastradas
    if len(data['diseases']) == 0:
        print("\nNão há doenças cadastradas.")
        return None

    # Imprime as doenças cadastradas
    print(string)
    for i, disease in enumerate(data['diseases']):
        print(f"{i+1}. {Disease(disease['name'], disease['symptoms'], disease['date'])}")        

def choose_disease(l=None,string="\nDoenças cadastradas:") -> int:
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['diseases'] = l
    
    # Verifica se há doenças cadastradas
    if len(data['diseases']) == 0:
        print("\nNão há doenças cadastradas.")
        return None
    
    # Imprime as doenças cadastradas
    list_diseases(data, string)

    # Lê o indice da doença escolhida
    choosed_disease = input("\nEscolha uma doença: ")

    # Verifica se o indice é válido
    if choosed_disease.isnumeric() and int(choosed_disease) > 0 and int(choosed_disease) <= len(data['diseases']):
        return int(choosed_disease) - 1
    else:
        print("\nOpção inválida.")
        return choose_disease(data, string)

def update_disease(l=None) -> list[Disease]:
    # Código para atualizar uma doença
    choosed_disese = choose_disease(l)

    if choosed_disese is not None:
        # Código para ler os dados do arquivo JSON
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['diseases'] = l
        
        # Lê os novos dados da doença escolhida
        name = input("Insira o nome da doença (deixe em branco para manter o nome atual: {}): ".format(data['diseases'][choosed_disese]['name']))
        if name == "":
            name = None
        confirmation = input("Deseja alterar os sintomas da doença? (s/n): ")
        if confirmation == "s":
            symptoms = data['diseases'][choosed_disese]['symptoms']
            while True:
                print("\n1. Adicionar sintoma cadstrado")
                print("2. Cadastrar novo sintoma")
                print("3. Visualizar sintomas da doença")
                print("4. Remover sintoma da doença")
                print("5. Finalizar edição de sintomas")
            
                option = input("\nEscolha uma opção: ")

                if option == "1":
                    # Adiciona um sintoma cadastrado
                    choosed_symptom = choose_symptom()
                    if choosed_symptom is not None:
                        with open('data.json', 'r') as f:
                            data = json.load(f)
                        symptoms.append(data['symptoms'][choosed_symptom])
                        print("\nSintoma adicionado com sucesso!")
                elif option == "2":
                    # Cadastra um novo sintoma
                    symptoms.append(register_symptom())
                elif option == "3":
                    if len(symptoms) == 0:
                        print("\nNão há sintomas na doença.")
                    else:
                        # Visualiza os sintomas da doença
                        list_symptoms(symptoms, "\nSintomas da doença:")
                elif option == "4":
                    # Remove um sintoma da doença
                    if len(symptoms) == 0:
                        print("\nNão há sintomas na doença.")
                    else:
                        choosed_symptom = choose_symptom(symptoms, "\nSintomas da doença:")
                        if choosed_symptom is not None:
                            symptoms.pop(choosed_symptom)
                            print("\nSintoma removido com sucesso!")
                        else:
                            print("\nOpção inválida.")
                elif option == "5":
                    # Finaliza a edição dos sintomas
                    break
                else:
                    print("\nOpção inválida.")
            
            else:
                symptoms = None

            date = input("Insira a data da doença (deixe em branco para manter a data atual: {}): ".format(data['diseases'][choosed_disese]['date']))
            
            # Atualiza os dados da doença
            disease = Disease(data['diseases'][choosed_disese]['name'], data['diseases'][choosed_disese]['symptoms'], data['diseases'][choosed_disese]['date'])
            disease = disease.update(name, symptoms, date)

            data['diseases'][choosed_disese] = disease.__dict__()

            print("\nDoença atualizada com sucesso!")
            print(disease)
            return data['diseases']
        else:
            print("\nDoença não atualizada.")
            try:
                return data['diseases']
            except:
                pass

def delete_disease(l=None) -> list[Disease]:
    # Código para deletar uma doença cadastrada
    choosed_disease = choose_disease(l)

    if choosed_disease is not None:
        # Código para ler os dados do arquivo JSON
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['diseases'] = l

        # Imprime a doença a ser deletada
        disease = Disease(data['diseases'][choosed_disease]['name'], data['diseases'][choosed_disease]['symptoms'], data['diseases'][choosed_disease]['date'])
        print(f"Você deseja deletar a doença abaixo?\n{disease}")
        confirmation = input("Digite 'sim' para confirmar: ")
        if confirmation != "sim":
            print("\nDoença não deletada.")
            return data['diseases']

        # Exclui a doença escolhida
        disease.delete()
        if l is not None:
            data['diseases'].pop(choosed_disease)
        print("\nDoença deletada com sucesso!")
        return data['diseases']

# ------ Funçõoes para manipular os dados de exames ------
def manage_exams():
    # Código para gerenciar os exames
    print("\nMenu de opções para exames:")
    print("1. Cadastrar novo exame")
    print("2. Listar exames")
    print("3. Atualizar exame")
    print("4. Excluir exame")
    print("5. Voltar ao menu principal")

    option = input("\nEscolha uma opção: ")

    if option == "1":
        # Chama a função para cadastrar um novo exame
        register_exam()
    elif option == "2":
        # Chama a função para listar os exames
        list_exams()
    elif option == "3":
        # Chama a função para atualizar um exame
        update_exam()
    elif option == "4":
        # Chama a função para excluir um exame
        delete_exam()
    elif option == "5":
        # Volta ao menu principal
        return
    else:
        print("\nOpção inválida.")
        manage_exams()

def register_exam() -> Exam:
    # Código para cadastrar um novo exame
    name = input("Insira o nome do exame: ")
    results = input("Insira os resultados do exame: ")
    professional = input("Insira o nome do profissional que solicitou o exame: ")
    date = input("Insira a data do exame (DD/MM/AAAA): ")

    # Cria um objeto do tipo Exame
    exam = Exam(name, results, professional, date).create()

    print("\nExame cadastrado com sucesso!")
    print(exam)
    return exam

def list_exams(l=None, string="Exames cadastrados:"):
    # Código para listar os exames cadastrados
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['exams'] = l

    # Verifica se há exames cadastrados
    if len(data['exams']) == 0:
        print("\nNão há exames cadastrados.")
        return None
    
    # Imprime os exames cadastrados
    print(string)
    for i, exam in enumerate(data['exams']):
        print(f"{i+1}. {Exam(exam['name'], exam['results'], exam['professional'], exam['date'])}")

def choose_exam(l=None, string="Exames cadastrados:") -> int:
    # Código para escolher um exame
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['exams'] = l

    # Verifica se há exames cadastrados
    if len(data['exams']) == 0:
        return None

    # Imprime os exames cadastrados
    list_exams(l, string)

    # Lê o índice do exame escolhido
    choosed_exam = input("Escolha um exame: ")

    # Verifica se o usuário escolheu um exame válido
    if choosed_exam.isnumeric() and int(choosed_exam) > 0 and int(choosed_exam) <= len(data['exams']):
        return int(choosed_exam) - 1
    else:
        print("\nExame inválido. Tente novamente.")
        return choose_exam(l, string)

def update_exam(l=None) -> list[Symptom]:
    # Código para atualizar um exame cadastrado
    choosed_exam = choose_exam(l)

    if choosed_exam is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['exams'] = l

        # Lê os dados do exame
        name = input("Insira o nome do exame (deixe em branco para manter o atual: {}): ".format(data['exams'][choosed_exam]['name']))
        if name == "":
            name = None
        results = input("Insira os resultados do exame (deixe em branco para manter o atual: {}): ".format(data['exams'][choosed_exam]['results']))
        if results == "":
            results = None
        professional = input("Insira o nome do profissional que solicitou o exame (deixe em branco para manter o atual: {}): ".format(data['exams'][choosed_exam]['professional']))
        if professional == "":
            professional = None
        date = input("Insira a data do exame (DD/MM/AAAA) (deixe em branco para manter o atual: {}): ".format(data['exams'][choosed_exam]['date']))
        if date == "":
            date = None
        
        # Cria um objeto do tipo Exame
        exam = Exam(name, results, professional, date).update(data['exams'][choosed_exam])
        exam = exam.update(name, results, professional, date)

        data['exams'][choosed_exam] = exam.__dict__()

        print("\nExame atualizado com sucesso!")
        print(exam)
        return data['exams']

def delete_exam(l=None):
    # Código para excluir um exame cadastrado
    choosed_exam = choose_exam(l)

    if choosed_exam is not None:
        # Código para ler os dados do arquivo JSON
        if l is None:
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['exams'] = l

        # Cria um objeto do tipo Exame
        exam = Exam(data['exams'][choosed_exam]['name'], data['exams'][choosed_exam]['results'], data['exams'][choosed_exam]['professional'], data['exams'][choosed_exam]['date'])
        exam.delete()

        # Remove o exame da lista de exames
        data['exams'].pop(choosed_exam)

        print("\nExame excluído com sucesso!")

# ------ Funçõoes para manipular os dados de consultas ------
def manage_consultations():
    # Código para gerenciar as consultas
    print("\nMenu de opções para consultas:")
    print("1. Cadastrar nova consulta")
    print("2. Listar consultas")
    print("3. Atualizar consulta")
    print("4. Excluir consulta")
    print("5. Voltar ao menu principal")

    option = input("Escolha uma opção: ")

    if option == "1":
        # Chama a função para cadastrar uma nova consulta
        register_consultation()
    elif option == "2":
        # Chama a função para listar as consultas
        list_consultations()
    elif option == "3":
        # Chama a função para atualizar uma consulta
        update_consultation()
    elif option == "4":
        # Chama a função para excluir uma consulta
        delete_consultation()
    elif option == "5":
        # Volta ao menu principal
        return
    else:
        print("\nOpção inválida. Tente novamente.")
        manage_consultations()

def register_consultation() -> Consultation:
    # Código para cadastrar uma nova consulta
    professional = input("Insira o nome do profissional: ")
    patient = input("Insira o nome do paciente: ")

    # Adicionar sintomas
    symptoms = []
    while True:
        print("\n1. Adicionar sintoma cadastrado:")
        print("2. Cadastrar novo sintoma:")
        print("3. Visualizar sintomas adicionados:")
        print("4. Editar sintomas adicionados:")
        print("5. Remover sintomas adicionados:")
        print("6. Finalizar")

        option = input("Escolha uma opção: ")

        if option == "1":
            # Adiciona um sintoma cadastrado
            choosed_symptom = choose_symptom()
            if choosed_symptom is not None:
                # Código para ler os dados do arquivo JSON
                with open('data.json', 'r') as f:
                    data = json.load(f)

                symptom = Symptom(data['symptoms'][choosed_symptom]['name'], data['symptoms'][choosed_symptom]['description'])
                symptoms.append(symptom.__dict__)
                print("\nSintoma adicionado com sucesso!")
        elif option == "2":
            # Cadastra um novo sintoma
            symptom = register_symptom()
            symptoms.append(symptom.__dict__)
            print("\nSintoma {} adicionado com sucesso!".format(symptom.name))
        elif option == "3":
            # Impressão dos sintomas adicionados
            list_symptoms(symptoms,string="\nSintomas adicionados:")
        elif option == "4":
            # Edição dos sintomas adicionados
            symptoms = update_symptom(symptoms)
        elif option == "5":
            # Remoção dos sintomas adicionados
            choosed_symptom = choose_symptom(symptoms, string="\nSintomas adicionados:")
            if choosed_symptom is not None:
                option_exclusion = input("Deseja realmente excluir o sintoma {}? (s/n): ".format(symptoms[choosed_symptom]['name']))
                if option_exclusion == "s":
                    confirm = input("Tem certeza? (sim/n): ")
                    if confirm == "sim":
                        # Remove o sintoma do cadastro
                        Symptom(symptoms[choosed_symptom]['name'], symptoms[choosed_symptom]['description']).delete()
                        print("\nSintoma excluído do cadastro com sucesso!")
                    symptoms.pop(choosed_symptom)
                    print("\nSintoma removido da consulta com sucesso!")
        elif option == "6":
            # Finaliza a adição de sintomas
            break
        else:
            print("\nOpção inválida. Tente novamente.")
        
    diagnose = input("Insira o diagnóstico: ")

    exams = []
    while True:
        print("\n1. Adicionar exame cadastrado:")
        print("2. Cadastrar novo exame:")
        print("3. Visualizar exames adicionados:")
        print("4. Editar exames adicionados:")
        print("5. Remover exames adicionados:")
        print("6. Finalizar")

        option = input("Escolha uma opção: ")

        if option == "1":
            # Adiciona um exame cadastrado
            choosed_exam = choose_exam()
            if choosed_exam is not None:
                # Código para ler os dados do arquivo JSON
                with open('data.json', 'r') as f:
                    data = json.load(f)

                exam = Exam(data['exams'][choosed_exam]['name'], data['exams'][choosed_exam]['description'])
                exams.append(exam.__dict__)
                print("\nExame adicionado com sucesso!")
        elif option == "2":
            # Cadastra um novo exame
            exam = register_exam()
            exams.append(exam.__dict__)
            print("\nExame {} adicionado com sucesso!".format(exam.name))
        elif option == "3":
            # Impressão dos exames adicionados
            list_exams(exams,string="\nExames adicionados:")
        elif option == "4":
            # Edição dos exames adicionados
            exams = update_exam(exams)
        elif option == "5":
            # Remoção dos exames adicionados
            choosed_exam = choose_exam(exams, string="\nExames adicionados:")
            if choosed_exam is not None:
                option_exclusion = input("Deseja realmente excluir o exame {}? (s/n): ".format(exams[choosed_exam]['name']))
                if option_exclusion == "s":
                    confirm = input("Tem certeza? (sim/n): ")
                    if confirm == "sim":
                        # Remove o exame do cadastro
                        Exam(exams[choosed_exam]['name'], exams[choosed_exam]['description']).delete()
                        print("\nExame excluído do cadastro com sucesso!")
                    exams.pop(choosed_exam)
                    print("\nExame removido da consulta com sucesso!")
        elif option == "6":
            # Finaliza a adição de exames
            break
        else:
            print("\nOpção inválida. Tente novamente.")
        
    date = input("Insira a data da consulta (DD/MM/AAAA): ")

    consultation = Consultation(professional, patient, symptoms, diagnose, exams, date)
    consultation.create()

    print("\nConsulta cadastrada com sucesso!")
    print(consultation)

    return consultation

def list_consultations(l=None, string="\nConsultas cadastradas:"):
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['consultations'] = l
    
    # Verifica se há consultas cadastradas
    if len(data['consultations']) == 0:
        print("\nNão há consultas cadastradas.")
        return
    
    # Impressão das consultas cadastradas
    print(string)
    for i in range(len(data['consultations'])):
        print("{} - {}".format(i, data['consultations'][i]['professional']['name'], data['consultations'][i]['patient']['name'], data['consultations'][i]['date']))      

def choose_consultation(l=None, string="\nConsultas cadastradas:"):
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['consultations'] = l
    
    # Verifica se há consultas cadastradas
    if len(data['consultations']) == 0:
        print("\nNão há consultas cadastradas.")
        return None
    
    # Impressão das consultas cadastradas
    list_consultations(data, string)

    # Escolha da consulta
    choosed_consultation = input("Escolha uma consulta: ")
    
    # Verifica se a opção escolhida é válida
    if choosed_consultation.isnumeric() and choosed_consultation >= 0 and choosed_consultation < len(data['consultations']):
            return int(choosed_consultation) - 1
    else:
        print("\nOpção inválida. Tente novamente.")
        return choose_consultation(data, string)

def update_consultation(l=None):
    # Código para atualizar os dados de uma consulta

    choosed_consultation = choose_consultation(l)
    
    if choosed_consultation is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['consultations'] = l
        
        # Lê os novos dados da consulta
        professional = input("Insira o nome do profissional (deixe em branco para manter o valor atual: {}): ".format(data['prescriptions'][choosed_consultation]['professional']))
        if professional == "":
            professional = None
        patient = input("Insira o nome do paciente (deixe em branco para manter o valor atual: {}): ".format(data['prescriptions'][choosed_consultation]['patient']))
        if patient == "":
            patient = None
        
        confirmation = input("Deseja alterar os sintomas? (s/n): ")
        if confirmation == "s":
            symptoms = data['prescriptions'][choosed_consultation]['symptoms']
            
            while True:
                print("1. Adicionar sintoma cadastrado")
                print("2. Cadastrar novo sintoma")
                print("3. Visualizar sintomas adicionados")
                print("4. Remover sintoma adicionado")
                print("5. Finalizar edição de sintomas")

                option = input("Escolha uma opção: ")

                if option == "1":
                    # Adiciona um sintoma cadastrado
                    choosed_symptom = choose_symptom()
                    if choosed_symptom is not None:
                        with open('data.json', 'r') as f:
                            data = json.load(f)
                        symptoms.append(data['symptoms'][choosed_symptom])
                        print("\nSintoma adicionado com sucesso!")
                elif option == "2":
                    # Cadastra um novo sintoma
                    register_symptom()
                elif option == "3":
                    # Visualiza os sintomas adicionados
                    list_symptoms(symptoms)
                elif option == "4":
                    # Remove um sintoma adicionado
                    if len(symptoms) == 0:
                        print("\nNão há sintomas adicionados.")
                    else:
                        choosed_symptom = choose_symptom(symptoms, "\nSintomas adicionados:")
                        if choosed_symptom is not None:
                            symptoms.pop(choosed_symptom)
                            print("\nSintoma removido com sucesso!")
                        else:
                            print("\nOpção inválida.")
                elif option == "5":
                    # Finaliza a edição de sintomas
                    break
                else:
                    print("\nOpção inválida.")

        date = input("Insira a data da receita (dd/mm/aaaa) (deixe em branco para manter o valor atual: {}): ".format(data['prescriptions'][choosed_consultation]['date']))
        if date == "":
            date = None
        
        # Atualiza os dados da consulta
        consultation = Consultation(data['consultations'][choosed_consultation]['professional'], data['consultations'][choosed_consultation]['patient'], data['consultations'][choosed_consultation]['symptoms'], data['consultations'][choosed_consultation]['date'])
        consultation.update(professional, patient, symptoms, date)

        data['consultations'][choosed_consultation] = consultation.__dict__

        print("\nConsulta atualizada com sucesso!")
        print(consultation)
        return data['consultations']
    else:
        print("\nReceita não atualizada.")
        try:
            return data['consultations']
        except:
            pass

def delete_consultation(l=None):
    # Código para deletar uma consulta

    choosed_consultation = choose_consultation()
    
    if choosed_consultation is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['consultations'] = l
        
        # Imprime a consulta escolhida
        consultation = Consultation(data['consultations'][choosed_consultation]['professional'], data['consultations'][choosed_consultation]['patient'], data['consultations'][choosed_consultation]['symptoms'], data['consultations'][choosed_consultation]['date'])
        print(f"Você deseja deletar a consulta abaixo?\n{consultation}")
        confirm = input("Digite 'sim' para confirmar: ")
        if confirm != "sim":
            print("Operaçao cancelada.")
            return data['consultations']
        
        # Exclui a consulta
        consultation.delete()
        if l is not None:
            data['consultations'].pop(choosed_consultation)
        print("Consulta excluída com sucesso!")
        return data['consultations']

# ------ Funçõoes para manipular os dados de pacientes ------
def manage_patients():
    # Código para gerenciar os pacientes
    print("\nMenu de gerenciamento de pacientes")
    print("1. Cadastrar paciente")
    print("2. Listar pacientes")
    print("3. Atualizar paciente")
    print("4. Excluir paciente")
    print("5. Voltar ao menu principal")

    option = input("Escolha uma opção: ")

    if option == "1":
        # Cadastra um novo paciente
        register_patient()
    elif option == "2":
        # Lista os pacientes cadastrados
        list_patients()
    elif option == "3":
        # Atualiza um paciente
        update_patient()
    elif option == "4":
        # Exclui um paciente
        delete_patient()
    elif option == "5":
        # Volta ao menu principal
        return
    else:
        print("\nOpção inválida. Tentar novamente.")
        manage_patients()

def register_patient():
    # Código para cadastrar um novo paciente
    name = input("Insira o nome do paciente: ")
    birth_date = input("Insira a data de nascimento do paciente (dd/mm/aaaa): ")
    gender = input("Insira o gênero do paciente (M/F): ")

    # Cria um novo paciente
    patient = Patient(name, birth_date, gender)
    patient.create()

    print("\nPaciente cadastrado com sucesso!")
    print(patient)

    return patient

def list_patients(l=None, string="\nPacientes cadastrados"):
    # Código para listar os pacientes cadastrados
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['patients'] = l
    
    print(string)
    for i in range(len(data['patients'])):
        print("{}. {}".format(i+1, data['patients'][i]['name']))

def choose_patient(l=None, string="\nPacientes cadastrados"):
    if l is None:
        # Código para ler os dados do arquivo JSON
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}
        data['patients'] = l
    
    # Verifica se há pacientes cadastrados
    if len(data['patients']) == 0:
        print("\nNão há pacientes cadastrados.")
        return None
    
    # Lista os pacientes cadastrados
    list_patients(l, string)

    # Escolhe um paciente
    choosed_patient = input("Escolha um paciente: ")

    # Verifica se o paciente escolhido é válido
    if choosed_patient.isnumeric() and int(choosed_patient) > 0 and int(choosed_patient) <= len(data['patients']):
        return int(choosed_patient) - 1
    else:
        print("\nOpção inválida. Tentar novamente.")
        return choose_patient(l, string)

def update_patient(l=None):
    # Código para atualizar um paciente
    choosed_patient = choose_patient(l)
    
    if choosed_patient is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['patients'] = l
        
        # Lê os novos dados do paciente
        name = input("Insira o novo nome do paciente (deixe em branco para manter o nome atual: {}): ".format(data['patients'][choosed_patient]['name']))
        if name == "":
            name = None
        birth_date = input("Insira a nova data de nascimento do paciente (deixe em branco para manter a data atual: {}): ".format(data['patients'][choosed_patient]['birth_date']))
        if birth_date == "":
            birth_date = None
        gender = input("Insira o novo gênero do paciente (deixe em branco para manter o gênero atual: {}): ".format(data['patients'][choosed_patient]['gender']))
        if gender == "":
            gender = None
        
        # Atualiza o paciente
        patient = Patient(data['patients'][choosed_patient]['name'], data['patients'][choosed_patient]['birth_date'], data['patients'][choosed_patient]['gender'])
        patient.update(name, birth_date, gender)

        data['patients'][choosed_patient] = patient.__dict__

        print("\nPaciente atualizado com sucesso!")
        print(patient)
        return data['patients']
    else:
        print("\nReceita não atualizada.")
        try:
            return data['patients']
        except:
            pass

def delete_patient(l=None):
    # Código para excluir um paciente
    choosed_patient = choose_patient(l)

    if choosed_patient is not None:
        if l is None:
            # Código para ler os dados do arquivo JSON
            with open('data.json', 'r') as f:
                data = json.load(f)
        else:
            data = {}
            data['patients'] = l
        
        # Imprime o paciente que será excluído
        patient = Patient(data['patients'][choosed_patient]['name'], data['patients'][choosed_patient]['birth_date'], data['patients'][choosed_patient]['gender'])
        print(f"\nVocê deseja deletar o paciente abaixo?\n{patient}")
        confirm = input("Digite 'sim' para confirmar: ")
        if confirm != "sim":
            print("\nExclusão cancelada.")
            return data['patients']
        
        # Exclui o paciente
        patient.delete()
        if l is not None:
            data['patients'].pop(choosed_patient)
        print("\nPaciente excluído com sucesso!")
        return data['patients']

if __name__ == "__main__":
    main()