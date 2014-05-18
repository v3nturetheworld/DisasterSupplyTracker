"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators
from wtforms.ext.appengine.ndb import model_form

from .models import ExampleModel


class ClassicExampleForm(wtf.Form):
    example_name = wtf.TextField('Name', validators=False)
    example_description = wtf.TextAreaField('Description', validators=False)

# App Engine ndb model form example
ExampleForm = model_form(ExampleModel, wtf.Form, field_args={
    'example_name': "Test",
    'example_description': "Test12",
})
