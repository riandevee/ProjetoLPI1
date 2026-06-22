# Gestão de Obras, Equipamentos e Contratos

Sistema em Python orientado a objetos para cadastro e controle de **obras**, **equipamentos** (com herança: Betoneira e Furadeira), **empreiteiros** e **contratos**, desenvolvido como projeto da disciplina de Linguagem de Programação I (LPI) — Sistemas de Informação, FACET/UFGD.

## Sobre o projeto

O sistema permite cadastrar obras de construção civil, alocar equipamentos específicos para cada obra e formalizar contratos entre obras e empreiteiros responsáveis pela execução. Todo o cadastro é feito via interface textual, com persistência dos dados em arquivo binário entre execuções.

## Funcionalidades

- **Cadastro via interface textual** de Empreiteiros, Equipamentos, Obras e Contratos
- **Herança**: a classe `Equipamento` é especializada em `Betoneira` (tipo, voltagem, capacidade) e `Furadeira` (perfuração, aplicação)
- **Relacionamento n:n** entre Obras e Equipamentos — cada obra pode referenciar múltiplos equipamentos, e o mesmo equipamento pode ser usado em diferentes obras
- **Entidade associadora** `Contrato`, vinculando Obra e Empreiteiro
- **Impressão formatada** com colunas alinhadas dinamicamente conforme o maior valor de cada campo
- **Filtragem progressiva** de contratos por múltiplos critérios combinados:
  - data mínima do contrato
  - prefixo do nome do empreiteiro
  - método de execução da obra (horizontal/vertical)
  - peso máximo dos equipamentos
  - capacidade mínima da betoneira
  - tipo de perfuração da furadeira
- **Persistência em arquivo** (`pickle`) com tratamento de exceções para carregamento e salvamento automático ao iniciar/encerrar a aplicação

## Estrutura do projeto

```
src/
├── controle/
│   └── projeto.py              # ponto de entrada: salvar/recuperar e loop principal
├── entidades/
│   ├── contrato.py              # classe associadora Contrato + filtragem
│   ├── empreiteiro.py           # classe Empreiteiro
│   ├── equipamento.py           # classe Equipamento + subclasses Betoneira/Furadeira
│   └── obra.py                  # classe Obra
├── interfaces/
│   └── interface_textual.py     # leitura de dados via terminal e menus
└── util/
    ├── data.py                  # classe Data (datas customizadas)
    ├── gerais.py                 # funções genéricas de impressão
    └── persistência_arquivo.py  # salvar/carregar objetos em .bin
```

## Como executar

```bash
cd src/controle
python projeto.py
```

Ao iniciar, o sistema carrega automaticamente os dados salvos anteriormente (se existirem) e apresenta o menu principal:

```
Opções [C: Cadastrar / I: Imprimir / S: Selecionar / T: Imprimir Todos / <ENTER>: Parar]
```

## Modelo de dados

- **Empreiteiro**: nome, telefone, email, endereço
- **Equipamento** (superclasse): nome, valor, peso, disponível
  - **Betoneira**: capacidade, voltagem, tipo
  - **Furadeira**: perfuração, aplicação
- **Obra**: id, descrição, datas, execução *(referencia múltiplos Equipamentos)*
- **Contrato**: data *(referencia uma Obra e um Empreiteiro)*

## Autor

Rian Ruela Ribeiro — Sistemas de Informação, UFGD
