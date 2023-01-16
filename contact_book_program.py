from contact import Contact, Contact_View

#from contact import Contact_Record
from contact_repository import Contact_Repository
from contact_book_repository import create_contact
from contact_book_repository import delete_contact
from contact_book_repository import update_contact
from contact_book_repository import list_contact
from contact_book_repository import close
#from contact_book_repository import *



def action_chosen_from_input(chosen_action):
    if chosen_action == 1:
        create()
    elif chosen_action == 2:
        update()
    elif chosen_action == 3:
        delete()
    elif chosen_action == 4:
        list()
    elif chosen_action == 5:
        Contact_Repository.close()
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
    contact_to_add = Contact_View(contact_name, contact_city, contact_number,
        contact_email)
    Contact_Repository.create(contact_to_add)
    print("*************\nCreating contact was successful\n*************")
    contact_book_home_screen()


def delete():  # check if entry exist
    print("Enter the contact ID you wish to delete")

    #TODO make logic for retaining values if user input is blank ==== DONE
    cid = str(input())  #deviates from interface made on mermaid js
    if is_entry_null(cid):
        pass
        #contact object not used
        #contact = Contact_Repository.get_one(cid)
    else:
        print("Contact doesn't exist. Returning to home")
        contact_book_home_screen()

    Contact_Repository.delete(cid)
    print("*************\nDeleting contact was successful\n*************")
    contact_book_home_screen()


def update(): # check if entry exists 
    print("Enter the contact ID you wish to update")
    cid = str(input())  # need to check input
    # get_one()
    # if not 0 then continue
    if is_entry_null(cid):
        contact = Contact_Repository.get_one(cid)
    else:
        print("Contact doesn't exist. Returning to home")
        contact_book_home_screen()

    #TODO make logic for retaining values if user input is blank ==== DONE
    print("Enter the updated name (Leave blank if you wish to retain)")
    contact_name = input()
    if contact_name == '':
        contact_name = contact.name
    print("Enter the updated city (Leave blank if you wish to retain)")
    contact_city = input()
    if contact_city == '':
        contact_city = contact.city
    print("Enter the updated contact number (Leave blank if you wish to retain)")
    contact_number = input()
    if contact_number == '':
        contact_number = contact.contact_no
    print("Enter the updated email address (Leave blank if you wish to retain)")
    contact_email = input()
    if contact_email == '':
        contact_email = contact.email

    contact_to_update = Contact(cid, contact_name, contact_city,
        contact_number, contact_email)
    Contact_Repository.update(contact_to_update)
    print("*************\nUpdating contact was successful\n*************")
    contact_book_home_screen()
    
    

def is_entry_null(cid: int):
    contact = Contact_Repository.get_one(cid)
    if contact is None:
        return False
    else:
        return True




def list():
    print("Contact_ID | Name | City | Contact Number | Email Address")
    #list_contact()
    result = Contact_Repository.get_all()
    for contact in result:
        print("%s | %s | %s | %s | %s" %
            (contact.cid, contact.name, contact.city, contact.contact_no, contact.email))
    contact_book_home_screen()



if __name__ == "__main__":
    contact_book_home_screen()
    