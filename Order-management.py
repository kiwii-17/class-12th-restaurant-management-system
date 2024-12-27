from menu.order import order_report, menu_category, menu_order_options, fetch_prices
import mysql.connector
from cryptography.fernet import Fernet
import json
import inquirer
import os

order_key = Fernet.generate_key()
order_log = {}
result = order_report()

order_log[str(order_key)] = result

question = [
    inquirer.Confirm(
        "confirmation",
        message="Do you want to place a new order"
    )
]

confirmation = inquirer.prompt(question)

while confirmation["confirmation"] != False:

    result = order_report()
    order_key = Fernet.generate_key()
    order_log[str(order_key)] = result

    confirmation = inquirer.prompt(question)

with open("menu/order.json", "a") as f:
    json.dump(order_log, f)

my_db = mysql.connector.connect(
    user="root",
    host="127.0.0.1",
    password="",
    database="restaurant_management"
)

cursor = my_db.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS Customers(
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255) NOT NULL
                )""")


cursor.execute("""CREATE TABLE IF NOT EXISTS Orders(
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                menu_item_id INT NOT NULL,
                customer_id INT NOT NULL,
                order_date DATE NOT NULL,
                order_time TIME NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
                FOREIGN KEY (menu_item_id) REFERENCES Menu(menu_item_id)
                )""")

def update_Custormers(name):
    cursor.execute("INSERT INTO Customers(Name) VALUES (%s)", [name])
    my_db.commit()

def update_Orders(order_date, order_time):
    cursor.execute("INSERT INTO Orders(order_date, order_time) VALUES (%s, %s)", (order_date, order_time))
    my_db.commit()

with open("menu/order.json", "r") as f:
    data = json.load(f)


for records in data.values():
    print(records)
    update_Custormers(records["name"])
    update_Orders(records["order_date"], records["order_time"])

os.remove("menu/order.json")

cursor.close()
my_db.close()