from database import resources, MENU


is_on = True
profit = 0

def is_suff(order_name):
    for item in order_name:
        if resources[item] >= order_name[item]:
            return True
        else:
            print(f"Not enough {item}.")


def process_coins():
    print("Please, insert your coins:")
    total = 0
    total +=  int(input("How many pennys:"))*0.01
    total += int(input("How many nickels:"))*0.05
    total += int(input("How many dimes:"))*0.1
    total += int(input("How many quartes:"))*0.25
    return total
     
    
def transaction_suc(payment, drink_cost):
        if payment >= drink_cost:
            global profit 
            profit += drink_cost   
            exchange = round(payment - drink_cost,2)
            print(f"Here's your exchange of {exchange}")
            return True
        else:
            print("Sorry, not enought money.")
        return False

def make_coffee(drink_name , order_ingredients):  
    for item in order_ingredients:
            resources[item] -= order_ingredients[item] 
    print(f"Here's your {drink_name}. Enjoy!")




     


while is_on:
    choice = input(f"What would you like (espresso/latte/cappuccino): ") 

    if choice == 'report':
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}ml")
        print(f"Money: ${profit}")
    elif choice == 'off':
        is_on = False
    else:
        drink = MENU[choice]
        if is_suff(drink["ingredients"]):
            payment = process_coins()
            if transaction_suc(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

            


        
        


    