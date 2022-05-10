from unicodedata import category
from flask import redirect, render_template,url_for
from . import main
from ..models import Pitch
from .forms import PitchForm
from flask_login import login_required

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

@main.route('/pitches/entertainment_pitches')
def entertainment_pitches():

    pitches = Pitch.get_pitches('entertainment')

    return render_template("entertainment_pitches.html", pitches = pitches)

@main.route('/pitch/new',methods=["GET","POST"])
@login_required
def new_pitch():
     pitch_form = PitchForm()
     if pitch_form.validate_on_submit():
         title=pitch_form.title.data
         text=pitch_form.text.data
         category=pitch_form.category.data

         new_pitch=Pitch(title=title,text=text,category=category)
         new_pitch.save_pitch()
         return redirect(url_for('.index'))

     return render_template('new_pitch.html',pitch_form=pitch_form)

    

