from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Levi_Cheater
from cheatdice import Levi_Cheater_2

cheater1 = Levi_Cheater_2()#Cheat_Swapper()
cheater2 = Levi_Cheater() #Cheat_Loaded_Dice()

cheater1.roll()
cheater2.roll()

cheater1.cheat()
cheater2.cheat()

print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))

if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
  print("Draw!")

elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
  print("Cheater 1 wins!")

else:
  print("Cheater 2 wins!")

