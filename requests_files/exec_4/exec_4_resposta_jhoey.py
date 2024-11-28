import requests
import pandas as pd
import csv
 
def pegar_população_json(name: str):
    url_response = requests.get(f'https://restcountries.com/v3.1/name/{name}')
    if url_response.status_code == 200:
        info_paises_json = url_response.json()
    else:
        print('Erro na requisição')
        
    name_country = info_paises_json[0]['name']['common']
    population = info_paises_json[0]['population']
    lat_pais = info_paises_json[0]['capitalInfo']['latlng'][0]
    lon_pais = info_paises_json[0]['capitalInfo']['latlng'][1]
 
    return {
        "País": name_country,
        "População": population,
        "Latitude País": lat_pais,
        "Longitude País": lon_pais
    }
 
def lat_long_dados(pegar_população_json):
    latitude = pegar_população_json["Latitude País"]
    longitude = pegar_população_json["Longitude País"]
    api_key = '655abfe772c79fcd6669dde861cbf399'
    url_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric')
    if url_response.status_code == 200:
        temperatura = url_response.json()
    else:
        print('Erro na requisição')
    return temperatura

def save_csv(dict_infos):
     
    fields = ['Pais', 'Populacao', 'Temperatura Media']
    rows =  []
    for paises in dict_infos:
        rows.append({
            'Pais': paises['Pais'],
            'Populacao': paises['População'],
            'Temperatura Media': paises['Temperatura Media']
        })
    filename = 'correlacao_pais_temperatura.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as filename:
        csvwriter = csv.DictWriter(filename, fieldnames=fields)
        csvwriter.writeheader()
        csvwriter.writerows(rows)

def correlacao_pais_temperatura(dict_infos):                                                                  
    
   array_populacao = []
  
   
   for paises in dict_infos:
       pais = paises['Pais']
       array_populacao.append((paises['População'], paises['Temperatura Media']))
    
       for paises in array_populacao:
           df = pd.DataFrame(array_populacao, columns=['População', 'Temperatura Media'])
           print(df.corr())

     
def main():
    dict_infos = []
    lista = ['Brasil', 'Argentina', 'Syria', 'France', 'Paraguay', 'El Salvador', 'Ukraine', 'United States of America', 'Ecuador', 'Colombia' ]
    for populacao in lista:
        try:
            populacao_info = pegar_população_json(populacao)
            t = lat_long_dados(populacao_info)
            temperatura = t['main']['temp']
            sensacao_termica = t['main']['feels_like']
            temperatura_media = round(temperatura + sensacao_termica) / 2
            dict_infos.append({
            "Pais": populacao_info["País"],
            "População": populacao_info["População"],
            "Latitude": populacao_info["Latitude País"],
            "Longitude": populacao_info["Longitude País"],    
            "Temperatura Media": temperatura_media
        })
        except:
            print('Erro na requisição', populacao)
            pass
            
    save_csv(dict_infos)    

    teste = correlacao_pais_temperatura(dict_infos)
    
    

if __name__ == '__main__':
 
    main()