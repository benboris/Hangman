
'''
 using a python 3.7 in this Game 

'''

import urllib.request  
# print txt from url
import random  
# for random word in def word_Game to person


def print_hangman():  
# print from url need import urllib.request
    url = 'http://e-learn.cyber.org.il/python/rolling_assignment/resources/hangman_welcome_screen.txt'
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    print(text)
    print("")
    print(
        "Welcome to Hangman! A word will be chosen at random and you must try to guess the word correctly letter by letter before you run out of attempts. Good luck! "
    )


def word_Game():
    file_path = [
        "hangman", "chairs", "backpack", "bodywash", "clothing", "computer",
        "python", "program", "glasses", "sweatshirt", "sweatpants", "mattress",
        "friends", "clocks", "biology", "algebra", "suitcase", "knives",
        "ninjas", "shampoo"
    ]

    index = choose_word(file_path, len(file_path))
    return index


def main():

    MAX_TRIES = 7
    End_Game = 0
    print_hangman()  
    # print txt from url
    secret_word = word_Game()  
    # secret word is random word from  my arr words
    length_word = len(secret_word)  
    #length in word
    
    print(
        "You need to guess a %s-letter word. You have 7 attempts If you're wrong"
        % (length_word))
    person_arr = []
    error_person_str = ""

    for _ in range(0, length_word):
        person_arr.append("__")

    Beautiful_printing(person_arr)
    letter_guessed = input('Guess a letter:')
    person = check_valid_input(letter_guessed, error_person_str)

    def show_hidden_word(secret_word, old_letters_guessed):
        for i in range(0, length_word):
            if secret_word[i] == person:
                old_letters_guessed[i] = person
            else:
                continue
        return old_letters_guessed

    while (MAX_TRIES != 0):

        if (not (person in secret_word)):
            error_person_str = error_person_str + person
            MAX_TRIES = MAX_TRIES - 1
            End_Game = End_Game + 1
            print(":(")
            if End_Game == 1:
                HANGMAN_PHOTOS_1()
            elif End_Game == 2:
                HANGMAN_PHOTOS_2()
            elif End_Game == 3:
                HANGMAN_PHOTOS_3()
            elif End_Game == 4:
                HANGMAN_PHOTOS_4()
            elif End_Game == 5:
                HANGMAN_PHOTOS_5()
            elif End_Game == 6:
                HANGMAN_PHOTOS_6()
            elif End_Game == 7:
                HANGMAN_PHOTOS_7(secret_word)
                break
            else:
                print("End Game")
        else:
            person_arr = show_hidden_word(secret_word, person_arr)
            error_person_str = error_person_str + person

        string_arr = ''.join(person_arr)
        CK = check_win(secret_word, string_arr)

        if (CK == True):
            print("Well done, you won !")
            Beautiful_printing(person_arr)
            break

        Beautiful_printing(person_arr)
        letter_guessed = input('Guess a letter:')
        person = check_valid_input(letter_guessed, error_person_str)


def choose_word(file_path, index):
    random_choice = random.choice(file_path)
    for i in range(0, index):
        if file_path[i] == random_choice:
            j = i
    print(
        "There are %s words in the file and the selected word is in the index %s"
        % (index, j))
    return random_choice


def check_valid_input(letter_guessed, old_letters_guessed):
    while (True):
        if not (letter_guessed in old_letters_guessed):
            return letter_guessed
        else:
            letter_guessed = try_update_letter_guessed(letter_guessed,
                                                       old_letters_guessed)


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    print("X")
    print(old_letters_guessed)
    letter_guessed = input('Guess a letter:')
    return letter_guessed


def check_win(secret_word, old_letters_guessed):
    if (secret_word == old_letters_guessed):
        return True
    else:
        return False


def Beautiful_printing(person_arr):
    x = str(person_arr)
    x = x.replace("[", "")
    x = x.replace("]", "")
    x = x.replace(",", " ")
    x = x.replace("'", "")
    print(x)
    print(" ")


def HANGMAN_PHOTOS_1():
    print("x-------x")
    print("")


def HANGMAN_PHOTOS_2():
    print("x-------x")
    print("|        ")
    print("|        ")
    print("|        ")
    print("|        ")
    print("|        ")
    print("")


def HANGMAN_PHOTOS_3():
    print("x-------x")
    print("|       |")
    print("|       0")
    print("|        ")
    print("|        ")
    print("|        ")
    print("")


def HANGMAN_PHOTOS_4():
    print("x-------x")
    print("|       |")
    print("|       0")
    print("|       |")
    print("|        ")
    print("|        ")
    print("")


def HANGMAN_PHOTOS_5():
    print(" x-------x   ")
    print(" |       |   ")
    print(" |       0   ")
    print(" |      /|\  ")
    print(" |           ")
    print(" |           ")
    print("")


def HANGMAN_PHOTOS_6():
    print("x-------x  ")
    print("|       |  ")
    print("|       0  ")
    print("|      /|\ ")
    print("|      /   ")
    print("|          ")
    print("")


def HANGMAN_PHOTOS_7(secret_word):
    print("x-------x  ")
    print("|       |  ")
    print("|       0  ")
    print("|      /|\ ")
    print("|      / \ ")
    print("|          ")
    print("You LOSE The Word Was : %s " % (secret_word))
    print("")


if __name__ == "__main__":
    main()
