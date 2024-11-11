import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        if player_dict['nationality'] == "FIN":
            player = Player(player_dict)
            players.append(player)

    print("Players from FIN:\n")

    players_sorted_by_points = sorted(players, key=lambda player: player.points, reverse=True)
    for player in players_sorted_by_points:
        print(player)

if __name__ == "__main__":
    main()