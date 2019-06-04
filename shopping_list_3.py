import os

shopping_list = []


def clear_screen():
    """Looks at system;
    Runs 'nt' for all modern versions of Windows;
    Runs 'clear' if on a non-Windows computer;
    """
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    """Clears screen, then shows help menu"""
    clear_screen()
    print("What should we pick up at the store? Enter items below.")
    print("""
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'MOVE' to move an item on your list.
Enter 'REMOVE' to delete an item from your list.
Enter 'CLEAR' to clear your list.
Enter 'DONE' or 'QUIT' to stop adding items.
""")


def move_item():
    """Asks user for item number to move, moves it to specified location"""
    if len(shopping_list) > 1:
        show_list()
        while True:
            try:
                item_to_move = shopping_list.pop((int(input("""
                What item number would you like to move?\n> """)))-1)
                break
            except ValueError:
                print("Please enter a number")
                continue
            except IndexError:
                print("Please enter a valid number")
                continue
        shopping_list.insert((int(input("""
        What position should {} go in?\n>
        """.format(item_to_move)))-1), item_to_move)
        show_list()
    else:
        print("Your list has too few items to move!")


def add_to_list(item):
    """Adds inputed item to list in specified location"""
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)

    show_list()


def clear_list():
    """Asks for a confirm, then clears all items from list"""
    confirm_clear = input("""
    Are you sure you would like to clear your list?
    [y]es or [n]o
    >""")
    if confirm_clear.upper() == "Y":
        while shopping_list:
            del shopping_list[0]
        show_list()
    if confirm_clear.upper() == "N":
        print("Gotcha!")
        show_list()


def show_list():
    """Prints out entire list to screen"""
    clear_screen()
    print("Here's your list:")

    for index, item in enumerate(shopping_list, start=1):
        print("{}. {}".format(index, item))
    print("-"*10)


def remove_from_list():
    """Removes an item from the list by name"""
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()

show_help()
while True:
    new_item = input("> ")

    if new_item.upper() == "DONE" or new_item.upper() == "QUIT":
            break
    elif new_item.upper() == "HELP":
            show_help()
            continue
    elif new_item.upper() == "SHOW":
            show_list()
            continue
    elif new_item.upper() == "REMOVE":
            remove_from_list()
            continue
    elif new_item.upper() == "MOVE":
            move_item()
            continue
    elif new_item.upper() == "CLEAR":
            clear_list()
            continue
    else:
        add_to_list(new_item)

show_list()
