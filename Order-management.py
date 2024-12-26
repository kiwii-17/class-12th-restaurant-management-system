from menu.order import order_report, menu_category, menu_order_options
import mysql.connector
from cryptography.fernet import Fernet
import datetime

result = order_report()


my_db = mysql.connector.connect(
    user="root",
    host="127.0.0.1",
    password="",
    database="restaurant_management"
)

cursor = my_db.cursor()

def create_table_Customers():
    return cursor.execute("""CREATE TABLE IF NOT EXISTS Customers(
                   customer_id INT AUTO_INCREMENT PRIMARY KEY,
                   Name VARCHAR(255) NOT NULL
                   )""")

def create_table_Orders():
    return cursor.execute("""CREATE TABLE IF NOT EXISTS Orders(
                    order_id INT AUTO_INCREMENT PRIMARY KEY,
                    menu_item_id INT NOT NULL,
                    customer_id INT NOT NULL,
                    order_date DATE NOT NULL,
                    order_time TIME NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
                    FOREIGN KEY (menu_item_id) REFERENCES Menu(menu_item_id)
                   )""")

def update_Custormers(name):
    return cursor.execute(f"INSERT INTO Customers(Name) VALUES ('{name})")

def update_Orders(customer_id, order_date):
    return cursor.execute(f"INSERT INTO Orders(customer_id, order_date) VALUES ('{customer_id}', '{order_date}')")

