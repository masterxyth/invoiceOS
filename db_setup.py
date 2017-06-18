import pymysql
import config

connection = pymysql.connect(host='localhost', user=config.user, passwd=config.password)

try:
    with connection.cursor() as cursor:

        sql = "CREATE DATABASE IF NOT EXISTS indentify"
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS indentify.company (id int NOT NULL AUTO_INCREMENT,
        name VARCHAR(128),
        address1 VARCHAR(255),
        address2 VARCHAR(255),
        phone VARCHAR(255),
        fax VARCHAR(255),
        email VARCHAR(255),
        PRIMARY KEY (id));"""

        cursor.execute(sql)

        sql= """CREATE TABLE IF NOT EXISTS indentify.user (id int NOT NULL AUTO_INCREMENT,
        cid INT NOT NULL,
        email VARCHAR(50),
        salt CHAR(156),
        hashed CHAR(156),
        PRIMARY KEY (id)
        FOREIGN KEY (cid) REFERENCES indentify.company(id));"""
        cursor.execute(sql)

        sql= """CREATE TABLE IF NOT EXISTS indentify.indent (id INT NOT NULL AUTO_INCREMENT,
        uid INT NOT NULL,
        create_date DATETIME,
        last_update TIMESTAMP,
        status VARCHAR(50),
        type VARCHAR(50),
        PRIMARY KEY (id),
        FOREIGN KEY (uid) REFERENCES indentify.user(id));"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS indentify.terms (id int NOT NULL AUTO_INCREMENT,
        iid INT NOT NULL,
        term VARCHAR(255),
        PRIMARY KEY (id),
        FOREIGN KEY (iid) REFERENCES indentify.indent(id));"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS indentify.line_item (id INT NOT NULL AUTO_INCREMENT,
        pid INT NOT NULL,
        iid INT NOT NULL,
        unit VARCHAR(10) NOT NULL,
        price NUMERIC(15,2),
        package VARCHAR(10),
        comission NUMERIC(15,2),
        load VARCHAR(10),
        PRIMARY KEY (id),
        FOREIGN KEY (iid) REFERENCES indentify.indent(id),
        FOREIGN KEY(pid) REFERENCES indentify.product(id));"""
        cursor.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS indentify.product (id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255),
        PRIMARY KEY (id));"""
        cursor.execute(sql)

        connection.commit()
finally:
    connection.close()
