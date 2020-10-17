from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

# create signup route

@auth.route('/signup')
def signup():
    return 'This is sign-up page'

# create login route

@auth.route('/login')
def login():
    return 'This is the login page'

@auth.route('/logout')
def logout():
    return 'You are logged out'

