from player import Player
from game import Game


# Administration services not required in this logic, Player can manage their accounts
# Unless if it is support issues, player will have to contact with admins or support desk
# Through a contact system that I will attach to the program
line = '*'*40


def main_menu() -> None:
    try:
        player:Player = Player() #Just making sure that I get a real player object with the type annotations
        print(f'{line}\n\t--- [WELCOME USER] ---\n{line}\n')
        action:int = int(input(f'What are we doing today?\n\t1 --- Login\n\t2 --- Create Account\n\t0 --- Exit\n\t[CHOICE]: '))
        if action == 1:
            player.login()
        elif action == 2:
            player.register()    
        elif action == 0:
            exit(0)
        else:
            print(f'[WRONG INPUT] {action} : Please choose from the given list of Numbers!')
            main_menu()
    except (TypeError, ValueError) as er:
        print(f'[ERROR]: Please type numbers or text where due!')
        main_menu()
        
# Now, check if user wants to run this class and execute it
if __name__=='__main__':
    main_menu()