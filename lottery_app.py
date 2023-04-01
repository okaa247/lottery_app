import random


winning_number = 30
username = input("Enter your name to play: ")
print("Hello", username, "welcome to cohort 1 lucky lottery")

def lottery_app():
    while 1:
        usernumber = int(input("enter any number from 0 to 50: "))
        random_number = random.randint(0, 50)
        if usernumber > 50:
            print("Your input number is more than 50, sorry you are disqualified, try again later.")
            exit() 
        elif usernumber == winning_number == random_number:
            print("congratulations!", username, "you won")
        else:
            print("sorry", username, "you lost, you can try again")

lottery_app()        
        
