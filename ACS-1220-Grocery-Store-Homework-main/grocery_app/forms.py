from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, NumberRange
from grocery_app.models import *

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
    
