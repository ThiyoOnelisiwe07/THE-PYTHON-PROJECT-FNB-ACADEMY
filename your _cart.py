# create a shopping cart programme that will continuously ask the user for food product and the price of that product
# Have an exit clause if the user wishes to stop adding more things to their cart
# At the end show the food items and the total cost to the user

foods = []      # list to store food names
prices = []     # list to store their prices
total = 0       # running total

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        
        # 1️⃣ append to the correct list
        foods.append(food)
        prices.append(price)
        
        # 2️⃣ update the running total only once
        total += price
        
        print("-----YOUR CART-----")
        for food in foods:
            print(food , end= "")
            
        print("/n")
        print(f"Your total is: R{total:.2f}")   # show two decimal places
