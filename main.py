import random
import time
import os
from hangman import hangman


def main():
    victory = False
    while victory == False:
        if death_cycle():
            victory = True
        if victory == True:
            break

    #PNG of final scene of Seventh Seal using Tkinter
    print("ALL DONE")
    return

def death_cycle():
    os.system('clear')
    print("And when the Lamb had broken the seventh seal there was silence in heaven about the space of half an hour.")
    time.sleep(1)
    print("And the seven angels who had the seven trumpets prepared themselves to sound.")
    time.sleep(3)
    os.system('clear')

    user_name = input("Who are you?  ")
    if "death" in user_name.lower():
        user_come = input("Have you come for me?  ")
        if "by your side" in user_come.lower():
            user_ready = input("Yes, I know...  ")
            if "ready" in user_ready.lower():
                print("My flesh is afraid, but I am not")
                time.sleep(3)
                user_chess = input("Wait a moment. You play chess, do you not?  ")
                if "y" in user_chess.lower():
                    if play_chess():
                        return True
        else:
            print("You are not ready...")
            time.sleep(2)
            print("...let us continue")
            time.sleep(2)
            hangman()
    else:
        print("You are not ready...")
        time.sleep(2)
        print("...let us continue\n\n")
        grave_riddle()
    return False

def play_chess():
    print("CHESS!")
    return True
    #Make sure the user is in a position they cannot win

def grave_riddle():
    seed = random.randint(1,2)
    tries = 3
    while tries > 0:
        print(f"\n{tries} Tries:")
        if seed == 1:
            answer = input("What is he that builds stronger than either the mason, the shipwright, or the carpenter?  " )
            if "gravedigger" in answer.lower():
                print("Correct...")
                death_question()
                return
        if seed == 2:
            answer = input("I am not alive but grow; I don't need air or time to slow. I rest where silence is a guest. What am I?  " )
            if "graveyard" in answer.lower():
                print("Correct")
                death_question()
                return
        tries -= 1
    if player_continue() == True:
        grave_riddle()
        return
    return

def death_question():
    time.sleep(2)
    print("\n\nNow for another question:")
    tries = 3
    while tries > 0:
        print(f"\n{tries} Tries:")
        player_answer = input("And who resides over the armies that live in this domain?  ")
        if "death" in player_answer:
            print("Congratulations. Here is your key to progress:\n")
            print('"Death"\n')
            time.sleep(3)
            input("Press enter to continue... ")
            return
        tries -= 1
    if player_continue() == True:
        grave_riddle()
        return
    return


def player_continue():
    os.system('clear')
    player_continue = input("It is over. I grant no reprieves. But for you I offer the choice. Continue?(yes/no):  ")
    if "y" in player_continue.lower():
        return True
    else:
      print("I will not willingly provide the solution. It must be earned. Remember this.")
      time.sleep(5)
      input("Press enter to continue... ")
      return False

main()