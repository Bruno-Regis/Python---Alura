import random
def play():
    print_welcome()
    secret_word = load_word()

    word_letters = ["_" for l in secret_word] #List comprehension -> loop to increase '_' for each letter (l) in secret_word

    guessed = False
    died = False
    misses: int = 0
    while (not died and not guessed ):

        guess = input("Try to guess a letter:\n").strip().upper()

        if (guess in secret_word):
            input_discovered_letters(secret_word,guess,word_letters)
        else:
            misses += 1
            draw_hangman(misses)

        died = misses == 7
        guessed = '_' not in word_letters
        print(word_letters)

    if   (guessed):
        win_message()
    elif (died):
        loser_message(secret_word)

    print("\nThe end.")
#####Game Functions#####
#Docstrings immediately after functions headers
def print_welcome():
    """Function that calls welcome message"""
    print(26 * "~")
    print("Welcome to the Hangman game!")
    print(26 * "~")

def load_word():
    """Function that returns random word from .txt"""
    file = open("words.txt", "r")
    words = []
    for line in file:
        line = line.strip()
        words.append(line)
    file.close()
    num = random.randrange(0, len(words))
    secret_word = words[num].upper()
    return secret_word

def input_discovered_letters(secret_word,guess,word_letters):
    """Function that substitue "_" by a guessed word,"""
    n = 0
    for letter in secret_word: #loop that recognize right words in secret_word, then input these letters in word_letters[] to show the user guessed words
        if (letter == guess):
            word_letters[n] = letter
        n += 1

def win_message():
    """Function that calls winners message"""
    print("Congratulations, you save him from the hangman!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def loser_message(secret_word):
    """Function that calls losers message"""
    print("Oh dear, your effort wasn't enough to save him!!")
    print(f"The Answer was {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def draw_hangman(misses):
    print("  _______     ")
    print(" |/      |    ")

    if(misses == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(misses == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(misses == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(misses == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(misses == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(misses == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (misses== 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
if (__name__ == "__main__"):
    play()