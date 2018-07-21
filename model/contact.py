from sys import maxsize


class Contact:
    def __init__(self, id=None, firstname=None, lastname=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return "%s;%s;%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname

    def id_or_max(c):
        if c.id:
            return c.id
        else:
            return maxsize