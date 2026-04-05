# DOCUMENTAÇÃO DO PROJETO  
## CRUD de Disciplinas com Testes Automatizados, BDD e GitHub Actions

**Alunos:** Marcelo Negrão Mascarenhas Filho, Luísa Castro Santos  
**Disciplina:** Teste e Qualidade de Software  
**Professor:** Neuton Melo  

## Sumário

1. Introdução  
2. Objetivo do Projeto  
3. Tecnologias Utilizadas  
4. Estrutura e Funcionamento do Projeto  
5. Funcionamento do CRUD  
6. Persistência de Dados com JSON  
7. Testes Automatizados e BDD  
8. Cobertura de Testes  
9. GitHub Actions e Esteira Automatizada  
10. Conclusão  

## 1. Introdução

Este projeto foi desenvolvido com o objetivo de aplicar conceitos de teste e qualidade de software por meio da construção de um sistema CRUD para gerenciamento de disciplinas acadêmicas.

O sistema foi implementado em Python e utiliza um arquivo JSON para armazenar os dados. Além da funcionalidade principal do CRUD, o projeto também conta com testes automatizados, lógica baseada em BDD, análise de cobertura de testes e uma esteira automatizada com GitHub Actions.

A proposta da atividade foi desenvolver um sistema funcional e, ao mesmo tempo, aplicar boas práticas de organização, validação e automação.

## 2. Objetivo do Projeto

O objetivo principal deste projeto é permitir o cadastro e gerenciamento de disciplinas por meio das operações básicas de CRUD:

- Create (Criar)
- Read (Ler/Listar)
- Update (Atualizar)
- Delete (Deletar)

Além disso, o projeto busca aplicar conceitos importantes da área de qualidade de software, como testes automatizados, cobertura de testes e integração contínua.

## 3. Tecnologias Utilizadas

As principais tecnologias e ferramentas utilizadas foram:

- Python 3.11
- Pytest
- Pytest-Cov
- JSON
- Git
- GitHub
- GitHub Actions

## 4. Estrutura e Funcionamento do Projeto

O projeto foi organizado da seguinte forma:

```bash
crud-disciplinas-bdd/
│
├── .github/workflows/ci.yml
├── data/disciplinas.json
├── src/
│   ├── disciplina.py
│   ├── service.py
│   └── storage.py
├── tests/
│   ├── test_create.py
│   ├── test_read.py
│   ├── test_update.py
│   └── test_delete.py
├── requirements.txt
└── README.md
```

O arquivo disciplina.py representa a estrutura de uma disciplina, contendo seus atributos principais, como id, título, datas, número de vagas e se é disciplina de verão.

O arquivo storage.py é responsável por fazer a leitura e a gravação das informações no arquivo JSON, funcionando como a camada de persistência do sistema.

O arquivo service.py contém a lógica principal do projeto, sendo responsável por executar as operações do CRUD.

A pasta tests contém os testes automatizados do sistema, enquanto o arquivo requirements.txt lista as bibliotecas necessárias para o projeto funcionar.

O arquivo ci.yml, localizado dentro de .github/workflows, define a esteira automatizada do projeto utilizando GitHub Actions.

5. Funcionamento do CRUD

O sistema foi desenvolvido com base nas quatro operações fundamentais do CRUD.

A operação de Create é responsável por cadastrar uma nova disciplina no sistema.

A operação de Read é responsável por listar as disciplinas cadastradas.

A operação de Update permite alterar os dados de uma disciplina já existente.

A operação de Delete remove uma disciplina cadastrada.

Toda a lógica dessas operações foi centralizada no arquivo service.py.

6. Persistência de Dados com JSON

Neste projeto, optou-se pelo uso de um arquivo JSON em vez de banco de dados tradicional, pois a proposta da atividade não exigia uma estrutura mais complexa.

O arquivo utilizado foi:

data/disciplinas.json

Esse arquivo funciona como um banco de dados simples, armazenando os registros das disciplinas cadastradas.

Exemplo de registro salvo:

[
  {
    "id": 1,
    "titulo": "Programação Orientada a Objetos",
    "data_inicio": "2026-03-01",
    "data_termino": "2026-07-10",
    "numero_vagas": 30,
    "verao": false
  }
]
7. Testes Automatizados e BDD

Os testes automatizados foram implementados para garantir que cada funcionalidade principal do sistema funcione corretamente.

Foram criados testes para:

criação de disciplina;
leitura de disciplinas;
atualização de disciplina;
exclusão de disciplina.

Esses testes foram executados com a ferramenta Pytest.

Além disso, a lógica do projeto foi pensada com base em BDD (Behavior-Driven Development), ou seja, orientada ao comportamento esperado do sistema.

A ideia foi validar cenários como:

dado que não existe disciplina cadastrada, quando uma nova disciplina for criada, então ela deve ser salva corretamente;
dado que existe uma disciplina cadastrada, quando ela for listada, então deve aparecer corretamente;
dado que existe uma disciplina cadastrada, quando seus dados forem alterados, então a atualização deve funcionar;
dado que existe uma disciplina cadastrada, quando ela for removida, então ela não deve mais existir no sistema.
8. Cobertura de Testes

A cobertura de testes foi medida com a ferramenta pytest-cov.

O projeto atingiu:

90% de cobertura de testes

Esse valor supera o requisito mínimo exigido pela atividade, que era de:

75% de cobertura

Isso demonstra que a maior parte da lógica do sistema está sendo validada automaticamente.

9. GitHub Actions e Esteira Automatizada

O GitHub Actions foi utilizado para automatizar a validação do projeto.

A esteira foi configurada no arquivo:

.github/workflows/ci.yml

Ela foi programada para rodar automaticamente quando houver:

push para a branch main;
pull request para a branch main.

Sempre que for acionada, a esteira executa automaticamente as seguintes etapas:

baixa o código do repositório;
configura o ambiente Python;
instala as dependências;
roda os testes automatizados;
verifica se a cobertura está acima de 75%.

A pipeline falha quando:

algum teste falha;
a cobertura fica abaixo de 75%.

Durante o desenvolvimento, foi realizado um teste prático para validar o funcionamento da esteira. Foi alterado propositalmente o valor esperado de um teste de criação de disciplina, mudando o ID esperado de 1 para 999. Com isso, a pipeline falhou corretamente, mostrando que a automação está funcionando como esperado.

10. Conclusão

O desenvolvimento deste projeto permitiu aplicar, de forma prática, conceitos importantes relacionados à qualidade de software.

Entre os principais pontos trabalhados estão:

implementação de CRUD;
organização de projeto em Python;
persistência de dados com JSON;
testes automatizados;
aplicação de BDD;
cobertura de testes;
automação com GitHub Actions.
