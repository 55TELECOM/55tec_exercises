import requests
import operator
import csv

def pegar_populacao(url):
    lista_populacao = []
    paises = requests.get(url)
    paises_json = paises.json()
    cont = 0
    for population in paises_json:
        if cont <=19:
            pais = population['name']['common']
            populacao = population["population"]
            area = population['area']
            densidade_populacional = populacao / area
            print(type(densidade_populacional))
            lista_populacao.append({
            'País': pais,
            'População': f'{populacao:.2f}',
            'Área': f'{area:.2f}km²',
            'Densidade_Populacional': densidade_populacional
        })
        cont += 1
    return lista_populacao

def obter_densidade(pais):
    return pais['Densidade_Populacional']

def csv_densidade(paises_ordenados):
    campos = ['País', 'População', 'Área', 'Densidade Populacional']
    resultados = []
    for results in paises_ordenados:
        dens_form = results['Densidade_Populacional']
        resultados.append({
            'País': results['País'],
            'População': results['População'],
            'Área': results['Área'],
            'Densidade Populacional': f'{dens_form:.2f}'
        })
    csvfile = "Lista_Densidade.csv"
    with open(csvfile, 'w', newline='', encoding= 'utf-8') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=campos)
        csvwriter.writeheader()
        csvwriter.writerows(resultados)
        
def main():
    url = "https://restcountries.com/v3.1/all"
    populacao_paises = pegar_populacao(url)
    paises_ordenados = sorted(populacao_paises, key=obter_densidade, reverse=True)
    csv_densidade(paises_ordenados)
    

if __name__ == "__main__":
    main()