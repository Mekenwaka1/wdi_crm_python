class Contact:

  contacts = []
  next_id = 1

  def __init__(self, first_name, last_name, email, note):
    """This method should initialize the contact's attributes"""
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.note = note
    self.id = Contact.next_id 
    Contact.next_id += 1
    
  def __str__(self):
    return f"{self.first_name} {self.last_name}"

  def __repr__(self):
    return str(self)

  def update(self, attribute, new_value):
    """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    """
    setattr(self, attribute, new_value)
    return self

  def full_name(self):
    """Returns the full (first and last) name of the contact"""
    return f"{self.first_name} {self.last_name}"

  def delete(self):
    """This method should delete the contact
    HINT: Check the Array class docs for built-in methods that might be useful here
    """
    Contact.contacts.remove(self)
  
  @classmethod
  def create(cls, first_name, last_name, email, note):
    """This method should call the initializer,
    store the newly created contact, and then return it
    """
    new_contact = Contact(first_name, last_name, email, note)
    print(new_contact)


    cls.contacts.append(new_contact)
    return new_contact

  @classmethod
  def all(cls):
    """This method should return all of the existing contacts"""
    return Contact.contacts 

  @classmethod
  def find(cls, id):
    """ This method should accept an id as an argument
    and return the contact who has that id
    """
    for contact in cls.contacts:
      if contact.id == id:
        return contact

  @classmethod
  def find_by(cls, attribute, value):
    """This method should work similarly to the find method above
    but it should allow you to search for a contact using attributes other than id
    by specifying both the name of the attribute and the value
    eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    """
    for contact in cls.contacts:
      if getattr(contact, attribute) == value:
        return contact

  @classmethod
  def delete_all(cls):
    """This method should delete all of the contacts"""
    return cls.contacts.clear()

# Feel free to add other methods here, if you need them.

contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
contact2 = Contact.create('Fred', 'Ngo', 'fred@bitmakerlabs.com', 'Loves his cat Corey')
contact3 = Contact.create('John', 'Smith', 'johnsmith@gmail.com', 'Loves Cars')
print(len(Contact.contacts))
print(contact1.id)
print(contact2.id)

print(contact1)
contact1.update("first_name", "Bob")
print(contact1)
# contact1.update("last_name", "Baker")
# print(contact1)


# contacts  = [{
#         email: "bettymakes@bitmakerlabs.com",
#         first_name: "Bob",
#         contact_id: 23,
#         last_name: "Bob",
#         note: "Loves Pokemon"
#     },{
#         py/object: "__main__.Contact",
#         email: "bettymakes@bitmakerlabs.com",
#         first_name: "Bob",
#         contact_id: 83,
#         last_name: "Bob",
#         note: "Loves Pokemon"
#     }
# ]
# print("Full name:", contact1.full_name())
# print("Before delete: ", Contact.contacts)
# contact1.delete()
# print("After delete: ", Contact.contacts)
# print("Test find_by: ", Contact.find_by("first_name", "Fred"))