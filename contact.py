class Contact_Record:
    def __init__(self, name: str, city: str, contact_no: str, email: str):
        self.name = name
        self.city = city
        self.contact_no = contact_no
        self.email = email

class Contact(Contact_Record): #inherits Contact_Record
    def __init__(self, contact_id: int, name: str, city: str, contact_no: str, email: str):
        self.contact_id = contact_id
        Contact_Record.__init__ (self, name, city, contact_no, email)
        

        
# record_contact = Contact(0, 'pol', 'qc', 'asd', 'asd@gmail.com')
# print(record_contact.contact_id)
# print(record_contact.name)
# print(record_contact.city)
# print(record_contact.contact_no)
# print(record_contact.email)



#contactlist: list[Contact] = [contact1,contact2,contact3]

#print(contactlist)

# str_int = {'one':5, 'two':7}
# int_int = {2:5, 2:6}

# def sum_dict(var: dict[str,int]):
#     return sum (var[key] for key in var.keys())

# sum_dict(int_int)