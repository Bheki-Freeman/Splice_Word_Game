# Take in the user details
# Log in the user
# User's Data saved into the database (sqlite 3 for now)
# User can remove Previous Data(Game statistics) and refresh
# The Game Statistics include (High Scores, Current Scores)
 
import sqlite3
from getpass import getpass
from game import Game

conn = sqlite3.connect('main.db')
cur = conn.cursor()

class Player(object):
    
    def __init__(self) -> None:
        pass
    def set_values(self, name, username, password, age, gender, phone) -> None:
        self.name = name
        self.username = username
        self.age  = age 
        self.gender = gender 
        self.password = password
        self.phone = phone 
    def delete_player_account(self) -> None: # Just delete, return nothing
        if len(self.name) != 0: # It's already available, but just to make things much easier  for the player
            try:
                def confirm_delete() -> bool:
                    confirm = input(f'[YOU REALLY WANNA DELETE ACCOUNT FOR]: {self.name} (yes / no)')
                    if confirm.lower() == 'yes':
                        return True
                    elif confirm.lower() == 'no': 
                        return False
                    else:
                        print('[WRONG USER INPUT] Please choose yes or no') # we just have to check all possible user actions, to communicate with them as effective as we can
                        confirm_delete()
                if confirm_delete():
                    del_password = getpass('[YOUR PASSWORD]')
                    self.delete(del_password)
                    print('[USER ACCOUNT REMOVED!]')
                    return 
                else : return
            except (TypeError, ValueError) as er:
                print(f'[USER INPUT ERROR]: {er}')
        else: 
            print(f'[NO ACCOUNT!]: user has to log in first!')
            log_in = input('[LOGIN] (yes /no): ')
            if log_in.lower() == 'yes':
                self.login()
            elif log_in.lower() == 'no':
                return
            else:
                print('[WRONG USER INPUT!] Please type in yes or no')
                self.delete_player_account()
    def delete(self, del_pass) -> None:
        sql = f"DELETE FROM player WHERE username='{self.username}' AND password='{del_pass}'"
        cur.execute(sql)
        conn.commit()
    def menu(self):
        line = '-'* 40
        try:
            print(f'{line}\n\t--- [PLAYER ACCOUNT] ---\n{line}\n')
            action:int = int(input(f'Manage Account Details?\n\t1 --- Games Played\n\t2 --- Update Account\n\t3 --- Remove Account\n\t0 --- Exit\n\t[CHOICE]: '))
            if action == 1:
                self.get_games()
            elif action == 2:
                self.update()
            elif action == 3:
                self.delete_player_account()
            elif action == 0:
                exit(0)
            else:
                print(f'[WRONG INPUT] {action} : Please choose from the given list of Numbers!')
                self.menu()
        except (TypeError, ValueError) as er:
            print(f'[ERROR]: Please type numbers or text where due!')
            self.menu()
    def update(self):
        print('updating player details')
    def get_games(self):
        print('printing Games Details')
        
    def register(self) -> None:
        try:
            self.name = input('[NAME]: ')
            self.take_user_name()
            self.password = getpass("[PASSWORD]: ")
            self.age = int(input('[AGE]: '))
            self.gender = input('[GENDER] as (M/F): ')
            self.phone = int(input('[PHONE] as (+268 76294516): '))            
            def create_user_data(self) -> bool:
                sql = f"INSERT INTO player (name, username, password, age, gender, phone) VALUES('{self.name}','{self.username}','{self.password}','{self.age}','{self.gender}','{self.phone}')"
                cur.execute(sql)
                conn.commit()
                return True                
            if create_user_data(self):
                logon:str = input('[PLAYER SUCCESSFULLY REGISTERED!]\n\t[LOGIN] yes/no: ')
                if logon.lower() == 'yes':
                    self.login()
                elif logon.lower() == 'no':
                    print('[THANK YOU FOR REGISTERING WITH US!!]')
                    exit(0) 
                else:
                    print('[WRONG CHOICE]')
            else:
                print('[USER REGISTRATION FAILED!]')
                
        except (TypeError, ValueError) as er:
            print(f'[WRONG INPUT FOR VALUE]: {er}')
            self.register() # Start registration process afresh
        
    def take_user_name(self) -> None:
        try:
            username = input('[USERNAME]: ')
            if self.check_name(username): # Just to make sure that the username is unique
                self.username = username
            else:
                print(f'{username} [ALREADY TAKEN]!') # In this case we need to ask user if they want to login, or re-create username
                log_in = input('[LOGIN WITH YOUR USER ACCOUNT?] (yes/no): ')
                if log_in.lower() == 'yes':
                    self.login()
                elif log_in.lower() == 'no':
                    self.take_user_name()
                else:
                    print('[WRONG USER INPUT!] Please choose yes or no! ')
                    self.take_user_name()
        except (TypeError, ValueError) as er:
            print(f'[ERROR]: {er}')
    def login(self) -> None: #For now, we return void
        try:
            user_name = input('[USERNAME]: ')
            user_pass = getpass('[PASSWORD]: ')
            if self.fetch_user(user_name, user_pass):
                print()
                print('-'*40)
                print('\t--- [ACCESS GRANTED] ---')
                self.start_game()
            else:
                print('[ACCESS DENIED!]')
                have_account:str = input('[DONT HAVE AN ACCOUNT?] yes / no: ')
                if have_account.lower() == 'yes':
                    self.register()
                else:
                    self.login()
        except (TypeError, ValueError) as er:
            print(f'[ERROR]: {er}')
            
    def check_name(self, username) -> bool:
        sql = f"SELECT * FROM player WHERE username='{username}'"
        result = cur.execute(sql).fetchall()
        if not result: # If username has'nt been found we return True
            return True
        else:
            return False
        
    def fetch_user(self, username, password) -> bool: # Since we are kind of checking we just have return true or false
        sql = f"SELECT name, username, password FROM player WHERE username='{username}' AND password='{password}'"
        result = cur.execute(sql).fetchall()        
        if not result:
            return False
        else:
            for row in result:
                self.name, self.username, self.password = row 
            return True
    def start_game(self):
        line:str = '-'*40
        game:Game = Game()
        action:int = int(input(f'{line}\n-- Game Options --\n\t1 ---- New Game\n\t2 ---- Continue\n\t3 ---- Game settings\n\t4 ---- Player Account\n\t0 ---- Logout\n\t[CHOICE]: '))
        print()
        if action == 1:
            game.start()
            self.menu()
        elif action == 2:
            game.resume()
        elif action == 3:
            game.settings()
        elif action == 4:
            self.menu()
        else:
            exit(0)
                