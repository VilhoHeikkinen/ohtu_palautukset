class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = []
        for player in self.reader.get_players():
            if player.nationality == nationality:
                players_by_nationality.append(player)

        top_scorers = sorted(players_by_nationality, key=lambda player: player.points, reverse=True)
        result = []
        for player in top_scorers:
            result.append(player)
        return result