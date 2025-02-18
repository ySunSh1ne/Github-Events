﻿### GitHub User Activity CLI

Este projeto é uma aplicação de linha de comando (CLI) simples que utiliza a API do GitHub para buscar as atividades recentes de um usuário e exibi-las no terminal.

## Objetivo do Projeto

O objetivo é praticar:
- Trabalhar com APIs.
- Manipular dados em formato JSON.
- Criar uma aplicação CLI funcional.

## Como Usar

### Passos
1. Clone este repositório ou copie o código para um arquivo chamado `github_events.py`.
2. No terminal, execute o seguinte comando:
   ```bash
   python github_events.py <username>
   ```
   Substitua `<username>` pelo nome de usuário do GitHub que deseja consultar.

### Caso de erro (usuário inválido)
Comando:
```bash
python github_activity.py usuarioinvalido123
```

Saída:
```
Erro: Usuário 'usuarioinvalido123' não encontrado.
```
## Sobre o Projeto
A ideia do projeto vem do site: [Roadmap.sh](https://roadmap.sh/projects/github-user-activity).
