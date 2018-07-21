from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    contacts = db.get_contact_list()
    for c in contacts:
        print(c)
    print(len(contacts))
finally:
    db.destroy()