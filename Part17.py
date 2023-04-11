# Class or Static Variable

class Player:
    team_run = 0    # class / static variable
    def __init__(self, run):   #constructor
        self.run = run  # instance variable
        # self.team_run = 0


    def hit_four(self):     #instance method
        self.run += 4
        # self.team_run += 4
        Player.team_run += 4

    def hit_six(self):
        self.run += 6
        # self.team_run += 6
        Player.team_run += 6

print(Player.team_run)
sakib = Player(0)
tamim = Player(0)
print("Sakib : ", sakib.run)
print("Tamim : ", tamim.run)
tamim.hit_four()
tamim.hit_four()
sakib.hit_six()
print("Sakib : ", sakib.run)
print("Tamim : ", tamim.run)

print("Tamim :", tamim.__dict__)
print("Sakib :", sakib.__dict__)

#print("Team Run : ", tamim.team_run)

print("Team Run : ", Player.team_run)
