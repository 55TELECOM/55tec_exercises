import requests
from deep_translator import GoogleTranslator
from textblob import TextBlob
import csv
#pega a URL e transforma em json
def get_users(base_url):
    retorno = requests.get(base_url)
    users = retorno.json()
    return users
#realiza a tradução
def traduzir_posts(frases):
    traduzir = GoogleTranslator(source='auto', target='en').translate(text=frases)
    return  traduzir
#faz a análise da frase
def sentimento_text(frases_sentimento):
    sentimento = TextBlob(frases_sentimento)
    return sentimento.sentiment.polarity

def usuarios_positivos(info_completas):
    contagem_positivos = {}
    for positivos in info_completas:
        if positivos['sentimento'] == 'positivo':
            nome = positivos['nome']
            contagem_positivos[nome] = contagem_positivos.get(nome, 0) + 1
    return contagem_positivos

def order_positivos(element):
    return element[1]

def resultados_csv(dict_completa):
    campos = ["Usuário", "Título", "Sentimento"]
    resultados = []
    for usuarios in dict_completa:
        resultados.append({
            "Usuário": usuarios["nome"],
            "Título": usuarios["titulo"],
            "Sentimento": usuarios["sentimento"]
        })
    csv_file = "Resultados.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=campos)
        csvwriter.writeheader()
        csvwriter.writerows(resultados)

def main():
    BASE_URL_USERS = "https://jsonplaceholder.typicode.com/users"
    usuarios = get_users(BASE_URL_USERS)
    info_completas = []
    for usuario in usuarios:
        id = usuario['id']
        nome = usuario['name']
        base_url_posts = f'https://jsonplaceholder.typicode.com/users/{id}/posts/'
        posts = get_users(base_url_posts)
        for post in posts:
            titulo = post['title']
            post_id = post['id']
            titulo_traduzido = traduzir_posts(titulo)
            sentimento_polarity = sentimento_text(titulo_traduzido)
            #verifica os sentimento do usuário
            if sentimento_polarity < 0:
                sentimento_polarity = "negativo"
            elif sentimento_polarity == 0:
                sentimento_polarity = "neutro"
            else:
                sentimento_polarity = "positivo"

            info_completas.append({
                'nome': nome,
                'titulo': titulo_traduzido,
                'Post_id': post_id,
                'sentimento': sentimento_polarity      
        })  
        resultados = usuarios_positivos(info_completas)
    for nome, dict_positivos in sorted(resultados.items(), key=order_positivos, reverse=True):
        print(f"Usuário: {nome}, Posts Positivos: {dict_positivos}")
        
    resultados_csv(info_completas)     
                    
if __name__ == '__main__':

    main()
