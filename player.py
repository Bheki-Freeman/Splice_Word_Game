# Take in the user details
# Log in the user
# User's Data saved into the database (sqlite 3 for now)
# User can remove Previous Data(Game statistics) and refresh
# The Game Statistics include (High Scores, Current Scores)
 
import sqlite3
conn = sqlite3.connect('main.db')
cur = conn.cursor()

class Player():
    def __init__(self) -> None:
        pass
    def set_values(self, name, username, password, age, gender, phone) -> None:
        self.name = name
        self.username = username
        self.age  = age 
        self.gender = gender 
        self.password = password
        self.phone = phone 
    def register(self) -> None:
        try:
            self.name = input('[NAME]: ')
            self.take_user_name()
            self.password = input('[PASSWORD]: ')
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
                
        except ValueError as ve:
            print(f'[ERROR]: {ve.args}')
        
    def take_user_name(self) -> None:
        username = input('[USERNAME]: ')
        if self.check_name(username): # Just to make sure that the username is unique
            self.username = username
        else:
            print(f'{username} [ALREADY TAKEN]!')
            self.take_user_name()
    def check_name(self, username) -> bool:
        sql = f"SELECT * FROM player WHERE username='{username}'"
        result = cur.execute(sql).fetchall()
        if not result: # If username has'nt been found we return True
            return True
        else:
            return False
        
    def login(self, username, password) -> bool:
        sql = f"SELECT name, username, password FROM player WHERE username='{username}' AND password='{password}'"
        result = cur.execute(sql).fetchall()
        if not result:
            return False
        else:
            return True
                