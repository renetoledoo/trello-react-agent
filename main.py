import os 
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.callbacks import get_openai_callback
import tools as ferramentas
from decouple import config
os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

model = ChatOpenAI(model='gpt-4', temperature=0)


prompt = '''
Você é o assistente virtual chamado "Trellozinho", especializado no Software Trello. 
Sua missão é ajudar os usuários respondendo perguntas de forma clara e precisa. 

- Quando alguém fizer uma pergunta que utilize a função Listar Status disponíveis para as tarefas do Projeto, não utilize a ferramenta Obter Lista de Projetos.
- Quando for utilizar a ferramenta Obter Tarefas da Lista, não utilize a ferramenta Obter Lista de Projetos.
- Caso o usuário faça uma pergunta casual ou de conversa, não utilize nenhuma ferramenta e apenas forneça uma resposta amigável. 
- Caso algum usuário peça para listar os projetos, lista apenas os nomes e no final Peça para que ele escolha um para obter informações como Tarefas, Prazos.
- Quando Definir Projeto escolhido, não execute nenhuma outra ferramente que não foi solicitada pelo usuário, retorne uma lista do que o usuário pode solicitar com base no projeto que foi escolhido. 
Pergunta: {q}

Para pesquisas que necessitem utilizar parâmetros, utilize:
Parâmetro: {id}


Regra mais importante: Caso não entenda a pergunta, peça educadamente repetir de forma clara e objetiva.

Regras:
- Sempre responder em português brasileiro.
- Para perguntas informais ou casuais, apenas forneça uma resposta amigável sem recorrer às ferramentas do Trello.

'''
prompt_template = PromptTemplate.from_template(prompt)



tools = [ferramentas.obter_projetos_tool, ferramentas.listar_listas_tool, ferramentas.obter_cards_projeto_tool, ferramentas.definir_variavel_tool, ferramentas.obter_detalhes_card_tool, ferramentas.obter_tarefas_membros, ferramentas.obter_membros]

react_instructions = hub.pull('hwchase17/react')

        
react_agent = create_react_agent(
    llm=model,
    tools=tools,
    prompt=react_instructions
)

agent_instance = AgentExecutor(
    agent=react_agent,
    tools=tools,
)


def chamarChat(msg: str):
    with get_openai_callback() as cb:
            print('ID Sendo Executada: ', ferramentas.id_projeto)
            response = agent_instance.invoke({'input': prompt_template.format(q=msg, id=ferramentas.id_projeto)})
            return response.get('output', 'Resposta não encontrada.')
        
        
      
