import datetime

import config

import pymysql
connect = pymysql.connect(host='localhost', user='root', password='Mc$pacejam101', db='indentify', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
class DBHelper:

    def connect(self, database="indentify"):
        return pymysql.connect(host='localhost', user=config.db_user, password=config.db_password, db=database, autocommit=True, cursorclass=pymysql.cursors.DictCursor)

    def create_user(self, email,salt, hashed):
        conn = self.connect()
        try:
            query = "INSERT INTO user (email, salt, hashed)\
             VALUES (%s,%s,%s);"
            with conn.cursor() as cursor:
                cursor.execute(query, (email, salt, hashed))
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def get_user(self, email):
        conn = self.connect()
        try:
            query = "SELECT * FROM user WHERE email = %s;"
            with conn.cursor() as cursor:
                cursor.execute(query, email)
                return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            conn.close()

    def create_company():
        return
    def get_company():
        return

    def update_company():
        return

    def create_indent():
        return

    def get_indent():
        return

    def update_indent():
        return
