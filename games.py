import hangman #Importing hangman game
import guess #Importing guess game
def choose_game(): #Defining a function wich choose the game called choose_game
    print("\033[1;31;47m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m")
    print("\033[1;31;47m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m")
    print('\033[1;30;47m Welcome!!!Which game would you like to play today?\033[m')
    print("\033[1;31;47m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m")
    print("\033[1;31;47m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[m")

    game = int(input("(1) - Hangman\n(2) - Guess Game\n")) #Choosing the game
    if game == 1:
        hangman.play()
    elif game == 2:
        guess.play()

if (__name__ == "__main__"): #If it is in the main archive, execute the function choose_game.
    choose_game()
