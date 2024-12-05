import requests
import csv


def pegar_população_json(name: str):
    url_response = requests.get(f'https://restcountries.com/v3.1/name/{name}')
    info_paises_json = url_response.json()

    population = info_paises_json[0]['population']
    pais = info_paises_json[0]['name']['common']
    lat_pais = info_paises_json[0]['capitalInfo']['latlng'][0]
    lon_pais = info_paises_json[0]['capitalInfo']['latlng'][1]
 
    return {
        "População": population,
        "Capital": pais,
        "Latitude País": lat_pais,
        "Longitude País": lon_pais
    }

def lat_long_dados(pegar_população_json):
    latitude = pegar_população_json["Latitude País"]
    longitude = pegar_população_json["Longitude País"]
    api_key = '655abfe772c79fcd6669dde861cbf399'
    url_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric')
    temperatura = url_response.json()
    temperatura_atual = temperatura['main']['temp']
    temperatura_sensacao = temperatura['main']['feels_like']
    
    return {
        "Temperatura_Atual": temperatura_atual,
        "Sensação Térmica": temperatura_sensacao
    }

def Paises_csv(dict_infos):
    campos = ['País', 'População', 'Temperatura Média']
    csv_infos = []
    for paises in dict_infos:
        csv_infos.append({
            'País': paises['País'],
            'População': paises['População'],
            'Temperatura Média': paises['Temperatura Média']
        })
    csv_results = 'Paises.csv'
    with open(csv_results, 'w', newline='', encoding='utf-8') as csv_results:
        csvwriter = csv.DictWriter(csv_results, fieldnames=campos)
        csvwriter.writeheader()
        csvwriter.writerows(csv_infos)

def main():
    dict_infos = []
    lista = ['Brasil', 'Argentina', 'Syria', 'France', 'Paraguay', 'El Salvador', 'Ukraine', 'Norway', 'Namibia', 'United Arab Emirates' ]
    for populacao in lista:
        populacao_info = pegar_população_json(populacao)
        temperatura = lat_long_dados(populacao_info)
        temp_atual = temperatura["Temperatura_Atual"]
        temp_sens = temperatura["Sensação Térmica"]
        temp_mediaa = (temp_sens + temp_atual) / 2
        populacao_atual = populacao_info["População"]
        pais_info = populacao_info["Capital"]
        dict_infos.append({
            "País": pais_info,
            "População": f"{populacao_atual:,.2f}",
            "Temperatura Média": f"{temp_mediaa:.2f}°C"
        })
    
    Paises_csv(dict_infos)
        

        
        

if __name__ == '__main__':

    main()