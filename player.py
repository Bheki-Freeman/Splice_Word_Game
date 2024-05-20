# Take in the user details
# Log in the user
# User's Data saved into the database (sqlite 3 for now)
# User can remove Previous Data(Game statistics) and refresh
# The Game Statistics include (High Scores, Current Scores)
 
import sqlite3
from getpass import getpass

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
                print('[PLAYER SUCCESSFULLY REGISTERED!]')
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
    def login(self) -> object: #For now, we return void
        try:
            user_name = input('[USERNAME]: ')
            user_pass = getpass('[PASSWORD]: ')
            if self.fetch_user(user_name, user_pass):
                print('[ACCESS GRANTED]')
                return self
            else:
                print('[LOGIN FAILURE!]: Wrong Credentials')
                have_account = ('[DONT HAVE AN ACCOUNT?] yes / no: ')
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
                