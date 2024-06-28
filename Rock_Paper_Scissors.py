'''
Rock Paper Scissors game
------------------------------------------------------------------------------------------------------
'''

import random
import os
import re 
import time

def check_play_status():
    Valid_Response = ["yes", "no"]
    while True:
        try:
            
            Reponse = input("Do you wish to play again? (Enter Yes/No)") 
            if Reponse.lower() not in Valid_Response:
                raise ValueError ("Yes or No only pls")
            
            if Reponse.lower() == "yes":
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing')
                exit()
        except ValueError as err:
            print(err)


def play_rps():
    Play = True
    while Play:
        os.system('cls' if os.name == 'nt' else 'clear')
        Choises = ['R', 'P', 'S']
        opp_choice = random.choice(Choises)
        print('Rock, Paper Scissors, Shoot!')
        
        User_Choice= input('choose your wepone [R]ock, [P]apper, [S]cissors')
        
        if not re.match("[SsRrPp]",User_Choice):
            print('Please choose a letter:')
            print('[R]ock, [P]aper, or [S]cissors')
            time.sleep(3)
            continue
        
        print(f'you choose {User_Choice}')
        print(f'I Choose {opp_choice}')
        
        if opp_choice == User_Choice.upper():
            print("Tie!!")
            Play = check_play_status()
        elif opp_choice == 'R' and User_Choice.upper() == 'S':
            print("Rock beats Scissors, I WIN!!")
            Play = check_play_status()
        elif opp_choice == 'S' and User_Choice.upper() =='P':
            print("Scissors beats Paper, I WIN!!")
            Play = check_play_status()
        elif opp_choice == 'P' and User_Choice.upper() == 'R':
            print("Paper beats Rock, I WIN!!")
            Play = check_play_status()
        else:
            print("You Win!!")
            Play = check_play_status()
        
if __name__ == "__main__":
    play_rps()