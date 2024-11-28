import requests
import csv
from textblob import TextBlob
from deep_translator import GoogleTranslator

def get_users(base_url):
    resposta = requests.get(base_url)
    users = resposta.json()
    return users

def get_posts(base_url_posts):
    resposta = requests.get(base_url_posts)
    posts = resposta.json()
    return posts

def translate_posts(titulo):
    post_traduzido = GoogleTranslator(source='auto', target='en').translate(text=titulo)
    return post_traduzido

def get_polarity(titulo):
    sentimento = TextBlob(titulo)
    return sentimento.sentiment.polarity



def save_result_csv(info_completas):
        
    fields = ["Nome","Titulo","Sentimento Post"]
    rows = []
    for usuario in info_completas:
        rows.append({
            "Nome": usuario['nome'],
            "Titulo": usuario['titulo_post'],
            "Sentimento Post": usuario['sentimento'],
        })
        filename = 'result_feelings.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
            csvwriter.writeheader()
            csvwriter.writerows(rows)

def sorting_key_to_csv(element):
    return element['sentimento']

def sorting_to_rank_by_feeling(element):
    return element[1]


def ranking_users_by_feelings_post(info_completas):
    dict_positivos = {} 
    for usuario in info_completas:
        if usuario['sentimento'] == 'positivo':
            nome = usuario['nome']
            dict_positivos[nome] = dict_positivos.get(nome, 0) + 1
    return dict_positivos

def main():
    base_url_users = "https://jsonplaceholder.typicode.com/users/"
    usuarios = get_users(base_url_users)
    info_completas = []
    for usuario in usuarios:
        id = usuario['id']
        nome = usuario['name']
        base_url_posts = f"https://jsonplaceholder.typicode.com/users/{id}/posts/"
        posts = get_posts(base_url_posts)
        for post in posts:
            titulo = post['title']
            post_traduzido = translate_posts(titulo)
            sentimentos_titulos = get_polarity(post_traduzido)
            if sentimentos_titulos > 0.0:
                sentimentos_titulos = "positivo"
            elif sentimentos_titulos == 0.0:
                sentimentos_titulos = "neutro"
            else:
                 sentimentos_titulos = "negativo"

            info_completas.append({
                'nome': nome,
                'titulo_post': post_traduzido,
                'sentimento': sentimentos_titulos,  
        })           
            info_completas.sort(key=sorting_key_to_csv, reverse=True) # salvando dos posts positivos para os negativos.
            save_result_csv(info_completas)
    ranking_positivos = ranking_users_by_feelings_post(info_completas)
    for nome, dict_positivos in sorted(ranking_positivos.items(), key=sorting_to_rank_by_feeling, reverse=True):
        print(f"Usuário: {nome}, Posts Positivos: {dict_positivos}")

if __name__ == '__main__':
    main()