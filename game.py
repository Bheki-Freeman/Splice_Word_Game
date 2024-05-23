# The game logic, game Loop and so on
import time
from words import create_list,lst

# lines
line = '-'*40

class Game():
    is_running:bool = False 
    def game_loop(self):
        while(self.is_running):
            self.game()
            
    def game(self): 
        create_list()
        print(lst)    
        play = input('\n[MATCH] as (U-U-0-U) (0 if no match) or .q to QUIT! : ') 
        if play != '.q':            
            print(f'\nYou Chose {play}')
            lst.clear()            
        else:
            self.stop()            
    def start(self) -> None:
        self.is_running = True
        print(f'{line}\n\t --- \tGame Started\t ---\n{line}')
        print('Choose matching ALPHABETS from the following lists\n')
        self.game_loop()

    def stop(self) -> None:
        self.is_running = False
        print('\n\t--- [GAME OVER] ---')
    def settings(self) -> None:
        print('--- [GAME SETTINGS] ---')
    def resume(self) -> None:
        print('Resume')