from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[InputRequired()])
    text = TextAreaField('Text',validators=[InputRequired()])
    category = SelectField('Type',choices=[('business','Business pitch'),('entertainment','Entertainment pitch'),('puns','Puns pitch')],validators=[InputRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio',validators = [InputRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment:',validators=[InputRequired()])
    submit = SubmitField('Submit')