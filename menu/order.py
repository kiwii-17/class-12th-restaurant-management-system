import json
from pyfiglet import Figlet
import inquirer

result = {}
dish_list = []


def heading_display(text):
     return Figlet(font='larry3d').renderText(text)

def result_update(dict):
     return result.update(dict)

def menu_category():
     menu_categories = []

     with open('menu/menu.json', 'r') as f:
          menu = json.load(f)

     for heading in menu:

          for item in menu[heading]:

               menu_categories = list(menu[heading].keys())
     
     return menu_categories

 
def menu_order_options(menu_categories= menu_category()): 
     menu_items = {}
     add_on = 0
     once = 0

     with open('menu/menu.json', 'r') as f:
          menu = json.load(f)

     for heading in menu:

          for item in menu[heading]:

               if menu[heading][item] == "Ordinary & Happy":
                    print(heading_display(menu[heading][item]))
                    
               else:
                    for dishes in menu[heading][item]:
                         dish_list.append(f"{dishes['name']}")

                    menu_items.update({menu_categories[add_on]: dish_list})
                    add_on += 1


               dish_list = []

     return menu_items


def order_report(menu_categories= menu_category(), menu_items= menu_order_options()):
     order_id = 1

     question1 = [
          inquirer.Text(
               "name",
               message= "Please enter your name"
          ),
     ]

     info1 = inquirer.prompt(question1)
     result_update(info1)

     question2 = [
          inquirer.List(
               f"category{order_id}",
               message= "What would you like to eat",
               choices= menu_categories
          )
     ]

     info2 = inquirer.prompt(question2)
     result_update(info2)


     question3 = [
          inquirer.List(
               f"order{order_id}",
               message= "What would you like to order",
               choices= menu_items[result[f"category{order_id}"]]
          )
     ]

     info3 = inquirer.prompt(question3)
     result_update(info3)

     confirm_question = [
          inquirer.Confirm(
               "confirm",
               message= "Would you like to order again?"
          )
     ]

     info4 = inquirer.prompt(confirm_question)
     result_update(info4)

     while result["confirm"] == True:
          order_id += 1

          question2 = [
               inquirer.List(
                    f"category{order_id}",
                    message= "What would you like to eat",
                    choices= menu_categories
               )
          ]

          info2 = inquirer.prompt(question2)
          result_update(info2)

          question3 = [
               inquirer.List(
                    f"order{order_id}",
                    message= "What would you like to order",
                    choices= menu_items[result[f"category{order_id}"]]
               )
          ]

          info3 = inquirer.prompt(question3)
          result_update(info3)

          confirm_question = [
               inquirer.Confirm(
                    "confirm",
                    message= "Would you like to order again?"
               )
          ]

          info4 = inquirer.prompt(confirm_question)
          result_update(info4)

     return result

