class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team
        
    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
        
    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

    def show_players(self):
        for player in self.players:
            player.introduce()
            
    def delete_player(self, name):
        for player in self.players:
            if player.name == name:
                self.players.remove(player)
                print(f"Deleted {name}({self.team_name})")
            return
        print("Player not found")
            
            
team_x = Team("Team X")
team_blue = Team("Team Blue")

team_x.add_player("Nico")
team_blue.add_player("Juan")

team_blue.show_players()

team_blue.delete_player("Juan")

team_blue.show_players()