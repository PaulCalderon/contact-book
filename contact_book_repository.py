import sqlite3
from datetime import date


contact_book_database_connection = sqlite3.connect("ContactBook.db")
database_cursor = contact_book_database_connection.cursor()  
#calls and assigns database cursor to database_cursor
database_cursor.execute(
    "CREATE TABLE if not exists Contact_Book(contact_id INTEGER primary key, \
    name CHAR NOT NULL, city_address CHAR, contact_number CHAR, email_address CHAR)" 
    )  #currently not storing creation date of contact


class ContactBookRepository:

    def update_and_commit_to_database_name(self, update_list_values):
        database_cursor.execute("UPDATE Contact_Book SET name = ? \
            WHERE contact_id = ?", update_list_values)

    def update_and_commit_to_database_city_address(self, update_list_values):
        database_cursor.execute("UPDATE Contact_Book SET city_address = ? \
            WHERE contact_id = ?", update_list_values)

    def update_and_commit_to_database_contact_number(self, update_list_values):
        database_cursor.execute("UPDATE Contact_Book SET contact_number = ? \
            WHERE contact_id = ?", update_list_values)

    def update_and_commit_to_database_email_address(self, update_list_values):
        database_cursor.execute("UPDATE Contact_Book SET email_address = ? \
            WHERE contact_id = ?", update_list_values)

contact_book_repository = ContactBookRepository()


def contact_book_create_contact():
    print("Enter the name:")
    tuple_for_database_insert = input(),  #might actually not be a tuple
    print("Enter the city:")
    tuple_for_database_insert += input(),
    print("Enter the contact number:")
    tuple_for_database_insert += input(),
    print("Enter the email_address:")
    tuple_for_database_insert += input(),
    database_cursor.execute("INSERT INTO Contact_Book (name, city_address, \
        contact_number, email_address) VALUES(?,?,?,?)",
        tuple_for_database_insert)
    contact_book_database_connection.commit()
    print("*************\nCreating contact was successful\n*************")


def contact_book_delete_contact():
    print("Enter the contact ID you wish to delete")
    id_to_be_deleted = str(input())
        #could make code to confirm the contact to be deleted
    database_cursor.execute("DELETE FROM Contact_Book WHERE contact_id = ?", 
        id_to_be_deleted)
    contact_book_database_connection.commit()
    pass


def contact_book_update_contact():
    print("Enter the contact ID you wish to update")
    id_to_be_updated = str(input())
        #could make code to feedback the name of the contact selected to be updated
    print("Enter the updated name (Leave blank if you wish to retain)")
    updated_name = str(input())
    # tuple_for_formatted_database_update = []
    if updated_name != '':
        list_for_database_update = [updated_name]
        list_for_database_update.append(id_to_be_updated)
        contact_book_repository.update_and_commit_to_database_name(list_for_database_update)  #should I assign 'name to a variable?
    print("Enter the updated city (Leave blank if you wish to retain)")
    updated_city = str(input())
    if updated_city != '':
        list_for_database_update = [updated_city]
        list_for_database_update.append(id_to_be_updated)
        contact_book_repository.update_and_commit_to_database_city_address(list_for_database_update)  
    print("Enter the updated contact number (Leave blank if you wish to retain)")
    updated_contact_number = str(input())
    if updated_contact_number != '':
        list_for_database_update = [updated_contact_number]
        list_for_database_update.append(id_to_be_updated)
        contact_book_repository.update_and_commit_to_database_contact_number(list_for_database_update)  
    print("Enter the updated email address (Leave blank if you wish to retain)")
    updated_email_address = str(input())
    if updated_email_address != '':
        list_for_database_update = [updated_email_address]
        list_for_database_update.append(id_to_be_updated)
        contact_book_repository.update_and_commit_to_database_email_address(list_for_database_update)     
    contact_book_database_connection.commit()
    print("*************\nCreating contact was successful\n*************")


def contact_book_list_contact():
    for row in database_cursor.execute("SELECT contact_id, name, city_address, contact_number, email_address FROM Contact_Book ORDER BY contact_id"):
        print(row)
    #print()
#pass

def contact_book_close():
    contact_book_database_connection.close()

