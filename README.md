# 🏥 Sistema de Registro de Pacientes

Este repositório contém a documentação técnica do projeto desenvolvido para a disciplina de **Laboratório de Programação Back End**, cujo objetivo é apresentar um sistema completo de registro de pacientes, incluindo funcionalidades de **cadastro**, **histórico médico**, **agendamentos** e **relatórios clínicos**.

---

## 📚 Sumário

- [Objetivo do Projeto](#objetivo-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Diagramas](#diagramas)
  - [Diagrama de Entidade-Relacionamento (ER)](#diagrama-de-entidade-relacionamento-er)
  - [Diagrama de Casos de Uso](#diagrama-de-casos-de-uso)
  - [Fluxogramas](#fluxogramas)

---

## 🎯 Objetivo do Projeto

Desenvolver a documentação de um sistema Back End para gerenciamento de pacientes em uma clínica médica, com foco em:

- Organização dos dados clínicos
- Facilidade de acesso ao histórico médico
- Agendamento de consultas
- Geração de relatórios clínicos

---

## ⚙️ Funcionalidades

- **Cadastro de Pacientes**: Nome, CPF, data de nascimento, contato, endereço.
- **Histórico Médico**: Diagnósticos, prescrições, exames realizados.
- **Agendamentos**: Marcação de consultas com data, hora e profissional.
- **Relatórios Clínicos**: Geração de PDFs com resumo do histórico e atendimentos.

---

## 🛠️ Tecnologias Utilizadas

- Linguagem: `JavaScript` / `Node.js`
- Banco de Dados: `PostgreSQL`
- Ferramentas de Modelagem: `Draw.io`, `Lucidchart`, `DBDesigner`
- Documentação: `Markdown`, `PlantUML`

---

## 📊 Diagramas

### 📌 Diagrama de Entidade-Relacionamento (ER)

Representa a estrutura do banco de dados, com as principais entidades e seus relacionamentos:

- **Paciente**
- **Consulta**
- **Profissional**
- **Histórico Médico**
- **Relatório**

> 📎 O diagrama ER está disponível na pasta `docs/diagramas/er.png`

---

### 🎭 Diagrama de Casos de Uso

Descreve as interações entre os usuários (Recepcionista, Médico, Administrador) e o sistema:

- Cadastrar paciente
- Consultar histórico
- Agendar consulta
- Gerar relatório

> 📎 O diagrama de casos de uso está disponível em `docs/diagramas/casos_uso.png`

---

### 🔄 Fluxogramas

Fluxos operacionais das principais funcionalidades:

- Fluxo de cadastro de paciente
- Fluxo de agendamento de consulta
- Fluxo de geração de relatório

> 📎 Os fluxogramas estão disponíveis em `docs/diagramas/fluxogramas/`

---

## 👥 Autores

- [Seu Nome Aqui]
- [Nome do(s) colega(s) de equipe]
- Curso: [Nome do curso]
- Instituição: [Nome da instituição]

---

> Para mais detalhes, consulte os arquivos na pasta `docs/` deste repositório.
