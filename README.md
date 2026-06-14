# 📝 To-Do List App

## Descrição
Aplicação web simples de lista de tarefas (To-Do List), onde o usuário pode adicionar, marcar como concluída e remover tarefas. O projeto resolve o problema de organização de tarefas diárias de forma rápida e visual.

## Tecnologias Utilizadas
- **Backend:** Python + Flask
- **Frontend:** HTML, CSS e JavaScript (puro)
- **Containerização:** Docker
- **CI/CD:** GitHub Actions

## Guia de Instalação (via Docker)

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/todo-app.git
cd todo-app
```

2. Construa a imagem Docker:
```bash
docker build -t todo-app .
```

3. Execute o container:
```bash
docker run -p 5000:5000 todo-app
```

4. Acesse no navegador:
http://localhost:5000

## Membros da Duo
- Nickolas Eduardo Gonçalves de Oliveira — Matrícula: 01711842
- Nicolas Carneiro de Lima — Matrícula: 01706055