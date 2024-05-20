# The game logic, game Loop and so on
import time

class Game():
    is_running:bool = False 
    def game_loop(self):
        while(self.is_running):
            play = input('Choose a Letter from [A, B, C] or type .q to QUIT!: ') # This is not the real logic of our game, only for test purposes
            if play != '.q':
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