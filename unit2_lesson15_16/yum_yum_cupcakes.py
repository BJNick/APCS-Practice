"""
Mykyta S.
yum_yum_cupcakes.py
Simulates a cupcake business using a list
"""

import random


def print_menu(cupcake_list):
    """Prints out the cupcake menu"""
    print("Our Menu:")
    count = 0
    # Print out the menu
    for item in cupcake_list:
        count += 1
        itemName = item[0]
        itemQuantity = item[1]
        print("#%d\t%s - %d in stock" % (count, itemName, itemQuantity))
    print()


def process_customer(cupcake_list):
    """Receives input from the user and processes their request"""

    requested_item = input("Which item would you like? ").lower().strip()

    if (len(requested_item.strip()) == 0):
        print("Sorry, we don't have any of that.\n")
        return

    # If it's a number find the name in the list
    if (requested_item < "A"):
        requested_item = cupcake_list[int(requested_item) - 1][0]

    # Ask how many of that item they want
    requested_count = int(input("How many would you like? "))

    # Loop through the list and see if the order is possible
    item_found = False

    for item in cupcake_list:
        if item[0] == requested_item:
            item_found = "True"
            if item[1] >= requested_count:
                item[1] -= requested_count
                print("Here you go, %d %s cupcakes." % (
                requested_count, requested_item))
            else:
                print("Sorry, we don't have enough %s cupcakes." \
                      % requested_item)

    if not item_found:
        print("Sorry, it doesn't seem like we have any %s cupcakes." \
              % requested_item)
    print()


def check_stock(cupcake_list):
    """Checks the cupcake amounts and bakes some more if less than 3"""
    print("Taking a look at the stock...")
    for item in cupcake_list:
        if item[1] < 3:
            need_to_bake = 3 - item[1]
            item[1] += need_to_bake
            print("Baking %d more %s cupcakes, now there's %d." \
                  % (need_to_bake, item[0], item[1]))
        else:
            print("We have %d %s cupcakes already." % (item[1], item[0]))
    print()


def drop_a_cupcake(cupcake_list):
    """Drops a random cupcake and throws it away"""
    print("Whoops!")
    # Get a random cupcake that is in stock
    random_index = random.randint(0, len(cupcake_list)-1)
    while cupcake_list[random_index][1] <= 0:
        random_index = random.randint(0, len(cupcake_list)-1)
    dropped_cupcake = cupcake_list[random_index]
    print("I dropped a %s cupcake, I'm so sorry!" % dropped_cupcake[0])
    # Remove it from stock
    dropped_cupcake[1] -= 1
    print("Now there's %d of them left." % dropped_cupcake[1])
    print()


if __name__ == "__main__":

    yum_yum_cupcakes = [["chocolate mousse", 3], ["vanilla creme", 0],
                      ["strawberry fluff", 2], ["blueberry mousse", 2]]

    print_menu(yum_yum_cupcakes)

    drop_a_cupcake(yum_yum_cupcakes)

    process_customer(yum_yum_cupcakes)

    check_stock(yum_yum_cupcakes)

    print_menu(yum_yum_cupcakes)

