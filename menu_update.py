import json

price = [5.99, 8.99, 9.99, 7.49, 10.49, 12.99, 11.49, 8.49, 6.99, 13.99, 14.99, 9.99, 12.49, 7.99, 8.49, 11.99, 14.99, 10.49, 12.49, 9.99, 7.49, 8.99, 13.99, 5.99, 7.99, 9.49, 6.99, 6.49, 8.49, 7.99, 8.99, 9.49, 7.99, 9.49, 8.99, 11.49, 8.49, 7.99, 9.49, 8.49, 6.99, 7.99, 19.99, 18.99, 14.49, 15.99, 16.99, 11.49, 12.99, 13.49, 9.99, 8.99, 14.99, 12.99, 10.99, 11.49, 12.49]
prices = []

for i in price:
    prices.append(round(i))

price_index = 0

with open("menu/menu.json", "r") as f:
    menu = json.load(f)

for heading in menu:
    if heading == "restaurant":
        continue

    else:
        for item in menu[heading]:
            if item != "Ordinary & Happy":
                for dishes in menu[heading][item]:
                    a = list(dishes.values())

                    a[2]=prices[price_index]
                    price_index += 1
                    for i in a:
                        dishes["name"] = a[0]
                        dishes["description"] = a[1]
                        dishes["Price"] = a[2]
        
            else:
                print("This")

with open("menu/menu.json", "w") as f:
    json.dump(menu, f, indent=4)


