
"""
Created on Wed Feb 14 13:06:14 2018

@author: Austin Gill
"""


roomtype = [0,1,2,3]
#room 0 is normal (tan)
#room 1 is flooded (cooldown+1)(blue)
#room 2 is windy (cooldown-1)(red)
#room 3 is dark (don't see stats of enemy, randomly increase or decrease cooldown)(purple)

floor = 1

#floor will increase after defeating floor boss

level = 1

#level of character, when they level up, they get to increase 2 stats

exp = 0
expneed = 10

#experience needed to level up doubles each level

ranger = [10,5,2,7,5,3,5,3]
knight = [20,3,8,3,3,3,5,3]
wizard = [10,20,2,4,4,7,5,3]
theif = [10,6,2,5,5,4,6,3]
classtype = [ranger, knight, wizard, theif]

#Character classes will be ranger (0), knight (1), wizard (2), and theif (3) at first
#stats are going to be HP, MP, strength, speed, dexterity, intelligence, critcal, and luck
#Array contains stats in order of HMSSDICL (order listed above)

temp1 = input('Choose your character class: ranger(1), knight(2), wizard(3), or theif(3):')

switch ()















