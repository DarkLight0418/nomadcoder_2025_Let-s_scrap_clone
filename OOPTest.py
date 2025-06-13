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
        
    def sleep(self):
        print("zzzzzzz.......")
    
    def yummy(self):
        print("yumyumyummm.... it's delicious")


class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 5)
        
    def rrrrr(self):
        print("stay away!!")
        
class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__( # super() 부모 클래스 참조
            name, 
            breed, 
            0.1,
    )
        self.spoiled = True
    
    def woof_woof(self):
        print("Woof Woof!")

if __name__ == "__main__":
    print("")
    
    ruffus = Puppy(
        name="Ruffus",
        breed="Beagle",
    )
    
    bibi = GuardDog(
        name="Bibi",
        breed="Dalmatian",
    )
    
    ruffus.woof_woof()
    
    bibi.sleep()