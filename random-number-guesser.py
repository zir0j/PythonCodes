import random as r


# Generates Random number 
def random_number_guesser():
    try:
        user_input = int(input("Insert a number between 1 and 10! Remember, it has to be a WHOLE number: "))
        if 1 <= user_input <= 10:               # Validates if input is more than 11
            random = r.randrange(1, 10)         # Generates number from 1 to 10
            if random == user_input:
                print(f"Your number is {user_input} and mine is {random}. It's a tie")
            elif random > user_input:
                print(f"Your number is {user_input} and mine is {random}. I won!")
            else:
                print(f"Your number is {user_input} and mine is {random}. I lost!")
        else:
            print("More than 10. Clear the terminal and try again.")
    except:
        print("Not an integer. Clear the terminal and try again!")     # Validates if input is not integer

random_number_guesser()
