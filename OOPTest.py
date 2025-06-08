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
    def __init__(self, name, breed):  # self == 그들 자신 참조
        self.name = name
        self.age = 0.1
        self.breed = breed
    def __str__(self):  # __자동 호출 메서드__
        return f"{self.breed} puppy named {self.name}"
        
ruffus = Puppy(
    name="ruffus",
    breed="Beagle") # ruffus == self
bibi = Puppy("bibi", "Dalmatian")

print(bibi, ruffus)
