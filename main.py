import random
import hangman_words as hw

chosen_word = random.choice(hw.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


import hangman_art as ha
print(ha.logo)

print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    
    if guess in display:
      print(f"you already enterd the letter {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

   
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(ha.stages[lives])