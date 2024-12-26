import mysql.connector
import json

my_db = mysql.connector.connect(
    user="root",
    password="",
    host="127.0.0.1",
    database="restaurant_management"
)

cursor = my_db.cursor()

def create_table_Menu():
    return cursor.execute("""CREATE TABLE IF NOT EXISTS Menu(
                          menu_item_id INT AUTO_INCREMENT PRIMARY KEY,
                          Name VARCHAR(255), 
                          Description VARCHAR(255),
                          Price DECIMAL
                          )""")

def fetch():
    return cursor.fetchall()

def insert():
    with open("menu/menu.json", "r") as f:
        data = json.load(f)

    for heading in data:
        if heading == "restaurant":
            continue

        else:
            for item in data[heading]:
                if item != "Ordinary & Happy":
                    for dishes in data[heading][item]:
                        query = "INSERT INTO Menu (Name, Description, Price) VALUES (%s, %s, %s)"
                        cursor.execute(query, (dishes["name"], dishes["description"], dishes["Price"]))
                else:
                    continue

    return cursor.fetchall()

create_table_Menu()
print(insert())




