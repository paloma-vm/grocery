from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, NumberRange, ValidationError
from grocery_app.extensions import app, db, bcrypt
from grocery_app.models import User, GroceryItem, GroceryStore, ItemCategory


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    # - title - StringField
    # - address - StringField
    # - submit button
    title = StringField('Store Title',
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your title needs to be betweeen 3 and 80 chars")
            ])
    address = StringField('Store Address',
        validators=[
            DataRequired(), 
            Length(min=5, max=80, message="Your address needs to be betweeen 5 and 80 chars")
            ])
    submit = SubmitField('Submit')
    
class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    name = StringField('Grocery Item Name',
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your item name needs to be betweeen 3 and 80 chars")
            ])
    price = FloatField('Item Price')
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo URL',
        validators=[
            DataRequired(),
            Length(min=5, max=80, message="Your Photo URL needs to be betweeen 5 and 80 chars")
            ])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit = SubmitField('Submit')
    
# Login #####################################

class SignUpForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('No user with that username. Please try again.')

    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not bcrypt.check_password_hash(
                user.password, password.data):
            raise ValidationError('Password doesn\'t match. Please try again.')
