from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')

class Contact(Model):
  first_name = CharField()
  last_name = CharField()
  email = CharField()
  note = TextField()

  class Meta:
    database = db

  def full_name(self):
    return "{} {}".format(self.first_name, self.last_name)

db.connect()
db.create_tables([Contact])


# Using CRUD operations.

# Create two entries in the db
contact1 = Contact.create(
      first_name="Betty",
      last_name="Maker",
      email="bettymakes@bitmakerlabs.com",
      note="Loves Pokemon"
    )

contact2 = Contact.create(
      first_name="Fred",
      last_name="Ngo",
      email="fred@bitmakerlabs.com",
      note="Loves his cat Corey"
    )

# Updates an instance in the db with the id: 30
contact_to_update = Contact.select().where(Contact.id == 30).get()
contact_to_update.first_name = "Lazio"
contact_to_update.save()

# Delete an instance in the db with the id: 31
contact_to_delete = Contact.select().where(Contact.id == 31).get()
contact_to_delete.delete_instance()
