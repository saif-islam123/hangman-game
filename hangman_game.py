import random
import hangman_art
import hangman_words 

print(hangman_art.logo)

stages = hangman_art.stages
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

lives = 6
display = ["_"] * len(chosen_word)
#  Main loop 
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower() 

    if guess in display:
        print(f"You have already guess the letter {guess}")
        continue
    
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    else:
        lives -= 1
        print(f"The letter {guess} is not in the word. You lose a life")
        print(stages[lives])        

        if lives == 0:
            print("You lose! ")
            break
        
    print(" ".join(display))

if "_" not in display:
    print("You won the game!")

print(stages[lives])

       
    



