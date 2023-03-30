from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, ValidationError,PasswordField,IntegerField,SubmitField
from wtforms.validators import DataRequired, Email,Length,EqualTo


class RegisterForm(FlaskForm):
    full_name = StringField('name', validators=[DataRequired(),Length(min=6, max= 100)])
    email = EmailField('email', validators=[DataRequired(), Email(),Length(min=2, max= 200)])
    password = PasswordField('pasword', validators=[DataRequired(),Length(min=6, max= 200)])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    

class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),Length(min=6, max= 100)])
    
    
class ContactForm(FlaskForm):
    full_name = StringField('name', validators=[DataRequired(),Length(min=6, max= 200)])
    email = EmailField('email', validators=[DataRequired(), Email(),Length(min=6, max= 200)])
    message = TextAreaField('message', validators=[DataRequired()])
    