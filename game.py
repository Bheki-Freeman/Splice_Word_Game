# The game logic, game Loop and so on
import time
from words import create_list,lst

class Game():
    is_running:bool = False 
    def game_loop(self):
        while(self.is_running):
            self.game()
            
    def game(self): 
        create_list()
        print(lst)    
        play = input('[LIST and MATCHING LETTERS] as (1b) or .q to QUIT! : ') 
        if play != '.q':            
            print(f'You Chose {play}')
            lst.clear()            
        else:
            self.stop()            
    def start(self) -> None:
        self.is_running = True
        print('Game Started!')
        print('Choose matching ALPHABETS from the following lists')
        self.game_loop()

    def stop(self) -> None:
        self.is_running = False
        print('\n\t--- [GAME OVER] ---')
    def settings(self) -> None:
        print('--- [GAME SETTINGS] ---')
    def resume(self) -> None:
        print('Resume')