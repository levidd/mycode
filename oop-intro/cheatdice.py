from random import randint
from random import choice
from player import Player

class Cheat_Swapper(Player):
  def cheat(self):
    self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
  def cheat(self):
    i = 0
    while i < len(self.dice):
      if self.dice[i] < 6:
        self.dice[i] += 1
      i += 1

class Levi_Cheater(Player):
    def cheat(self):
        for i in range(len(self.dice)):
            self.dice[i] = choice(self.dice)

class Levi_Cheater_2(Player):
    def cheat(self):
        for i in range(len(self.dice)):
            newDice = []
            for attempt in range(self.dice[i]):
                newDice.append(randint(1,6))
            self.dice[i] = max(newDice)
