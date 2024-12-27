@ -0,0 +1,22 @@
import mysql.connector

my_db = mysql.connector.connect(
    user="root",
    password="o89h^h7r^Jr*bL1",
    host="127.0.0.1",
    database="restaurant_management"
)

cursor = my_db.cursor()

def create_table(str):
    return cursor.execute(f"CREATE TABLE {str}")

def fetch_data(str):
    return cursor.fetchall()

def delete_table(table):
    return cursor.execute(f"DROP TABLE {table}")

create_table("This")
fetch_data("This")