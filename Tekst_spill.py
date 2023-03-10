import time
import random

a = 0
player_health = random.randint(1, 10)
player_damage = random.randint(1, 10)

monster_health = random.randint(1, 10)
monster_damage = random.randint(1, 10)
monster_counter = 0

def shop():
    print("du kan velge en av disse to gjenstandene til å hjelpe deg")
    print("1. helse styrkende medaljong")
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


