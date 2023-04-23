from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from missingprofessor.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Username"})
    email = StringField('Email',
                        validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password',validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('An account already exists with this Email.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()],  render_kw={"placeholder": "Email"})
    password = PasswordField('Password',validators=[DataRequired()], render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class Unlocklab(FlaskForm):
    answer = StringField('Enter Answer',
                           validators=[DataRequired()],render_kw={"placeholder": "Enter Password"})
    submit = SubmitField('ENTER')
    def validate_answer(self, answer):
        answers = ["cooper"]
        ans = answer.data.lower()
        if ans not in answers:
            raise ValidationError('Wrong Answer')
