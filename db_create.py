from project import db

# drop all of the existing database tables
db.drop_all()

# create the database and the database table
db.create_all()

# commit the changes
db.session.commit()