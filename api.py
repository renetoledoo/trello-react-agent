import requests
import json
from decouple import config


API_KEY = config('API_KEY')
TOKEN = config('TOKEN')
KEY =  config('KEY')
query = {
    'key': API_KEY,
    'token': TOKEN
}


def obter_listas_projeto(id_projeto):
    
    url = f"https://api.trello.com/1/boards/{id_projeto}/lists"
    headers = {
    "Accept": "application/json"
    }
    response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
    )

    print('Minha URL > ', url)
    if response.status_code == 200:
            try:
                meu_json = response.json()
                nomes_listas = [item['name'] for item in meu_json]
                
                return nomes_listas
            except json.JSONDecodeError:
                print("Erro ao decodificar a resposta JSON:", response.text)
    else:
            print(f"Erro na requisição, código de status: {response.status_code}")
            return []


def obter_cards_projeto(id_projeto):
    url = f"https://api.trello.com/1/boards/{id_projeto}/cards"
    response = requests.request(
    "GET",
    url,
    params=query
    )
    meu_json = json.loads(response.text)
    nomes_Card = [item['name']  for item in meu_json ]
    return nomes_Card



def obter_detalhes_card(id_projeto):
    url = f"https://api.trello.com/1/boards/{id_projeto}/cards"
    response = requests.request(
    "GET",
    url,
    params=query
    )
    meu_json = json.loads(response.text)
    
    resultado = []
    for card in meu_json:
        resultado.append({
            'nome': card.get('name'),
            'dataPrazo': card.get('due'),
            'descricao': card.get('desc'),
            'concluida': card.get('dueComplete')
        })
    return resultado


def obter_prazos(id_projeto):
    url = f"https://api.trello.com/1/boards/{id_projeto}/cards"
    response = requests.request(
    "GET",
    url,
    params=query
    )
    meu_json = json.loads(response.text)
    
    resultado = []
    for card in meu_json:
        resultado.append({
            'nome': card.get('name'),
            'dataPrazo': card.get('due'),
            'descricao': card.get('desc')
        })
    return resultado


def procurar_trello(query_search):
    url = "https://api.trello.com/1/search"

    headers = {
    "Accept": "application/json"
    }

    query['query'] = query_search

    response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

def obter_projetos(args):
    url = "https://api.trello.com/1/members/me/boards"
    params = {
        "fields": "name,url",
        "key": KEY,
        "token": TOKEN
    }
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.text


def obter_membros_projeto(id_projeto):
    url = f"https://api.trello.com/1/boards/{id_projeto}/members"

    headers = {
    "Accept": "application/json"
    }

    response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
    )
    print(response)
    meu_json = json.loads(response.text)
    return meu_json


def obter_tarefas_membros_executor(id_membro):
    url = f"https://api.trello.com/1/members/{id_membro}/cards"
    
    headers = {
    "Accept": "application/json"
    }

    response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
    )
    meu_json = json.loads(response.text)
    return meu_json


def obter_tarefas_membro_invoke(id_projeto):
    membros = obter_membros_projeto(id_projeto)
    resultado = []

    for membro in membros:
        codigo_membro = membro.get('id')
        nome_membro = membro.get('fullName')

        cards = obter_tarefas_membros_executor(codigo_membro)
        tarefas = []

        for card in cards:
            tarefas.append({
                "nome": card.get('name'),
                "prazo": card.get('due'),
                "concluído": card.get('dueComplete')
            })

        resultado.append({
            "membro": nome_membro,
            "tarefas_membro": tarefas
        })

    return resultado



