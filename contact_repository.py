import sqlite3
from typing import Optional
from contact import Contact
from contact import Contact_View

#TODO implement connection manager for opening and closing database connection

contact_book_database_connection = sqlite3.connect("ContactBook.db") 
database_cursor = contact_book_database_connection.cursor()

class Contact_Repository:
    @staticmethod
    def create(contact: Contact_View):
        database_cursor.execute("INSERT INTO Contact_Book (cid, name, \
        city_address, contact_number, email_address) VALUES(?,?,?,?)",
            [contact.name, contact.city, contact.contact_no, contact.email])
        contact_book_database_connection.commit()

    @staticmethod
    def update(contact: Contact):
        database_cursor.execute(
        """
        UPDATE Contact_Book
            SET name = ?,
            city_address = ?,
            contact_number = ?,
            email_address = ?
        WHERE contact_id = ?
        """
        , [contact.cid, contact.name, contact.city, contact.contact_no, contact.email]
        )
        contact_book_database_connection.commit()

    @staticmethod
    def delete(cid: int):
        database_cursor.execute("DELETE FROM Contact_Book WHERE contact_id = ?", [cid])
        contact_book_database_connection.commit()

    @staticmethod
    def get_all(self) -> list[Contact]:
        contact_list: list[Contact] = []
        result = database_cursor.execute("SELECT contact_id, name, \
        city_address, contact_number, email_address FROM Contact_Book ORDER BY contact_id")
        for row in result:
            contact_result = Contact(row[0], row[1], row[2], row[3], row[4])
            contact_list.append(contact_result)
        return contact_list

    @staticmethod
    def get_one(cid: int) -> Optional[Contact]:
        cursor = database_cursor.execute("SELECT * FROM Contact_Book WHERE contact_id = ?", cid)
        result = cursor.fetchone()
        
            #print(row)
        # for row in database_cursor.execute("SELECT * FROM Contact_Book WHERE contact_id = %s", cid):
        #     print(row)
        # for row in database_cursor.execute("SELECT contact_id, name, \
        # city_address, contact_number, email_address FROM Contact_Book ORDER BY contact_id"):
        #     print ("%s | %s | %s | %s | %s" % (row[0], row[1], row[2], row[3], row[4]))
        # print(result[0])
        #if(len(result) == 0):
        if result is None:
            return None

        contact = Contact(result[0], result[1], result[2], result[3], result[4])
        return contact