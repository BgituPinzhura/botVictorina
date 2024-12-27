import sqlite3


class Database:
    def __init__(self, root: str):
        self.database = sqlite3.connect(root)
    
    def is_registered(self, telegram_id: str) -> bool:
        sql_text = f"SELECT TELEGRAM_ID FROM USERS"
        users = self.database.execute(sql_text).fetchall()
        for i in range(len(users)):
            if str(telegram_id) == str(users[i][0]):
                return True
        return False
    
    def registration(self, telegram_id: str, question_type: int) -> None:
        sql_text = f"INSERT INTO USERS (TELEGRAM_ID, QUESTION_TYPE, IS_ADMIN)" \
                   f" VALUES ({telegram_id}, {question_type}, 0);"
        self.database.execute(sql_text)
        self.database.commit()
    
    def set_question_type(self, question_type: int, telegram_id: str, ) -> None:
        sql_text = "UPDATE USERS SET QUESTION_TYPE = " + str(question_type) + \
                   " WHERE TELEGRAM_ID = " + str(telegram_id) + ";"
        self.database.execute(sql_text)
        self.database.commit()
    
    def set_admin_access(self, is_admin: bool, telegram_id: str) -> None:
        sql_text = "UPDATE USERS SET IS_ADMIN = " + str(is_admin) + \
                   " WHERE TELEGRAM_ID = " + telegram_id + ";"
        self.database.execute(sql_text)
        self.database.commit()
    
    def get_admin_access(self, telegram_id: str) -> bool:
        sql_text = f"SELECT IS_ADMIN FROM USERS WHERE TELEGRAM_ID = {telegram_id};"
        result = self.database.execute(sql_text).fetchall()
        return bool(result[0][0])
    
    def get_question_type(self, telegram_id: str) -> int:
        sql_text = f"SELECT QUESTION_TYPE FROM USERS WHERE TELEGRAM_ID = {telegram_id};"
        result = self.database.execute(sql_text).fetchall()
        return result[0][0]
