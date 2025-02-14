# Análise de Estatísticas de Chutes em Competições de Futebol

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este projeto analisa as estatísticas de chutes de jogadores em várias competições de futebol, como Champions League, Premier League, La Liga, entre outras. Ele fornece insights sobre os melhores jogadores em termos de chutes, chutes no alvo e outras métricas importantes.

---

## Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Como Executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Requisitos](#requisitos)
- [Exemplo de Uso](#exemplo-de-uso)
- [Licença](#licença)
- [Contribuição](#contribuição)
- [Autor](#autor)

---

## Descrição

O script principal (`analise.py`) permite ao usuário escolher uma liga e duas equipes para comparar os melhores jogadores com base em suas estatísticas de chutes. As estatísticas incluem:
- Total de chutes.
- Chutes no alvo.
- Média de chutes por jogo (chutes/90 minutos).
- Distância média dos chutes.

Os dados são carregados de arquivos JSON contendo informações detalhadas sobre os jogadores e suas performances.

---

## Funcionalidades

- Escolha de ligas populares (Champions League, Premier League, etc.).
- Comparação de equipes dentro da mesma liga.
- Exibição dos melhores jogadores de cada equipe com base em diferentes métricas.
- Formatação colorida e tabular para facilitar a leitura das estatísticas.

---

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina (versão 3.x recomendada).
2. Instale as bibliotecas necessárias:
   ```bash
   pip install tabulate colorama

## Exemplo de Uso

Aqui está como o programa se parece ao ser executado:

![Exemplo de Saída no Terminal](https://github.com/NatanSzyslak/shooting-stats-analysis/blob/main/prnt.png)

1. Escolha uma liga:
2. Escolha as euipes que vão se enfrentar
