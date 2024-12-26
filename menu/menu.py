import mysql.connector

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
                          Price Currency
                          )""")
    #return cursor.execute(f"CREATE TABLE {str} {final_column_tuple};")
