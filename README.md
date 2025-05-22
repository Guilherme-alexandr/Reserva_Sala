# Microsserviço de Reservas de Salas

Este projeto é um microsserviço independente responsável pela criação e consulta de reservas de salas de aula. Ele é vinculado à API principal de gerenciamento de alunos, professores e turmas, disponível em:  
🔗 https://github.com/Guilherme-alexandr/teste-api-school

⚠️ Este serviço depende da API principal para validar o ID das turmas antes de registrar uma reserva.

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Flask
- Flask-CORS
- Flask-SQLAlchemy
- SQLite (banco local)
- Requests (integração entre serviços)
- Estrutura baseada em MVC (Model-View-Controller)

## 📁 Estrutura do Projeto

.
├── app.py  
├── config.py  
├── database.py  
├── requirements.txt  
├── models/  
│   └── reserva_model.py  
├── controllers/  
│   └── reserva_route.py  

## ⚙️ Funcionalidades

- ✅ Criar reservas (verifica previamente o ID da turma via API externa)
- ✅ Listar todas as reservas
- ✅ Consultar uma reserva específica por ID
- ✅ Atualizar reserva existente
- ✅ Deletar uma reserva
- 🔁 Integração com a API de gerenciamento para validação de turmas

## 🔌 Integração com API Principal

Este microsserviço consome a seguinte rota da API principal:

GET http://localhost:8000/turmas/filtrar/{turma_id}

Você precisa rodar o projeto principal antes de iniciar este microsserviço para que a verificação funcione corretamente.

## ▶️ Como Rodar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-repo-reservas
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Garanta que a API principal (teste-api-school) esteja em execução:
   ```bash
   git clone https://github.com/Guilherme-alexandr/teste-api-school  
   cd teste-api-school  
   python app.py
   ```

4. Em outro terminal, rode o microsserviço de reservas:
   ```bash
   python app.py
   ```

A API de reservas estará disponível em:  
http://localhost:9000/reservas

## 🧪 Exemplos de Rotas

- POST /reservas/criar  
  Corpo JSON:
  ```json
  {
    "turma_id": 1,
    "sala": "A101",
    "data": "2024-05-22",
    "hora_inicio": "09:00",
    "hora_fim": "11:00"
  }
  ```

- GET /reservas/listar  
- GET /reservas/filtrar/1  
- PUT /reservas/atualizar/1  
- DELETE /reservas/deletar/1  
