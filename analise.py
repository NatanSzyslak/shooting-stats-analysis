import json
import os
from tabulate import tabulate  # Certifique-se de instalar essa biblioteca: pip install tabulate
from colorama import Fore, Style, init  # Certifique-se de instalar essa biblioteca: pip install colorama

# Inicializa o colorama
init(autoreset=True)

# Função para carregar os dados de um arquivo JSON
def load_data_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{Fore.RED}Arquivo {filename} não encontrado.{Style.RESET_ALL}")
        return None
    except json.JSONDecodeError:
        print(f"{Fore.RED}Erro ao decodificar o JSON no arquivo {filename}.{Style.RESET_ALL}")
        return None

# Função para filtrar os melhores jogadores de uma equipe (ordenados por chutes)
def get_top_players_by_team(data, team_name, metric='shots', top_n=5):
    filtered_data = [player for player in data if player.get('team') == team_name and player.get(metric)]
    sorted_data = sorted(filtered_data, key=lambda x: float(x[metric]) if x[metric] else 0, reverse=True)
    return sorted_data[:top_n]

# Função para formatar os dados em uma tabela com cores
def format_player_stats_table(players):
    table = []
    headers = [
        f"{Fore.YELLOW}Jogador{Style.RESET_ALL}",
        f"{Fore.YELLOW}Chutes{Style.RESET_ALL}",
        f"{Fore.YELLOW}Chutes no Alvo{Style.RESET_ALL}",
        f"{Fore.YELLOW}Chutes/90{Style.RESET_ALL}",
        f"{Fore.YELLOW}Chutes a Gol/90{Style.RESET_ALL}",
        f"{Fore.YELLOW}Dist. Média (m){Style.RESET_ALL}"
    ]
    for i, player in enumerate(players):
        # Alternando cores para as linhas da tabela
        row_color = Fore.WHITE if i % 2 == 0 else Fore.LIGHTBLACK_EX
        row = [
            f"{row_color}{player.get('player', 'Desconhecido')}{Style.RESET_ALL}",
            f"{row_color}{player.get('shots', 'N/A')}{Style.RESET_ALL}",
            f"{row_color}{player.get('shots_on_target', 'N/A')}{Style.RESET_ALL}",
            f"{row_color}{player.get('shots_per90', 'N/A')}{Style.RESET_ALL}",
            f"{row_color}{player.get('shots_on_target_per90', 'N/A')}{Style.RESET_ALL}",
            f"{row_color}{player.get('average_shot_distance', 'N/A').replace(',', '.')}{Style.RESET_ALL}"
        ]
        table.append(row)
    return tabulate(table, headers=headers, tablefmt="grid")

# Função principal para exibir estatísticas de acordo com a liga e as equipes selecionadas
def display_statistics():
    # Lista de competições disponíveis (baseado nos nomes dos arquivos JSON)
    competitions = [
        "Champions_League_shooting_stats.json",
        "Europa_League_shooting_stats.json",
        "Premier_League_shooting_stats.json",
        "La_Liga_shooting_stats.json",
        "Serie_A_shooting_stats.json",
        "Bundesliga_shooting_stats.json",
        "Ligue_1_shooting_stats.json"
    ]

    # Solicitar ao usuário que escolha uma liga
    print("Escolha uma liga:")
    for i, competition in enumerate(competitions, 1):
        print(f"{i}. {competition.replace('_shooting_stats.json', '').replace('_', ' ')}")
    
    choice = int(input("Digite o número da liga: "))
    if 1 <= choice <= len(competitions):
        selected_competition = competitions[choice - 1]
        data = load_data_from_json(selected_competition)
        
        if data is not None:
            # Obter todas as equipes únicas presentes nos dados e ordená-las alfabeticamente
            teams = sorted(set(player['team'] for player in data if 'team' in player))
            
            # Solicitar ao usuário que escolha duas equipes
            print("\nEscolha as equipes que vão se enfrentar:")
            for i, team in enumerate(teams, 1):
                print(f"{i}. {team}")
            
            team1_choice = int(input("\nDigite o número da primeira equipe: "))
            team2_choice = int(input("Digite o número da segunda equipe: "))
            
            if 1 <= team1_choice <= len(teams) and 1 <= team2_choice <= len(teams):
                team1 = teams[team1_choice - 1]
                team2 = teams[team2_choice - 1]
                
                # Exibir os melhores jogadores de cada equipe (ordenados por chutes)
                print(f"\n{Fore.GREEN}Melhores jogadores da equipe {team1} (ordenados por chutes):{Style.RESET_ALL}")
                top_players_team1 = get_top_players_by_team(data, team1, metric='shots')
                print(format_player_stats_table(top_players_team1))

                print(f"\n{Fore.BLUE}Melhores jogadores da equipe {team2} (ordenados por chutes):{Style.RESET_ALL}")
                top_players_team2 = get_top_players_by_team(data, team2, metric='shots')
                print(format_player_stats_table(top_players_team2))
            else:
                print(f"{Fore.RED}Escolha inválida para as equipes.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Escolha inválida para a liga.{Style.RESET_ALL}")

# Função principal
if __name__ == "__main__":
    display_statistics()