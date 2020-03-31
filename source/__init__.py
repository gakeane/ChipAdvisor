
"""
We create the flask app as a package global variable by declaring it in the __init__.py module

Flask uses the jinja2 template engine which allows us to write code inside a template.
this code will be parsed by the jinja template engine.
"""

from flask import Flask

app = Flask(__name__)

# Sets a secret key for the WebApp, (prevents modified cookies and cross-stie request forgery)
app.config['SECRET_KEY'] = 'daff361285c114ce64ec984b3667df65'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
