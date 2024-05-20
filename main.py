from player import Player
from game import Game


# Administration services not required in this logic, Player can manage their accounts
# Unless if it is support issues, player will have to contact with admins or support desk
# Through a contact system that I will attach to the program

def start_game(player):
    line:str = '-'*40
    game:Game = Game()
    action:int = int(input(f'{line}\n-- Game Options --\n\t1 ---- New Game\n\t2 ---- Continue\n\t3 ---- Game settings\n\t4 ---- Player Account\n\t0 ---- Logout\n\t[CHOICE]: '))
    if action == 1:
        game.start()
    elif action == 2:
        game.resume()
    elif action == 3:
        game.settings()
    elif action == 4:
        player.delete_player_account()
    else:
        exit(0)

def main_menu() -> None:
    player:Player = Player() #Just making sure that I get a real player object with the type annotations
    print('--- [WELCOME USER] ---')
    action:int = int(input(f'What are we doing today?\n\t1 --- Login\n\t2 --- Create Account\n\t0 --- Exit\n\t[CHOICE]: '))
    if action == 1:
        player.login()
        start_game(player=player)
    elif action == 2:
        player.register()    
        exit(0)
    else:
        print(f'[WRONG INPUT] {action} : Please input a positive number!')
        main_menu()
        
# Now, check if user wants to run this class and execute it
if __name__=='__main__':
    main_menu()