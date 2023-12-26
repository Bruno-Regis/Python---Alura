import random #importing random function to generate random number.
def play(): #Defining a function called play to execute the game
    print(26*"~")
    print("Welcome to the guess game!")
    print(26*"~")
#Defining initial variables
    secret_number = random.randrange(1,101)
    count = 0
    score = 1000

#Choosing difficulty game level
    print("Choose difficulty level: ")
    level = int(input("1 - Easy\n2 - medium\n3 - hard\n"))
    if level == 1:
        count = 20
    elif level == 2:
        count = 10
    elif level == 3:
        count = 5

#Loop for each try including countings
    for round in range(1,count + 1):
        print(f"Attempt {round}/{count}")
        guess = int(input("try to guess a  number between 1 and 100: "))
        print("Your number is: ", guess)

#If user try a invalid number send a message and losses a try
        if (guess < 1) or (guess > 100):
            print("You should try a number between 1 and 100")
            continue

#Defining if guess number is corret, bigger or smaller then the secret number
        correct = guess == secret_number
        bigger  = guess > secret_number
        smaller = guess < secret_number

#Conditionals, if guess is correct, send a congratz, if it is bigger or smaller send a message too
        if (correct):
            print(f"Congratulations, you guess the right number!!\nYour score is: {score}")
            break
        else:
            if (bigger):
                print("You messed up, your try is bigger than the secret number.")
            elif (smaller):
                print("You messed up, your try is smaller than the secret number.")
#If number enter on else conditional, the score is recalculate
        losses_score = abs(secret_number-guess) #Calling built-in python function to set a absolute number
        score = score-losses_score #Score recalc
    print("The end.")

if (__name__ == "__main__"): #If it is in the main archive, execute the function play.
    play()