# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    ('''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    ''')

    is_word_guessed_bool = True

    for i in secret_word:
        if "_" not in get_guessed_word(secret_word, letters_guessed):
            is_word_guessed_bool = True
        else:
            is_word_guessed_bool = False




    return is_word_guessed_bool



def get_guessed_word(secret_word, letters_guessed):
    #v More spaghetti i might want to look at later v
    ('''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    )

    guessed_word = []
    for i in secret_word:
        if i in letters_guessed:
            guessed_word.append(i)
        else:
            guessed_word.append("_")

    guessed_word_as_string = " ".join(guessed_word)
    return guessed_word_as_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet_raw = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet_raw)



    for letters in letters_guessed:
        for index in alphabet:
            if letters.lower() == index.lower():
                alphabet.remove(index)

    # available_letters = ' '.join([str(item) for item in alphabet])
    available_letters = ' '.join([str(item) for item in alphabet])
    return available_letters



def hangman(secret_word):
    ('''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    ''')

    tries = 6
    warnings = 3
    is_word_guessed_bool = False
    secret_word_as_list = list(secret_word)
    letters_guessed_as_list = []
    current_guessed_word = []
    letters_guessed_as_string = "".join(letters_guessed_as_list)



    while not is_word_guessed_bool and tries > 0:


        
        print("You have ", tries, " tries remaining.")
        print("You have ", warnings, " warnings remaming.")
        print("Available letters: ", get_available_letters(letters_guessed_as_list))
        print("Current guessed word: ", get_guessed_word(secret_word, letters_guessed_as_list))
        #print("DELETE Secret word is: ", secret_word)




        letters_guessed = input('Please guess a letter (seperate letters with a space): ')
        letters_guessed_as_list.append(letters_guessed.lower())

        if len(letters_guessed) == 1 and letters_guessed.isalpha():
            if letters_guessed not in secret_word_as_list:
                print("----------------------------------")
                print(letters_guessed, ' is not in the word')
                tries-=1

            elif letters_guessed in secret_word:
                print("----------------------------------")
                print("Good job!", letters_guessed, " is a letter.")
                if is_word_guessed(secret_word, letters_guessed_as_list) == True:
                    print("----------------------------------")
                    is_word_guessed_bool = True
                    user_play = input("Congratulations, you guessed the word! Would you like to play again? (y/n): ")
                    if user_play.lower() == "y":
                        secret_word = choose_word(wordlist)
                        hangman(secret_word)
                    else:
                        print("----------------------------------")
                        print("Thank you for playing! The secret word was ", secret_word)
                else:
                    is_word_guessed_bool = False

            elif letters_guessed not in get_available_letters(letters_guessed_as_list):
                print(letters_guessed, " is not an available letter")
                if warnings > 0:
                    warnings -= 1
                    print("You lose a warning. You have ", warnings, " left.")
                elif warnings == 0:
                    tries -= 1
                    print("No more warnings, you lose a try. You have ", tries, " left.")
        else:
            if warnings > 0:
                print("----------------------------------")
                warnings = warnings - 1
                print("Please input letters only, you lose a warning.")
                print("Warnings left: ", warnings)

            elif warnings == 0:
                print("----------------------------------")
                tries = tries - 1
                print("You've run out of warnings, you lose a try...")
                print("Tries remaining: ", tries)

    if tries == 0:
        print("----------------------------------")
        user_play = input("You've run out of tries! Would you like to play again? (y/n): ")
        if user_play.lower() == "y":
            secret_word = choose_word(wordlist)
            hangman(secret_word)
        else:
            print("Thank you for playing! The secret word was ", secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_no_space = my_word.replace(" ","")
    length_of_word = len(my_word_no_space)
    letters = list(my_word_no_space)

    if len(other_word) == length_of_word:
        for i in range(length_of_word):
            if my_word_no_space[i] == other_word[i]:
                continue

            elif my_word_no_space[i] == "_" and other_word[i] not in letters:
                continue

            else:
                return False

        return True
    else:
        return False




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = ""

    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            possible_matches += (other_word + " ")

        else:
            continue
    if possible_matches == "":
        print("----------------------------------")
        print("No matches found.")
    else:
        print("----------------------------------")
        print("Loading possible matches...")
        print("Possible matches: ",possible_matches)



def hangman_with_hints(secret_word):
    ('''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    ''')

    tries = 6
    warnings = 3
    is_word_guessed_bool = False
    secret_word_as_list = list(secret_word)
    letters_guessed_as_list = []
    vowels = "aeiou"
    letters_guessed_as_string = "".join(letters_guessed_as_list)

    while not is_word_guessed_bool and tries > 0:

        print("Enter * for a hint.")
        print("You have ", tries, " tries remaining.")
        print("You have ", warnings, " warnings remaming.")
        print("Available letters: ", get_available_letters(letters_guessed_as_list))
        print("Current guessed word: ", get_guessed_word(secret_word, letters_guessed_as_list))
        #print("DELETE Secret word is: ", secret_word)

        letters_guessed = input('Please guess a letter: ')
        current_guessed_word = get_guessed_word(secret_word, letters_guessed_as_list).replace(" ","")
        letters_guessed_as_list.append(letters_guessed.lower())




        if len(letters_guessed) == 1 and letters_guessed.isalpha():
            if letters_guessed not in secret_word_as_list and letters_guessed != "*":
                if letters_guessed.lower() in vowels:

                    print("----------------------------------")
                    print(letters_guessed, ' is not in the word')
                    print("Incorrect guesses that are vowels cost two tries.")
                    tries -= 2
                    print("You have ", tries, " tries remaining.")

                elif letters_guessed.lower() not in vowels:
                    print("----------------------------------")
                    print(letters_guessed, ' is not in the word')
                    tries-=1
                    print("You have ", tries, " tries remaining.")

            elif letters_guessed in secret_word:
                print("----------------------------------")
                print("Good job!", letters_guessed, " is a letter.")
                if is_word_guessed(secret_word, letters_guessed_as_list) == True:
                    print("----------------------------------")
                    print(get_guessed_word(secret_word, letters_guessed_as_list))
                    is_word_guessed_bool = True
                    user_play = input("Congratulations, you guessed the word! Would you like to play again? (y/n): ")

                    if user_play.lower() == "y":
                        secret_word = choose_word(wordlist)
                        hangman_with_hints(secret_word)
                    else:
                        print("----------------------------------")
                        print("Thank you for playing!")
                else:
                    is_word_guessed_bool = False

            elif letters_guessed not in get_available_letters(letters_guessed_as_list):
                print(letters_guessed, " is not an available letter")
                if warnings > 0:
                    print("----------------------------------")
                    warnings -= 1
                    print("You lose a warning. You have ", warnings, " left.")
                elif warnings == 0:
                    print("----------------------------------")
                    tries -= 1
                    print("No more warnings, you lose a try. You have ", tries, " left.")

        elif letters_guessed == "*":

            show_possible_matches(current_guessed_word)

        else:
            if warnings > 0:
                print("----------------------------------")
                warnings = warnings - 1
                print("Please input letters only, you lose a warning.")
                print("Warnings left: ", warnings)

            elif warnings == 0:
                print("----------------------------------")
                tries = tries - 1
                print("You've run out of warnings, you lose a try...")
                print("Tries remaining: ", tries)

    if tries == 0:
        user_play = input("You've run out of tries! Would you like to play again? (y/n): ")
        print("Secret word was ", secret_word)
        if user_play.lower() == "y":
            secret_word = choose_word(wordlist)
            hangman_with_hints(secret_word)

        else:
            print("Thank you for playing! The secret word was ", secret_word)
    ('''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    ''')





# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
