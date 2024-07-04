import random
import time
import os


def main():
    victory = False
    print("And when the Lamb had broken the seventh seal there was silence in heaven about the space of half an hour.")
    time.sleep(1)
    os.system('clear')
    print("And the seven angels who had the seven trumpets prepared themselves to sound.")
    time.sleep(1)
    os.system('clear')

    while victory == False:
        if death_cycle():
            victory = True
        if victory == True:
            break

        print("You are not ready...")
        time.sleep(2)
        print("...so let us begin")
        grave_riddle()



    #PNG of final scene of Seventh Seal using Tkinter
    print("ALL DONE")
    return

def death_cycle():
    user_name = input("Who are you? ")
    if "death" in user_name.lower():
        user_come = input("Have you come for me?")
        if "by your side" in user_come.lower():
            user_ready = input("Yes, I know...  \n\n")
            if "ready" in user_ready.lower():
                print("My flesh is afraid, but I am not")
                time.sleep(3)
                user_chess = input("Wait a moment. You play chess, do you not?")
                if "y" in user_chess.lower():
                    if play_chess():
                        return True
    return False

def play_chess():
    print("CHESS!")
    return True
    #Make sure the user is in a position they cannot win

def grave_riddle():
    seed = random.randint(1,2)
    tries = 3
    while tries > 0:
        print(f"{tries} Tries:\n")
        if seed == 1:
            answer = input("What is he that builds stronger than either the mason, the shipwright, or the carpenter?" )
            if "gravedigger" in answer.lower():
                print("Correct...")
                return True
        if seed == 2:
            answer = input("I am not alive but grow; I don't need air or time to slow. I rest where silence is a guest. What am I?" )
            if "graveyard" in answer.lower():
                print("Correct")
                return True
        tries -= 1
    return False


main()