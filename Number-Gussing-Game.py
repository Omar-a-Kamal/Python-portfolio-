#number gussing game
import random

def show_score(attempts_list):
    if not attempts_list:
        print('There is currently no best score,'
              'it\'s yours for the taking!')
    else:
        print('the current score is ' f'{min(attempts_list)} attempts')
        
def wanna_play_evaluation(x):
    
    if x == 'yes' or x == 'no':
        return x
    else:
        return False
    
def didnt():
    print('I didn\'t get that please type "Yes" or "No"')
        
def Start_Game():
    attempts = 0
    rand_num = random.randint(1,10)
    attempts_list = []
    
    print('Hello Traveller! welcome to the game of guessing')
    player_name = input("What's your name? " )
    print(f'Hi {player_name}')

    while wanna_play_evaluation('yes') != False:
        wanna_play = input('would you like to play the gussing game? (Enter Yes or No):')
        wanna_play_eval = wanna_play_evaluation(wanna_play.lower())
    
        if wanna_play_eval:
       
            if wanna_play.lower() == 'no':
                print("that's cool, Thanks!")
                exit()
                
            elif wanna_play.lower() == 'yes':
                        
                while  wanna_play.lower() == 'yes':     #True:   
                    
                    #if wanna_play.lower() == 'yes':
                        show_score(attempts_list)
                    
                        while wanna_play.lower() == 'yes':
                            try:
                                guess = int(input('pick a number between 1 and 10 '))
                                
                                if guess < 1 or guess > 10 :
                                    raise ValueError ('please enter a value betweeen 1 and 10')
                                attempts += 1
                                
                                if guess == rand_num:
                                    attempts_list.append(attempts)
                                    print('Nice! you got it')
                                    print(f'it took you {attempts} attemps to figure it out')
                                    wanna_play = input('wanna play again? (Enter Yes or No):')
                                    eval_result = wanna_play_evaluation(wanna_play)
                                    if eval_result != False:
                                        
                                        if wanna_play.lower() == 'no':
                                            print("that's cool!")
                                            exit()
                                        else:
                                            attempts = 0
                                            rand_num = random.randint(1 , 10)
                                            show_score(attempts_list)
                                            continue
                                    else:
                                        didnt()
                                        continue
                                            
                                else:
                                    if guess > rand_num:
                                        print("it's lower")
                                    elif guess < rand_num:
                                        print("it's higher")
                            except ValueError as err:
                                print('oh no! the value is out of range, try again!')
                                print(err)

        elif wanna_play_eval == False:
       
            didnt()



        
if __name__ == '__main__':
    Start_Game()
         
                   

        