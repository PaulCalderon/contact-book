from contact import Contact
from contact import Contact_Record
from contact_book_repository import create_contact
from contact_book_repository import delete_contact
#from contact_book_repository import *


def action_chosen_from_input(chosen_action):
    if chosen_action == 1:
        create()
    elif chosen_action == 2:
        contact_book_update_contact()
    elif chosen_action == 3:
        delete()
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


def create():
    print("Enter the name:")
    contact_name = input()
    print("Enter the city:")
    contact_city = input()
    print("Enter the contact number:")
    contact_number = input()
    print("Enter the email_address:")
    contact_email = input()
    contact_to_add = Contact_Record(contact_name, contact_city, contact_number,
        contact_email)
    create_contact(contact_to_add)
    print("*************\nCreating contact was successful\n*************")


def delete():
    print("Enter the contact ID you wish to delete")
    delete_contact(int(input()))

if __name__ == "__main__":
    contact_book_home_screen()
    