
"""
The two databases have a one to many relationship
A single User can have multiple posts, however each most can only have one User.

"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from source import app

db = SQLAlchemy(app)


class User(db.Model):
    """ Class for creating a user table in a SQL database """

    # class variables
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        """ String representation of class """
        return "User: {}, Email: {}, Image: {}".format(self.username, self.email, self.image)


class Database():
    """ Class for administering the database """
