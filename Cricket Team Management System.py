class Player:
    def __init__(self, player_name, jersey_number, runs):
        self.player_name = player_name
        self.jersey_number = jersey_number
        self.runs = runs

    def get_category(self):
        if self.runs >= 500:
            return "Excellent"
        elif self.runs >= 250:
            return "Good"
        else:
            return "Average"

    def display(self):
        print("Player Name:", self.player_name)
        print("Jersey Number:", self.jersey_number)
        print("Runs:", self.runs)
        print("Category:", self.get_category())
        print()


class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_players(self):
        print("Cricket Player Records")
        print("----------------------")
        for player in self.players:
            player.display()


team = Team()

team.add_player(Player("Virat Kohli", 18, 650))
team.add_player(Player("Rohit Sharma", 45, 420))
team.add_player(Player("Jasprit Bumrah", 93, 180))
team.add_player(Player("Shubman Gill", 77, 520))

team.display_players()