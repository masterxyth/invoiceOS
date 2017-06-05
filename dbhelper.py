import datetime

import config

import pymysql


class DBHelper:

    def connect(self, database="indentify"):
        return pymysql.connect(host='localhost', user=config.db_user, password=config.db_password, db=database, autocommit=True)

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
            query = "SELECT email FROM user WHERE email = %s;"
            with conn.cursor() as cursor:
                cursor.execute(query, email)
                return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            conn.close()
