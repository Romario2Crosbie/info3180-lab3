from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(min=6, max=120)])
    subject = StringField('subject', validators=[DataRequired(), Length(min=1, max=100)])
    message = TextAreaField('message', validators=[DataRequired(), Length(min=10, max=500)])