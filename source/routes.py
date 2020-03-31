
"""

"""

# This imports from __init__.py
from source import app

from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect

from source.forms import RegistrationForm
from source.forms import LoginForm

@app.route("/")
@app.route("/home")
def home():
    """ Loads the main index page """

    return render_template('home_page.html')


@app.route("/about")
def about():
    """ Loads the about page """

    return render_template('about_page.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()


    # Execute form validation on retrival of a POST request
    if form.validate_on_submit():
        flash("Account created for {}".format(form.username.data), 'success')
        return redirect(url_for('home'))


    return render_template('register_page.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # Execute form validation on retrival of a POST request
    if form.validate_on_submit():

        # Successful Login
        if form.email.data =='admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in", 'success')
            return redirect(url_for('home'))

        # Unsuccessful Login
        else:
            flash("Login failed. Check username and password", 'danger')

    return render_template('login_page.html', title='Login', form=form)

@app.route("/login", methods=['GET', 'POST'])
def account():
    """ Allows user to update their account profile """

    return render_template('account_page.html', title='Account')
