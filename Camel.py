import random
miles_traveled = 0 
thirst = 0
camel_tiredness = 0 
native_distance = -20
drinks_in_canteen = 3
done = False
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")
while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print("")
    user_input = input("What will you do next?")
    if user_input.upper() == "Q" or user_input.upper() == "QUIT.":
        done = True
    elif user_input.upper() == "E" or user_input.upper() == "STATUS CHECK.":
        print("Miles traveled: " + str(miles_traveled))
        print("Drinks in canteen " + str(drinks_in_canteen))
        print("The natives are " + str(native_distance) + " miles behind you.")
    elif user_input.upper() == "D" or user_input.upper() == "STOP FOR THE NIGHT.":
        camel_tiredness = 0
        native_distance += random.randint(7, 14)
        print("The camel is happy!")
    elif user_input.upper() == "C" or user_input.upper() == "AHEAD FULL SPEED.":
        distance = random.randint(10, 20)
        miles_traveled += distance
        native_distance += random.randint(7, 14)
        thirst += 1
        camel_tiredness += random.randint(1, 3)
        print("You've traveled " + str(distance) + " miles and a total of " + 
              str(miles_traveled) + " miles overall.")
    elif user_input.upper() == "B" or user_input.upper() == "AHEAD MODERATE SPEED.":
        distance = random.randint(5, 12)
        miles_traveled += distance
        native_distance += random.randint(7, 14)
        thirst += 1
        camel_tiredness += 1
        print("You've traveled " + str(distance) + " miles and a total of " + 
              str(miles_traveled) + " miles overall.")
    elif user_input.upper() == "A" or user_input.upper() == "DRINK FROM YOUR CANTEEN.":
        if drinks_in_canteen:
            drinks_in_canteen -= 1
            thirst = 0
            print("You quenched your thirst and have " + 
                  str(drinks_in_canteen) + " drinks in your canteen left.")
        else:
            print("You have nothing in your canteen to drink!")
    else:
        print("Stop messing about! The Natives are getting closer and closer!")
    if thirst > 6:
        done = True
        print("You died of thirst!")
        break
    elif thirst > 4:
        print("You are thirsty.")
    if camel_tiredness > 8:
        done = True
        print("Your camel is dead.")   
        break
    elif camel_tiredness > 5:
        print("Your camel is getting tired.")
    if native_distance >= miles_traveled:
        done = True
        print("The natives have caught up to you, sorry! Game over!")
        break
    elif native_distance > miles_traveled - 15:
        print("The natives are getting close!")
    if miles_traveled >= 200:
        done = True
        print("You managed to escape the natives! Congrats you've won!")
        break
    if random.randint(1,20) == 2:
        print("You found an oasis! You filled your canteen," + 
              "quenched your thirst, rested your camel and the natives haven't made any progress.")
        drinks_in_canteen = 3
        thirst = 0
        camel_tiredness = 0