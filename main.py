#Define some basic data for your kitchen inventory. 
available_eggs = 1
available_flour = 2
available_sugar = 3

#Define a function to check if you have enough ingredients to make a cake.
def check_kitchen_stock():
    total_items = available_eggs +  available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

#Display the current kitchen inventory.
check_kitchen_stock()

#Use a requested number of eggs and return the remaining count.
def use_eggs(available_eggs, eggs_to_use):
    if eggs_to_use > available_eggs:
        print("The kitchen does not have enough eggs.")
        return available_eggs
    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use

#Demonstrate using one egg from the available stock.
use_eggs(available_eggs, 1)

#Make a fried egg when possible and return the remaining egg count.
def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1
    #Use one egg if available; otherwise report that frying is not possible.
    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print("Made a fried egg. Yummy!")
    else:
        print("Could not make a fried egg. Not enough eggs!")
    return available_eggs

#Update the global egg inventory with the remaining count.
available_eggs = make_fried_egg(available_eggs)
