import random
from traceback import print_list
print(''' _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/                      ''')
stages = [''' 
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========''', ''' 
+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', ''' 
+---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', ''' 
+---+
  |   |
  O   |
 /|   |
      |
      |
=========''', ''' 
+---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
+---+
  |   |
  O   |
      |
      |
      |
=========''', ''' 
+---+
  |   |
      |
      |
      |
      |
=========''']
lives = 6
word = ['apple', 'banana', 'carrot']
random_word = random.choice(word)
space = []
for underscore in random_word:
    space += "_"
while True:
    print(' '.join(space))
    guess_letter = input("Enter a letter\n").lower()
    if guess_letter in space:
        print("You have already chosen this letter,Please try some other letter")
    for letter in range(len(random_word)):
        if guess_letter == random_word[letter]:
            space[letter] = random_word[letter]
    if guess_letter not in random_word:
        print("You lose a life")
        print(stages[lives])
        lives -= 1
        print(f"The number of lives you have is {lives}")
        if lives == 0:
            print("You have lost this game")
            print(f"The word is {random_word}")
            print("Better luck next time")
            break
    if "_" not in space:
        print("You Win")
        break
