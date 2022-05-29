import random
import time

# Ship Project, kind of Battlefield style

# Status, Types, & Properties of Ships
status = ['alive', 'damaged','destroyed']
ships = ['Dreadnought', 'Cruiser', 'Fighter']
properties = [
    {'ship':'Dreadnought','cost': 5, 'combat value': 5, 'ship status':status[0]},
    {'ship':'Cruiser','cost': 2, 'combat value': 7, 'ship status':status[0]},
    {'ship':'Fighter','cost': 1, 'combat value': 9, 'ship status':status[0]}]

# Fleet Setup
def set_up ():
    # Cost is the money you have spent on ships, your fleet is initialized as empty
    cost = 0
    fleet_list = []
    fleet = {}
    
    # You get to buy ships one by one without going over the resource limmit of 30
    for x in range(len(ships)):
        ship_number = int(input("How many {} do you want to buy? \nThey cost {} & you are at {} resources spent.\nRemember, the resource cap is 30 so spend them wisely."
                                .format(ships[x],properties[x]["cost"],cost)))
        cost += ship_number*properties[x]['cost']
        for i in range(ship_number):
            fleet_list.append(ships[x])
            fleet['{}{}'.format(ships[x],i)] = properties[x]
        if cost >30:
            print("You can't go over 30 Resources... Try again? ")
            time.sleep(5)
            exit()
 
    time.sleep(2)
    print(*fleet_list)
    return fleet

# Getting your ships ready to attack
def hits(fleet):
    hits =0
    for x in fleet:
        if random.randint(1,10) >= fleet[x]['combat value']:
            print('{} is ready to attack'.format(x))
            time.sleep(1)
            hits+=1

    print("{} ship(s) are ready to attack \n".format(hits))
    time.sleep(1)
    return hits

# Formatting the status of your ship depending on which one was hit and if it was damaged or destroyed
def hits_taken(fleet, hits):
    fleet_list =[]
    for n in fleet:
        fleet_list.append(n)
    print(*fleet_list)

    for v in range(hits):
        Number = random.randint(0,len(fleet_list)-1)
        fleet_list[Number]

        if fleet[fleet_list[Number]]["ship"] == "Dreadnought":
            if fleet[fleet_list[Number]]["ship status"]== status[1]:
                fleet[fleet_list[Number]]["ship status"]= status[2]
                print('{} has been destroyed.'.format(fleet_list[Number]))
                fleet.pop(fleet_list[Number])
                fleet_list.pop(Number)
                time.sleep(1)
                continue
            else:
                fleet[fleet_list[Number]]["ship status"]= status[1]
                print("{} has been damaged ".format(fleet_list[Number]))
                time.sleep(1)
                continue
        else:
            print('{} has been destroyed.'.format(fleet_list[Number]))
            fleet.pop(fleet_list[Number])
            fleet_list.pop(Number)
            time.sleep(1)     
    return fleet

# Win condition where your fleet (fleet1) is still not 0 or if the enemy fleet (fleet2) is 0
def win_condition(fleet1, fleet2):
    winner = "Player"
    if len(fleet2) == 0:        
        print("Your ships won, congrats! I'm proud of you!")
        return True
    if len(fleet1) == 0:
        print("Your ships lost... It wasn't your fault champ, keep your chin up & maybe try again if you want. :)")
        return True
    else:
        return False

winner = False
player_fleet = set_up()
computer_fleet = player_fleet

# Setting up the rounds on the terminal
round_number = 1
while winner == False:
    
    print("---------- Round: "+str(round_number)+" ----------\n")
    time.sleep(1)
    print("Gathering the Fleet!!!")
    print("Player's fleet: ")
    time.sleep(1)
    player_hits = hits(player_fleet)
    print("Computer's fleet: ")
    computer_hits = hits(computer_fleet)
    print("Combat Systems Online!!!")
    time.sleep(1)
    print("\nPlayer's Damage Report: ")
    player_fleet = hits_taken(player_fleet, computer_hits)
    print("Player's Remaining Ships: ", *player_fleet)
    time.sleep(3)
    print('\nComputer Damage Report: ')
    computer_fleet = hits_taken(computer_fleet, player_hits)
    print("Computer's Remaining Fleet:", *computer_fleet)
    time.sleep(3)
    round_number +=1
    winner = win_condition(player_fleet,computer_fleet)
    
    # Doesn't take into account inputs of letters when expecting numbers