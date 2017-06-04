import pymysql
import dbconfig

connection = pymysql.connect(host='localhost', user=dbconfig.db_user, passwd=dbconfig.db_password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS indentify"
        cursor.execute(sql)
        sql= """CREATE TABLE IF NOT EXISTS indentify.user (id int NOT NULL AUTO_INCREMENT,
        email VARCHAR(50),
        salt CHAR(156),
        hashed CHAR(156),
        PRIMARY KEY (id)
        )"""
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
