from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():

    return 'Hello World Again'


@main.route('/profile')
def profile():

    return 'Profile Page here'