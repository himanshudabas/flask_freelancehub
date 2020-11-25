from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField('Service Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    price = IntegerField('Price', validators=[NumberRange(min=0, max=10000)])
    submit = SubmitField('Post')
