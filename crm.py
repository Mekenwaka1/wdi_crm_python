from contact import Contact
import sys

class CRM:

  crm_contacts = []

  def main_menu(self):

    while True:
      self.print_main_menu()
      user_selected = int(input())
      self.call_option(user_selected)

  def print_main_menu(self):

    print('[1] Add a new contact')
    print('[2] Modify an existing contact')
    print('[3] Delete a contact')
    print('[4] Display all the contacts')
    print('[5] Search by attribute')
    print('[6] Exit')
    print('Enter a number: ')

  def call_option(self, user_selected):

    if user_selected == 1:
      self.add_new_contact()
    elif user_selected == 2:
      self.modify_existing_contact()
    elif user_selected == 3:
      self.delete_contact()
    elif user_selected == 4:
      self.display_all_contacts()
    elif user_selected == 5:
      self.search_by_attribute()
    elif user_selected == 6:
      self.exit()


  # def add_new_contact(self):
  def add_new_contact(self):

    print('Enter First Name: ')
    first_name = input()

    print('Enter Last Name: ')
    last_name = input()

    print('Enter Email Address: ')
    email = input()

    print('Enter a Note: ')
    note = input()

    new_contact = Contact.create(first_name, last_name, email, note)
    print(new_contact)
    print(Contact.contacts)


  # def modify_existing_contact(self):
  def modify_existing_contact(self):

    print('What would you like to Modify?')
    print('Enter ID: ')
    id = input()
    contact = Contact.find(id)

    print('What attribute would you like to change? Enter first_name, last_name, email or note')
    choice = input()

    print(f'Enter New {choice}: ')
    new_value = input()

    contact.update(choice, new_value)

    print(Contact.contacts)


  # def delete_contact(self):
  def delete_contact(self):
    print('What contact would you like to Delete?')
    print('Enter ID: ')
    self.id = input()
    Contact.delete(self)


  # def display_all_contacts(self):
  def display_all_contacts(self):
    for contact in Contact.all():
      print(contact)


  # def search_by_attribute(self):
  def search_by_attribute(self):
    print('How would you like to search the contact list? Enter id, first_name, last_name, email or note')
    search_attribute = input()


    print(f'Please enter new {search_attribute}')
    new_value = input()
    Contact.find_by(search_attribute, new_value)


  def exit(self):
      sys.exit()

    
a_crm_app = CRM()
a_crm_app.main_menu()