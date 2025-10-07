# 🐍 Projeto 01: Calculadora de Média de Notas (Python Fundamentals)

Este projeto marca a conclusão da minha fase inicial de estudos de Lógica de Programação e Estruturas de Dados em Python. Simula um sistema de entrada de notas para um aluno, calculando a média e definindo a situação final.

## 🎯 Objetivo

Consolidar o uso de **fluxo de controle** e **estruturas de dados básicas**.

## ✨ Funcionalidades

* Coleta dinâmica de notas até o usuário digitar "FIM".
* Proteção contra erro de Divisão por Zero.
* Cálculo da Média Final.
* Determinação da Situação do Aluno: Aprovado (>= 7.0), Recuperação (>= 5.0), Reprovado (< 5.0).

## 🛠️ Tecnologias Utilizadas

| Conceito | Aplicação no Código |
| :--- | :--- |
| **Lógica de Repetição** | `while True` para coleta de dados e `break` para saída controlada. |
| **Estruturas de Dados** | `Listas` (`notas`) para armazenar coleções de dados. |
| **Cálculo** | `float()` para conversão de entrada; `len()` para obter o total de notas. |
| **Controle de Fluxo** | `if/elif/else` para classificar a situação do aluno. |

## 💻 Como Rodar

1. Clone o repositório.
2. Execute o arquivo `calculadora_media.py` em seu terminal.

```bash
python calculadora_media.py
