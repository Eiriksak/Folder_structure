from project import db

# Lager en klasse for table = banan
class Bananer(db.Model):
    __tablename__ = 'bananer'

# Setter hvilke kolonner vi skal ha og eventuelle constraints
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String)

# Lager en konstruktør for når vi skal lage og sette inn ting i tabellen
# I tilfelle med autoincrement id trenger vi ikke ha den her siden sql automatisk oppdaterer denne selv
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return '<title {}'.format(self.name)




class Epler(db.Model):
    __tablename__ = 'epler'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)

    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return '<title {}'.format(self.name)