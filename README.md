Alunos: Marcelo Negrão e Luísa Castro

# CRUD de Disciplinas com Testes Automatizados, BDD e GitHub Actions

## 📚 Sobre o Projeto
Este projeto foi desenvolvido com o objetivo de implementar um sistema **CRUD** (**Create, Read, Update, Delete**) para gerenciamento de disciplinas acadêmicas.

A aplicação permite armazenar e manipular informações de disciplinas utilizando **Python** e um arquivo **JSON** como mecanismo de persistência de dados.

Além da implementação do CRUD, o projeto também contempla:

- **testes automatizados**
- **cenários baseados em BDD**
- **cobertura de testes**
- **integração contínua com GitHub Actions**

O foco da atividade não foi apenas fazer o sistema funcionar, mas também aplicar práticas de **qualidade de software**, **organização de projeto** e **automação de validações**, como ocorre em projetos reais.

---

## 🎯 Objetivos da Atividade
Este projeto foi construído para atender aos seguintes objetivos:

- Implementar um CRUD funcional para disciplinas;
- Organizar o projeto em camadas simples e reutilizáveis;
- Utilizar **arquivo JSON** como forma de armazenamento;
- Criar testes automatizados para validar cada operação do sistema;
- Aplicar a lógica de **BDD (Behavior-Driven Development)**;
- Garantir no mínimo **75% de cobertura de testes**;
- Configurar uma **esteira automatizada com GitHub Actions** para validar alterações automaticamente.

---

## 🛠️ Tecnologias Utilizadas

As seguintes tecnologias e ferramentas foram utilizadas no projeto:

- **Python 3.11**
- **Pytest**
- **Pytest-Cov**
- **JSON**
- **Git**
- **GitHub**
- **GitHub Actions**

---

## 📂 Estrutura do Projeto

```bash
crud-disciplinas-bdd/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│   └── disciplinas.json
│
├── src/
│   ├── __init__.py
│   ├── disciplina.py
│   ├── service.py
│   └── storage.py
│
├── tests/
│   ├── __init__.py
│   ├── test_create.py
│   ├── test_read.py
│   ├── test_update.py
│   └── test_delete.py
│
├── requirements.txt
└── README.md
