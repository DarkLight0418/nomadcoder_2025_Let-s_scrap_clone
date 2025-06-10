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

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

class GuardDog(Dog):
        
    def rrrrr(self):
        print("stay away!!")
class Puppy(Dog):
    
    def woof_woof(self):
        print("Woof Woof!")

if __name__ == "__main__":
    print("")