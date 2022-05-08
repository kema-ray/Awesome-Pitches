from flask import render_template
from . import main

@main.route('/')
def index():

    title = 'Awesome Pitches'
    return render_template('index.html',title = title)