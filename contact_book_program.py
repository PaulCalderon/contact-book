from datetime import date
from contact_book_repository import *


def action_chosen_from_input(chosen_action):
    if chosen_action == 1:
        contact_book_create_contact()
    elif chosen_action == 2:
        contact_book_update_contact()
    elif chosen_action == 3:
        contact_book_delete_contact()
    elif chosen_action == 4:
        contact_book_list_contact()
    elif chosen_action == 5:
        contact_book_close()  
        exit()
    else:
        print("\nAction chosen was invalid\n")


def contact_book_home_screen():
    print("\nWelcome to your contact book.")
    print("What would you like to do?")
    print("1. Create contact")
    print("2. Update contact")
    print("3. Delete contact")
    print("4. List contact")
    print("5. Exit\n")
    print("Enter the number of the action you wish to perform: ")
    action_chosen_from_input(int(input()))
    contact_book_home_screen()


if __name__ == "__main__":
    contact_book_home_screen()
    