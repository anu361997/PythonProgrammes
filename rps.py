import random
import cv2

choice = ['Rock','Paper','Scissors']

flag = True

while (flag):
    bot_choice = choice[random.randint(0,2)]
    print("Enter Your Choice")
    user_input = input("Rock,Paper,Scissors?\n")
    print("Bot Choice: "+bot_choice)
    if(user_input == bot_choice):
        print("Tie!")
    elif(user_input == "Rock"):
        if(bot_choice == "Paper"):
            print("You lose")
        else:
            print("You win")
    elif(user_input == "Paper"):
        if(bot_choice == "Scissors"):
            print("You lose")
        else:
            print("You win")
    elif(user_input == "Scissors"):
        if(bot_choice == "Rock"):
            print("You Lose")
        else:
            print("You Win")
    else:
        print("Enter a valid choice")
        continue
    print("To exit press 1 otherwise press Enter")
    if(input() == '1'):
        flag = False
        continue
    else:
        continue 

