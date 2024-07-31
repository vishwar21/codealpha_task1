import random
import hangman_stages
import word_file
lives=6
chosen_word=random.choice(word_file.words)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over=False
while not game_over:
    guess_letter=input("Guess a Letter:").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter==guess_letter:
            display[position]=guess_letter
    print(display)
    if guess_letter not in chosen_word:
            lives -=1
            if lives==0:
                game_over=True
                print("You Loose!!")
    if '_' not in display:
            game_over=True
            print("Game Over!!!YOU WIN")        
    print(hangman_stages.stages[lives])




