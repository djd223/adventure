import random
import os
import time

def hangman():
  word = select_word().upper()
  player_correct = []
  player_incorrect = []
  player_tries = 6
  for i in range(0,len(word)-1):
    player_correct.append("_")

  print("\nAnd whats he then that says I play the villain?")
  print("Let's begin:\n")
  print(f"Tries: {player_tries}\n")
  print(hangman_list[player_tries])
  print(f"{player_correct}\n")

  victory = None

  while True:
    if "_" not in player_correct:
      victory = True
      break
    if player_tries == 0:
      victory = False
      break

    guess = player_guess()

    if guess in word:
      index = 0
      while index <= len(word)-1:
          index = word.find(guess, index)
          if index == -1:
            break
          player_correct[index] = guess
          index += 1
    elif guess not in word:
      if guess in player_incorrect:
        os.system('clear')
        print("\n\nRepeat offence... SHAMEFUL\nI feel no pity for your wasted life.\n\n")
        time.sleep(2)
        os.system('clear')
      else:
        os.system('clear')
        print("Thou art a boil, a plague sore")

      player_tries -= 1
      player_incorrect.append(guess)

    print(f"Tries: {player_tries}\n")
    print(hangman_list[player_tries])
    print(f"False Letters: {player_incorrect}\n")
    print(f"{player_correct}\n")
    print(word)

  os.system('clear')
  if victory == True:
    print("Congratulations. Here is your key to progress:\n\n")
    print('"I have always been by your side."\n')
    time.sleep(5)
    input("Press enter to continue... ")
    return
  elif victory == False:
    player_continue = input("It is over. I grant no reprieves. But for you I offer the choice. Continue?(yes/no):  ")
    if "y" in player_continue.lower():
      hangman()
      return
    else:
      print("I will not willingly provide the solution. It must be earned. Remember this.")
      time.sleep(5)
      input("Press enter to continue... ")
      return



def select_word():
  with open('./word_bank.txt') as f:
    words = f.readlines()
    length = len(words)
    word = words[random.randint(0, len(words)-1)]
  return word


def player_guess():
  guess = None
  while guess == None:
    guess = input("Guess:   ")
    if len(guess) != 1 or not guess.isalpha():
      guess = None
      print("Guess a single letter...")
  return guess.upper()




























hangman_6 = '''
    ------------
    |          |
               |
               |
               |
               |
              /|\\
             / | \ 
             
             '''
hangman_5 = '''
    ------------
    |          |
    0          |
               |
               |
               |
              /|\\
             / | \ 
             
             '''
hangman_4 = '''
    ------------
    |          |
    0          |
    |          |
    |          |
               |
              /|\\
             / | \ 
             
             '''
hangman_3 = '''
    ------------
    |          |
    0          |
    |\         |
    |          |
               |
              /|\\
             / | \ 
             
             '''     
hangman_2 = '''
    ------------
    |          |
    0          |
   /|\         |
    |          |
               |
              /|\\
             / | \ 
             
             '''
hangman_1 = '''
    ------------
    |          |
    0          |
   /|\         |
    |          |
     \         |
              /|\\
             / | \ 
             
             '''
hangman_0 = '''
    ------------
    |          |
    0          |
   /|\         |
    |          |
   / \         |
              /|\\
             / | \ 
             
             '''
             
hangman_list = [hangman_0, hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6]

    

  