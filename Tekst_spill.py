import random
import time
a = 0


player_health = random.randint(1, 10)
player_damage = random.randint(1, 10)

monster_health = random.randint(1, 10)
monster_damage = random.randint(1, 10)

print ("Du får random stats hver gang du spiller")
time.sleep(3)

while a == 0:
    print ("")
    print ("Du har", player_health, "liv og", player_damage, "damage")
    print ("Monsteret har", monster_health, "liv og", monster_damage, "damage")

    angrep = input("Hvil du angripe først?")
    if angrep == "ja":
        monster_health = monster_health - player_damage
        print ("Du gjør", player_damage, "skade, og monsteret har", monster_health, "liv igjen")
        if  monster_health <= 0:
            print ("Monsteret døde")
            a = 1
        elif monster_health >= 0:
            print ("")
    elif angrep == "nei":
        player_health = player_health - monster_damage
        print ("Monsteret gjør", monster_damage, "skade, og du har ", player_health, "liv igjen")
        if player_health <= 0:
            print ("Du døde")
            a = 1
        elif player_health >= 0:
            print ("")
            
            
        