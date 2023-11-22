#generate random word from a list of random words
#generate as many "_" as letters in the word
#ask user to guess a letter
#if the guessed letter is in the word, show that letter
#if not you will lose a life
#step 4 and if we guess every letter right within 6 wrong answers, you won
#step 5 and if you make 6 wrong moves, you lose

import random
import hangman_art
import hangman_wordlist


#importing logo from hangman_art
logo = hangman_art.logo
print(logo)

#generate random word from a list of random words
words = hangman_wordlist.words
chosen_word = random.choice(words)
print(chosen_word)
lives = 6


#generate as many "_" as letters in the word

display = []
for _ in chosen_word:
    display += "_"
print(display)

#ask user to guess a letter
end_of_game = False
while not end_of_game:
    user_input = input("guess a letter: ").lower()
    if user_input in display:
        print("letter", user_input, "already guessed")
 
    if user_input not in  chosen_word:
        lives -= 1
        print("The letter ", user_input, " not in the word, you lost a life")
        if lives == 0:
            end_of_game = True
            print("you lose")
    if user_input in chosen_word:
        for l in range(len(chosen_word)):
            letter = chosen_word[l]
            if letter == user_input:
                display[l] = letter
    print(' '.join(display))
    if "_" not in display:
        print("Congratualions, You won")
        end_of_game = True
    stages = hangman_art.stages
    print(stages[lives])
    