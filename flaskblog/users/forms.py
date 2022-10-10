from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, \
    FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, \
    ValidationError

from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('username already exists! pls choose '
                                  'another one')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('email already exists! pls choose another '
                                  'one')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed([
        'jpg', 'png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if current_user.username != username.data:
            if User.query.filter_by(username=username.data).first():
                raise ValidationError('username already exists! pls choose '
                                      'another one')

    def validate_email(self, email):
        if current_user.email != email.data:
            if User.query.filter_by(email=email.data).first():
                raise ValidationError(
                    'email already exists! pls choose another '
                    'one')