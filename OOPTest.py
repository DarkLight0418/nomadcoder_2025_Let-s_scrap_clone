# 리펙토링 전(클래스 사용 전)

'''
nico = {
    "name" : "Nico",
    "XP" : 1000,
    "team" : "Team X"
}

def create_player(name, xp, team):
    return {
    "name" : name,
    "XP" : xp,
    "team" : team
}

def introduct_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}.")
    

introduct_player(nico)

nico = create_player("Nico", 1500, "Team X")
'''
# class review

class Puppy:
    def __init__(self):  # self == 그들 자신 참조
        self.name = "Ruffus"
        self.age = 0.1
        self.breed = "Beagle"
        
ruffus = Puppy() # ruffus == self

print(
    ruffus.name,
    ruffus.age,
    ruffus.breed
)