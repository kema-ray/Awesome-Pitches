from flask import render_template
from . import main
from ..models import Pitch

@main.route('/')
def index():

    title = 'Awesome Pitches'

    # marketing_pitches = Pitch.get_pitches('')
    business_pitches = Pitch.get_pitches('business')
    entertainment_pitches = Pitch.get_pitches('entertainment')
    puns_pitches = Pitch.get_pitches('puns')
    
    return render_template('index.html',title = title,business=business_pitches,entertainment=entertainment_pitches,
    puns=puns_pitches)

@main.route('/pitches/business_pitches')
def business_pitches():

    pitches = Pitch.get_pitches('business')

    return render_template("business_pitches.html", pitches = pitches)

