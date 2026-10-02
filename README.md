# 📝 Lista de Tarefas

## Descrição
Aplicação web de lista de tarefas, onde o usuário pode adicionar, marcar como concluída e remover tarefas. As tarefas ficam salvas em um banco PostgreSQL, então continuam lá mesmo depois de reiniciar a aplicação.

## Tecnologias Utilizadas
- **Backend:** Python + Flask + Flask-SQLAlchemy
- **Banco de dados:** PostgreSQL 16
- **Frontend:** HTML, CSS e JavaScript (puro)
- **Containerização:** Docker e Docker Compose
- **Servidor de aplicação:** Gunicorn
- **CI/CD:** GitHub Actions

## Como executar (Docker Compose)

1. Clone o repositório:
```bash
git clone https://github.com/Nickolas30/todo-app.git
cd todo-app
```

2. Crie o arquivo de variáveis de ambiente e troque a senha:
```bash
cp .env.example .env
```
(no PowerShell, use `copy .env.example .env`)

3. Suba a aplicação e o banco:
```bash
docker compose up --build
```

4. Acesse no navegador:
http://localhost:5000

Para parar: `docker compose down`. Os dados ficam guardados em um volume do Docker e só são apagados com `docker compose down -v`.

## Estrutura
- `app.py`: rotas da API e modelo do banco
- `templates/index.html`: interface
- `Dockerfile`: imagem da aplicação
- `docker-compose.yml`: aplicação + PostgreSQL
- `.github/workflows/docker-build.yml`: build automático no GitHub Actions

## Autores
- Nickolas Eduardo Gonçalves de Oliveira
- Nicolas Carneiro de Lima
