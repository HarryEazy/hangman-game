import random
import hangman_words
import hangman_art
from replit import clear

word_list = hangman_words.word_list
stages = hangman_art.stages

#List for letters used
guessed_letters = []
#Create blanks
display = []
#Get random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Print logo
print(hangman_art.logo)


for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    while guess in guessed_letters:
      guess = input(f"{guess} has already been used, please try another letter: ")
      clear()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"\n{guess} is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"\nThe word was {chosen_word}")
            print("You lose.")

    guessed_letters.append(guess)
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(stages[lives])