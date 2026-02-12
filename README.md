# 🚀 Sistema de Gerenciamento de Usuários

> Projeto acadêmico desenvolvido com **FastAPI**, **Python** e **SQLite**, aplicando conceitos de **Orientação a Objetos** e integração entre **backend (API)** e **frontend**.

<br>

## 🧩 Sobre o Projeto

Este projeto consiste em um sistema simples de gerenciamento de usuários, permitindo **cadastrar** e **listar** usuários por meio de uma **API REST**, consumida por um frontend em HTML, CSS e JavaScript.

O foco principal é aplicar:
- Organização em camadas
- Boas práticas de backend
- Persistência de dados
- Comunicação entre frontend e backend

<br>

## 🛠️ Tecnologias

### Backend
- 🐍 Python 3.10+
- ⚡ FastAPI
- 🌐 Uvicorn
- 🗄️ SQLAlchemy
- 💾 SQLite

### Frontend
- 🌍 HTML5
- 🎨 CSS3
- 🧠 JavaScript (Fetch API)

<br>

## 🗂️ Estrutura do Projeto

```text
projeto-fastapi-usuarios/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database/
│   │   │   └── connection.py
│   │   ├── models/
│   │   │   └── user_model.py
│   │   ├── schemas/
│   │   │   └── user_schema.py
│   │   ├── repositories/
│   │   │   └── user_repository.py
│   │   └── controllers/
│   │       └── user_controller.py
│   ├── requirements.txt
|   ├── users.db
|   └──  public/
│         ├── index.html
│         └── script.js
└── README.md
```
<br>

## 🧠 Arquitetura

O projeto segue uma arquitetura em camadas, garantindo separação de responsabilidades:

- Controllers → Rotas da API
- Repositories → Lógica de acesso ao banco de dados
- Models → Entidades do sistema
- Schemas → Validação e transporte de dados
- Database → Configuração da conexão com o SQLite

Essa abordagem facilita a manutenção, leitura e evolução do código.

<br>

## ⚙️ Instalação
```text
1️⃣ É necessario ter o python 3 instalado na maquina

▶️ Instalar dependências
python -m pip install -r backend/requirements.txt

▶️ Executando a Aplicação
Backend
cd backend
python -m uvicorn app.main:app --reload --port 3000


📍 O frontend esta servido pelo FastAPI:

http://localhost:3000


📄 Documentação automática (Swagger):

http://localhost:3000/docs

O frontend se comunica com a API em:

http://localhost:3000/api/users
```
<br>

✨ Funcionalidades

- Cadastro de usuários
- Listagem de usuários
- Persistência de dados com SQLite
- API orientada a objetos
- Integração frontend + backend
