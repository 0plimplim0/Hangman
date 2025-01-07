import random
import os 
import time

def choose_word(list1):
    return random.choice(list1)

def clear_console():
    os.system("clear")

def display_hangman(tries):
    stages = [
        """
           |-----------|
           |          ( )
           |          /|\\ 
           |          / \\ 
         -----
        """,
        """
           |-----------|
           |          ( )
           |          /|\\ 
           |          /  
         -----
        """,
        """
           |-----------|
           |          ( )
           |          /|\\ 
           |           
         -----
        """,
        """
           |-----------|
           |          ( )
           |          /| 
           |           
         -----
        """,
        """
           |-----------|
           |          ( )
           |           | 
           |           
         -----
        """,
        """
           |-----------|
           |          ( )
           |           
           |           
         -----
        """,
        """
           |-----------|
           |          
           |           
           |           
         -----
        """
    ]
    print(stages[tries])

def hangman():
    usr_list = ""
    
    while usr_list == "":
        selected_list = input("Which category do you want to play with? ")
        if selected_list == "animals":
            usr_list = lists[2]
        elif selected_list == "fruits":
            usr_list = lists[1]
        elif selected_list == "colors":
            usr_list = lists[0]
        else: print("Please enter a valid category.")
        
    word = list(choose_word(usr_list))
    word2 = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6

    print("The game starts in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    os.system("clear")
    while not guessed and tries > 0:
        print(f"Word: {word2}")
        display_hangman(tries)
        usr_guess = input("Guess a letter: ").lower()
        if len(usr_guess) == 1 and usr_guess.isalpha():
            if usr_guess in guessed_letters: 
                print("You already guess this letter")
            elif not usr_guess in word:
                print(f"Wrong! {usr_guess} is not in the word")
                guessed_letters.append(usr_guess)
                tries -= 1
            else:
                print(f"Correct! {usr_guess} is in the word")
                guessed_letters.append(usr_guess)
                word3 = list(word2)
                indices = [i for i, letter in enumerate(word) if letter == usr_guess]
                for index in indices:
                    word3[index] = usr_guess
                word2 = "".join(word3)
                if "_" not in word2:
                    guessed = True

        else: print("Enter a valid letter")

        time.sleep(1)
        clear_console()

        word = "".join(word)
    if guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        display_hangman(tries)
        print(f"Sorry, you lost. The word was: {word}")

lists = [["rojo", "azul", "verde", "amarillo", "naranja", "rosa", "morado"], 
["manzana", "platano", "naranja", "uva", "fresa", "pera", "pina"], 
["perro", "gato", "pez", "tigre", "leon", "tiburon", "loro", "elefante", "jirafa", "zorro", "oso", "conejo", "serpiente", "aguila", "delfin", "camaleon", "canguro", "rinoceronte", "buho"
] ]

while True:
    clear_console()
    print("Hangman")

    usr_input = input("Type 'play' or 'exit': ")

    if usr_input == "play":
        while True:
            hangman()
            x = input("Do you want to play again?(Y or N) ").upper()
            if x == "N":
                break
    elif usr_input == "exit":
        print("Goodbye!")
        break
    else: print("Invalid command")
