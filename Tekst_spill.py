import time
import random

a = 0
player_health = random.randint(1, 10)
player_damage = random.randint(1, 10)

monster_health = random.randint(1, 10)
monster_damage = random.randint(1, 10)
monster_counter = 0

fBoss_health = random.randint(20, 30)
fBoss_damage = random.randint(20, 30)
def boss():
    global fBoss_health
    global fBoss_damage
    print ("Du har drept 10 monsteret og kommet til første boss")
    print ("Bossen har mye mer liv og skade enn et vanlig monster")
    print ("Boss liv:", fBoss_health)
    print ("Boss skade:", fBoss_damage)
    print ("")

    print ("Vil du slåss eller prøve å rømme.")
    boss_fight = input("Skriv ja eller nei: ")
    boss_fight = boss_fight.lower()
    if boss_fight == "ja":
        print ("Monsteret rager og angriper deg først")
        print ("Han gjør", fBoss_damage, "skade")
        player_health = player_health - fBoss_damage
        if player_health <= 0:
            print ("Du har gått under 0 liv")
            print ("Skriv 1 for å gjøre en saving throw for en sjanse i å overleve på et liv.")
            bSavingThrowValg = input("Skriv 0 for å gi opp og dø: ")
            if bSavingThrowValg == "1":
                bSavingThrow = random.randint(0, 2)
                if bSavingThrow == 0:
                    print ("Du overlevde og har 1 liv")
                else:
                    print ("Du failet og døde")
                
def shop():
    print ("du kan velge en av disse to gjenstandene til å hjelpe deg")
    print ("1. helse styrkende medaljong")
    print ("2. skade styrkende medaljong")
    global player_health
    global player_damage
    item = input("Skriv 1 eller 2 for å velge: ")
    if item == "1":
        player_health = player_health + 5
    elif item == "2":
        player_damage = player_damage + 5


print ("I dette spillet, kjemper du mot monsteret fram til du dør")
shop()
print ("Du får random  hver gang du spiller + gjenstanden du valgte")
time.sleep(3)

while a == 0:
    print ("")
    print ("Du har", player_health, "liv og", player_damage, "skade")
    print ("Monsteret har", monster_health, "liv og", monster_damage, "skade")

    angrep = input("Vil du angripe først? ")
    if angrep == "ja":
        monster_health = monster_health - player_damage
        print ("Du gjør", player_damage, "skade, og monsteret har", monster_health, "liv igjen")
        if  monster_health <= 0:
            print ("Monsteret døde")
            if monster_counter >= 5:
                monster_health = random.randint(5, 20)
                monster_damage = random.randint(5, 20)
            elif monster_counter <= 5:
                monster_health = random.randint(1, 10)
                monster_damage = random.randint(1, 10)
            monster_counter = monster_counter +1
            if monster_counter == 5:
                print ("Du har drept 5 monsteret nå!")
                print ("Det betyr at du kan oppgradere en av attributtene dine og få +2")
                print ("Skriv 1 for å oppgradere helse")
                oppgradering = input("Skriv 2 for å oppgradere skade: ")
                if oppgradering == "1":
                    player_health = player_health + 2
                elif oppgradering == "2":
                    player_damage = player_damage + 2

        elif monster_health >= 0:
            player_health = player_health - monster_damage
            print ("")
            print ("Monsteret angriper deg og gjør", monster_damage, "skade og du har", player_health, "liv igjen")
    elif angrep == "nei":
        player_health = player_health - monster_damage
        print ("Monsteret gjør", monster_damage, "skade, og du har ", player_health, "liv igjen")
        if player_health <= 0:
            print ("Du døde")
            a = 1
        elif player_health >= 0:
            print ("")