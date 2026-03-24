# Sistema de Gestão de Stock - Materiais Escolares

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)]()

> **Contexto Académico:** 10.º Ano | Programação e Sistemas de Informação (PSI)  
> **Objetivo:** Desenvolver um programa em Python que utiliza funções para gerir o stock de materiais escolares de uma escola, permitindo registo, consulta e atualização eficiente.

---

## Descrição do Projeto

Este projeto consiste num sistema de gestão de stock para materiais escolares (canetas, cadernos, borrachas, etc.), desenvolvido em Python. O programa automatiza o processo de registo manual, implementando uma solução modular baseada em funções que permite:

- Registar novos materiais com validação de dados
- Consultar stock de materiais específicos
- Atualizar quantidades (adição/remoção) com controlo de erros
- Exibir estado geral do stock em formato tabular
- Exportar dados para ficheiro de texto (funcionalidade extra)

---

## Funcionalidades

| Opção | Funcionalidade | Descrição |
|:-----:|----------------|-----------|
| 1 | **Adicionar Material** | Regista novos materiais com validação de quantidades (impede valores negativos e duplicados) |
| 2 | **Consultar Stock** | Pesquisa e exibe a quantidade disponível de um material específico |
| 3 | **Atualizar Stock** | Adiciona ou remove quantidades de materiais existentes com validação de stock suficiente |
| 4 | **Exibir Stock Geral** | Apresenta tabela completa com todos os materiais e respetivas quantidades |
| 5 | **Exportar Stock** | Gera ficheiro `.txt` com timestamp (YYYY.MM.DD.HH.MM.SS-Stock_Export.txt) |
| 6 | **Sair** | Encerra o programa de forma segura |

---

## Arquitetura do Programa

O programa está organizado em **funções modulares**, cada uma com responsabilidade única:

```python
def adicionar_material(stock)    # Registo de novos materiais
def consultar_stock(stock)       # Pesquisa de materiais
def atualizar_stock(stock)       # Gestão de entradas/saídas
def exibir_stock(stock)          # Visualização geral
def file_export(stock)           # Persistência de dados
def main()                       # Orquestração do menu principal
