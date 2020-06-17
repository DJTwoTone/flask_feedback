from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Optional, Email, Length
import email_validator

class RegisterForm(FlaskForm):
    """A form for registering"""

    username = StringField("Username", validators=[InputRequired(), Length(min=5, max=20, message="Please use between 5 and 20 characters for your username")])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=10, max=30, message="Please pick a stronger password")])
    email = StringField("Email Address", validators=[InputRequired(), Email()])
    first_name = StringField("Your First Name", validators=[InputRequired(), Length(min=1, max=30, message="We are sorry but your first name will not fit in our database")])
    last_name = StringField("Your Last Name", validators=[InputRequired(), Length(min=1, max=30, message="We are sorry but your first name will not fit in our database")])

class LoginForm(FlaskForm):
    """A form for logging in"""
    username = StringField("Username", validators=[InputRequired(), Length(min=5, max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=10, max=30)])

class FeedbackForm(FlaskForm):
    """A form for adding feedback"""

    title = StringField("Title", validators=[InputRequired(), Length(min=5, max=50)])
    content = StringField("Feedback", validators=[InputRequired()])
