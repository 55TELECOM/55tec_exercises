import requests
import csv

def get_users():    
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url, verify=False)
    users = response.json()
    return users

def get_info_tasks(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}/todos" 
    response = requests.get(url, verify=False)
    info_tasks = response.json()
    return info_tasks

def concluded_tasks(info_tasks):
    count = 0
    for task in info_tasks:
        if task['completed'] == True:
            count += 1
    return count

def not_concluded_tasks(info_tasks):
    count = 0
    for task in info_tasks:
        if task['completed'] == False:
            count += 1
    return count

def productivy_percentage(info_tasks):
    concluidas = concluded_tasks(info_tasks)
    nao_concluidas = not_concluded_tasks(info_tasks)
    total = concluidas + nao_concluidas
    percentual = concluidas / total * 100
    return round(percentual)

def get_valor_percentual_produtividade(elemento):
    return elemento['percentual_produtividade']

def get_maior_produtividade(dicionario):
    return max(dicionario, key=get_valor_percentual_produtividade)

def save_result_csv(info_completa):
    
    fields = ["Nome","Email","Tarefas Concluídas","Tarefas Não Concluídas","Porcentagem Concluída", "Produtividade"]
    rows = []
    
    for usuario in info_completa:
        maior_produtividade = get_maior_produtividade(info_completa)
        if maior_produtividade['percentual_produtividade'] == usuario['percentual_produtividade']:
            usuario['produtividade'] = 'Sim'
        else:
            usuario['produtividade'] = 'Nao'
        rows.append({
            "Nome": usuario['nome'],
            "Email": usuario['email'],
            "Tarefas Concluídas": usuario['tarefas_completadas'],
            "Tarefas Não Concluídas": usuario['tarefas_nao_completadas'],
            "Porcentagem Concluída": usuario['percentual_produtividade'],
            "Produtividade": usuario['produtividade']
        })
        
    with open('result.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
        csvwriter.writeheader()
        csvwriter.writerows(rows)
   
    filename = 'result.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
        csvwriter.writeheader()
        csvwriter.writerows(rows)

def main():
    info_users = get_users() 
    info_completa = []

    for users in info_users:
        id = users['id']
        nome = users['name']
        email = users['email']
        info_tarefas = get_info_tasks(id)
        tarefas_completadas = concluded_tasks(info_tarefas)
        tarefas_nao_completadas = not_concluded_tasks(info_tarefas)
        percentual_produtividade = productivy_percentage(info_tarefas)
        

        info_completa.append({
            'nome': nome,
            'email': email,
            'tarefas_completadas': tarefas_completadas,
            'tarefas_nao_completadas': tarefas_nao_completadas,
            'percentual_produtividade': percentual_produtividade,
            })
        
    salvar_csv = save_result_csv(info_completa)
       
if __name__ == '__main__':
    main()
