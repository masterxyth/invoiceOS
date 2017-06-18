import datetime

import config

import pymysql
connect = pymysql.connect(host='localhost', user=config.user, password=config.password, db=config.db, autocommit=True, cursorclass=pymysql.cursors.DictCursor)
class DBHelper:

    def connect(self, database="indentify"):
        return pymysql.connect(host='localhost', user=config.user, password=config.password, db=config.db, autocommit=True, cursorclass=pymysql.cursors.DictCursor)

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



    def get_company(self, uid):
        conn = self.connect()
        try:
            query = "SELECT * FROM company WHERE uid = %s;"
            with conn.cursor() as cursor:
                cursor.execute(query, uid)
                return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            conn.close

    def create_company(self, uid, name, address1, email, address2='', phone='', fax=''):
        conn = self.connect()
        try:
            query = "SELECT uid FROM company WHERE uid= %s;"
            with conn.cursor() as cursor:
                cursor.execute(query, uid)
                results = cursor.fetchall()
            if results:
                try:
                    query = "UPDATE company SET name = %s, address1 = %s, address2 = %s, phone = %s, fax = %s, email = %s\
                    where uid = %s;"
                    with conn.cursor() as cursor:
                        cursor.execute(query, (name, address1, address2, phone, fax, email, uid))
                except Exception as e:
                    print(e)
                finally:
                    conn.close()
            else:
                try:
                    query= "INSERT INTO company (uid, name, address1, address2, phone, fax, email)\
                    VALUES (%s, %s, %s, %s, %s, %s, %s);"
                    with conn.cursor() as cursor:
                        cursor.execute(query, (uid, name, address1, address2, phone, fax, email))
                except Exception as e:
                    print(e)
                finally:
                    conn.close()
        except Exception as e:
            print(e)


"""    def create_indent(self, uid, create_date, last_update, status, type):
        conn = self.connect()
        try:
            query= "INSERT INTO indent (uid, create_date, last_update, status, type )"
        return

    def create_terms():
        return

    def get_terms():


    def get_indent():
        return

    def update_indent():
        return
"""
