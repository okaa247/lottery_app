import random

# value = random.uniform(2, 3)
# print(value)


def lottery_app():
    while 1:
        username = input("Enter your username to play: ")
        usernumber = int(input("enter any number from 0 to 50: "))
        numbers = random.randint(0, 50)
        if numbers == 30:
            print("congratulations!", username, "you won")
        else:
            print("sorry", username, "you lost, you can try again")

lottery_app()        
