import time
import random

luke = {'name': "Luke Skywalker", 'power': 100, 'health': 300}
obiwan = {'name': "Obiwan Kenobi", 'power': 150, 'health': 325}
monster = {'power': 75, 'health': 450}

player = luke

finish = False


print("A battle begins! "+player['name']+" against Monster")

while finish == False:

    time.sleep(3)
    
    shield = 0
    print("\n(1) Attack")
    print("(2) Defense")
    playermove = input("Choose one number for movement (1 or 2): ")

    if (playermove == "1"):

        print(player['name'] + " will attack Monster")
        
        dmg2monster = random.uniform(0.5*player['power'], player['power'])

        ##Create bonus damage by calculating weak point:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print("\nCalculate weak point for bonus damage:")

        time1 = time.time()
        answer = input(str(num1) + " + " + str(num2) + "= ")
        waittime = time.time() - time1

        if (waittime < 3) and (num1 + num2 == int(answer)):
            dmg2monster = 1.5*dmg2monster
            print("Monster will get bonus damage!")
        else:
            print("Monster will get normal damage..")

    else:

        print(player['name'] + " will be defensive")
        shield = 1

    time.sleep(2)
    
    monstershield = 0
    monstermove = random.randint(1, 2)
    if monstermove == 1:
        print("\nMonster will attack " + player['name'])
        dmg2player = random.uniform(0.5*monster['power'], monster['power'])
    else:
        print("\nMonster will be defensive")
        monstershield = 1

    time.sleep(2)

    #RESULT:
    if (playermove == "1"):
        monster['health'] = monster['health'] - dmg2monster*(1-0.5*monstershield)
        print("Monster is damaged by " + str(dmg2monster*(1-0.5*monstershield)))

        time.sleep(2)
        
        if monster['health'] < 0:
            print("Player Wins")
            finish = True
            break
    
    if (monstermove == 1):
        player['health'] = player['health'] - dmg2player*(1-0.5*shield)
        print("Player is damaged by " + str(dmg2player*(1-0.5*shield)))

        time.sleep(2)

        if player['health'] < 0:
            print("Player Defeated")
            finish = True
            break
        
    print("\nResult: ")
    
    print(player['name'])
    print("Health Point: " + str(player['health']))
    print("\nMonster")
    print("Health Point: " + str(monster['health']))

    time.sleep(2)
