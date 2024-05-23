# The game logic, game Loop and so on
import time
from words import create_list,lst

class Game():
    is_running:bool = False 
    def game_loop(self):
        while(self.is_running):
            self.game()
            lst.clear()
            
    def game(self):
        print('The alphabet letters:')
        
        print()
        play = input('Choose a Letter from [A, B, C] or type .q to QUIT!: ') # This is not the real logic of our game, only for test purposes
        create_list()
        if play != '.q':            
            print(lst)
            print(f'You Chose {play}')
        else:
            self.stop()            
    def start(self) -> None:
        self.is_running = True
        print('Game Started!')
        self.game_loop()

    def stop(self) -> None:
        self.is_running = False
        print('\n\t--- [GAME OVER] ---')
    def settings(self) -> None:
        print('--- [GAME SETTINGS] ---')
    def resume(self) -> None:
        print('Resume')