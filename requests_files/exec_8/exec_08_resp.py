import requests
import json
import numpy as np
import csv

def get_infos(ptbr, api_key):
    response = requests.get(f"https://api.themoviedb.org/3/movie/top_rated?language={ptbr}&api_key={api_key}")
    response_json = response.json()
    return response_json

def films_avaliation(films_avaliation):
    films_list = []
    filmes = films_avaliation["results"]
    for filmes in filmes:
        films_name = filmes["title"]
        films_avali = filmes["vote_average"]
        num_avaliations = filmes["vote_count"]
        films_list.append({
            "Filmes": films_name,
            "Avaliação": films_avali,
            "Número de avaliações": num_avaliations
        })
    return films_list

def desvio_padrão(avaliations):
    lista_desvio = list()
    for avaliacoes in avaliations:
        avaliacao = avaliacoes["Avaliação"]
        lista_desvio.append(
             avaliacao
        )
    desvio = np.std(lista_desvio)
    return desvio

def csv_file(infos_avaliation):
    campos = ['Filme', 'Nota Média', 'Número de avaliações']
    lista_csv = []
    for list_csv in infos_avaliation:
        lista_csv.append({
            'Filme': list_csv["Filmes"],
            'Nota Média': list_csv["Avaliação"],
            'Número de avaliações': list_csv["Número de avaliações"],
        }) 
    csvfile = "ranking_filmes.csv"
    with open(csvfile,'w', newline='', encoding = 'utf-8') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=campos)
        csvwriter.writeheader()
        csvwriter.writerows(lista_csv)


def main():
    api_key = "9f9484e14a6a8f0808099a62f36af9e8"
    language = 'pt-BR'
    infos_filmes = get_infos(language, api_key)
    infos_avaliation = films_avaliation(infos_filmes)
    desvio = desvio_padrão(infos_avaliation)
    csv_file(infos_avaliation)
    print(f'O desvio padrão entre os filmes é: {desvio}')


if __name__ == "__main__":
    main()
    