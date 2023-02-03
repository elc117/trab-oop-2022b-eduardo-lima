import json
from datetime import datetime

#import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages

# Lê o arquivo data.json e armazena em um objeto python
with open('data.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

title = "# Controle de Saúde\n"
print(title)

data['professionals'].sort(key=lambda professional: professional['name'])
professionals = "### Profissionais\n"
for professional in data['professionals']:
    professionals += "**" + professional['name'] + "** - " + professional['specialty'] + "\n" + professional['city'] + "\n" + professional['phone'] + "\n\n"
print(professionals)

patients = "\n---\n### Pacientes\n"
img_count = 0

for patient in data['patients']:
    patients += "**" + patient['name'] + "** - " + patient['birth_date'] + " - " + patient['gender'] + "\n"
    
    # Peso
    if len(patient['weight']) > 1:
        patient['weight'].sort(key=lambda d:datetime.strptime(d['date'], '%d/%m/%Y'))
        values = [weight['value'] for weight in patient['weight']]
        dates = [weight['date'] for weight in patient['weight']]
        plt.plot(dates, values, '-o')
        plt.title("Histórico de peso")
        plt.xlabel("Data")
        plt.ylabel("Peso(Kg)")
        plt.savefig("imgs/"+str(img_count)+".jpg")
        patients += "![ ]("+"imgs/"+str(img_count)+".jpg"+")\n"
        img_count += 1
    elif len(patient['weight']) == 1:
        patients += "Peso: " + str(patient['weight'][0]['value']) + " - " + str(patient['weight'][0]['date']+'\n')

    # Altura
    if len(patient['height']) > 1:
        patient['height'].sort(key=lambda d:datetime.strptime(d['date'], '%d/%m/%Y'))
        values = [height['value'] for height in patient['height']]
        dates = [height['date'] for height in patient['height']]
        plt.plot(dates, values, '-o')
        plt.title("Histórico de altura")
        plt.xlabel("Data")
        plt.ylabel("Altura(m)")
        plt.savefig("imgs/"+str(img_count)+".jpg")
        patients += "![ ]("+"imgs/"+str(img_count)+".jpg"+")\n"
        img_count += 1
    elif len(patient['height']) == 1:
        patients += "Altura: " + str(patient['height'][0]['value']) + "m - " + str(patient['height'][0]['date']+'\n')

    patients += "\n#### Profissionais:\n"
    for professional in patient[
        'professionals']:
        patients += professional + "\n"

    patients += "\n#### Medicamentos:\n"
    for medicine in patient['medicines']:
        patients += medicine['name']# + "\n"
    
    patients += "\n#### Receitas:\n"
    for prescription in patient['prescriptions']:
        patients += prescription['professional'] + " - " + prescription['date'] + "\n"
        for medicine in prescription['medicines']:
            patients += f"* {medicine['name']} - {medicine['qnt']} {medicine['un']}\n\t{medicine['interval']}h - {medicine['duration']}\n\t{medicine['condition']}\n"


print(patients)

with open('report.md', 'w', encoding='UTF-8') as file:
    file.write(title)
    file.write(professionals)
    file.write(patients)
