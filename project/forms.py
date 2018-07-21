"""Flask forms."""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    """Form for user queries."""
    query = StringField('Query', validators=[DataRequired()])
    submit = SubmitField('Search')
