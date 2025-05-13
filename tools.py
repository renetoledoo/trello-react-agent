from langchain.agents import Tool
import api
import json 

id_projeto = None;

def definir_projeto(args):
    global id_projeto
    search = api.obter_projetos(args)
    search = json.loads(search)

    for projeto in search:
        if args.lower() in projeto['name'].lower():
            id_projeto = projeto['id']
            print('Salvo , ', id_projeto)
            return f"Projeto '{projeto['name']}' definido com sucesso! Agora você está liberado para consultas quaisquer informação do projeto"
    
    return "Nenhum projeto encontrado com o nome especificado."


obter_projetos_tool = Tool(
    name='Obter Lista de Projetos',
    description='Fornece a lista de todos os projetos disponíveis no Trello.',
    func=api.obter_projetos
)

listar_listas_tool = Tool(
    name='Listar Status disponíveis para as tarefas do Projeto',
    description='Fornece os status ou listas de um projeto específico.',
    func=api.obter_listas_projeto
)

obter_cards_projeto_tool = Tool(
    name='Obter Tarefas da Lista',
    description='Obtém os cards, Tarefas que estão associados a uma lista de um projeto específico. É necessário informar o ID do Projeto',
    func=api.obter_cards_projeto
)

definir_variavel_tool = Tool(
    name="Definir Projeto escolhido",
    description="Ferramenta para definir quando um projeto for escolhido pelo usuario",
    func = definir_projeto
)

obter_detalhes_card_tool = Tool(
    name = 'Obter informação do card',
    description='Obtém informação do card ou tarefa associado a um projeto específico, como nome, data prazo e descrição do projeto',
    func = api.obter_detalhes_card
)


obter_tarefas_membros = Tool(
    name = 'Obter tarefas dos membros',
    description='Ferramenta opara obter tarefas atribuídas a cada membro junto das informações como prazo, e conclusão, de um projeto específico no Trello',
    func = api.obter_tarefas_membro_invoke
)


obter_membros = Tool(
    name = 'Obter os membros',
    description='Ferramenta opara obter todos os membros de um projeto específico',
    func = api.obter_membros_projeto
)