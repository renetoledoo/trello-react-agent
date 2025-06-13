# 🤖 Trellozinho – Assistente Virtual para o Trello

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![LangChain](https://img.shields.io/badge/langchain-integrado-yellow.svg)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)

O **Trellozinho** é um assistente virtual inteligente construído com LangChain, projetado para interagir com usuários em **português** e fornecer suporte especializado ao uso do **Trello**. Ele entende comandos naturais, consulta dados via API e respeita regras específicas para garantir respostas úteis e precisas.

![image](https://github.com/user-attachments/assets/bc4a0f08-ddff-4670-8053-49e85f39786b)

---

## 📌 Funcionalidades

- ✅ **Listagem de Projetos Trello**  
  Fornece os nomes dos projetos disponíveis e orienta o usuário sobre os próximos passos.

- ✅ **Definição de Projeto Atual**  
  Permite ao usuário escolher um projeto para consultar tarefas, prazos, membros e status.

- ✅ **Listagem de Status das Tarefas**  
  Exibe as listas (status) de tarefas dentro de um projeto Trello.

- ✅ **Consulta de Tarefas**  
  Obtém cards (tarefas) de um projeto específico.

- ✅ **Detalhes das Tarefas**  
  Recupera informações como nome, data de entrega e descrição dos cards.

- ✅ **Tarefas por Membro**  
  Lista tarefas atribuídas aos membros com dados como prazos e status.

- ✅ **Listagem de Membros**  
  Retorna os membros associados a um projeto Trello.

---

## 🧠 Inteligência do Agente

O Trellozinho foi desenvolvido com base no framework LangChain e no modelo GPT-4 da OpenAI. Ele:

- Compreende linguagem natural.
- Decide automaticamente se deve usar ferramentas integradas ou apenas responder de forma amigável.
- Segue regras rígidas para evitar uso indevido das ferramentas.

---

## 🔧 Tecnologias Utilizadas

- LangChain
- OpenAI GPT-4
- Decouple (para variáveis de ambiente)
- Python 3.10+
- Trello API (via wrapper `api.py`)

---
