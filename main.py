print("welcome to the hangman game world!")
logo = '''                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    
'''
print(logo)
word_list = ["jagdish", "omkar", "manoj", "vikash", "bhagu"]
import random

stages = [
    '''
             _______
     |/      |
     |       O
     |     / | /
     |      /  /
     |______________      
     _______________
       ''', '''
             _______
     |/      |
     |       O
     |     / | /
     |      / 
     |______________      
     _______________
           ''', '''
               _______
     |/      |
     |       O
     |     / | /
     |       
     |______________      
     _______________     
          ''', '''
           _______
     |/      |
     |       O
     |     / | 
     |       
     |______________      
     _______________
          ''', '''
             _______
     |/      |
     |       O
     |     / 
     |      
     |______________      
     _______________
           ''', '''
            _______
     |/      |
     |       
     |     
     |      
     |______________      
     _______________
          '''
]

choisen_word = random.choice(word_list)
print(f"the choisen word is {choisen_word}")
end_of_game = False
lives = 6

display = []
for _ in range(len(choisen_word)):
    display += "_"
print(display)

while not end_of_game:
    guess = input("guess the letters:").lower()

    for _position in range(len(choisen_word)):
        letter = choisen_word[_position]

        if letter == guess:

            display[_position] = letter
        else:
            print("no match.")
    if guess not in choisen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose.")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("you win!")

    print(stages[lives - 1])
