from datetime import datetime
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import DataRequired, NumberRange, ValidationError


class CheckoutForm(FlaskForm):
    name = StringField('Card Holder Name', validators=[DataRequired()])
    card_no = IntegerField('Card Number', validators=[])
    expiry = StringField('Expiry', validators=[DataRequired()])
    cvv = PasswordField('CVV/CVV2', validators=[DataRequired()])
    submit = SubmitField('Pay')

    def validate_card_no(self, card_no):
        if len(str(card_no.data)) != 16:
            raise ValidationError('Credit/Debit Card Number Invalid. (should be of 16 digits)')

    def validate_expiry(self, expiry):
        curr_month = int(datetime.now().month)
        curr_year = int(datetime.now().year)
        mth, yr = [int(i.strip()) for i in expiry.data.split("/")]
        if curr_year < yr:
            return
        if curr_year == yr:
            if curr_month <= mth and mth <= 12:
                return
        raise ValidationError("Your Card's Exipry date is incorrect")

    def validate_cvv(self, cvv):
        if len(str(cvv.data)) != 3 and len(str(cvv.data)) != 4:
            raise ValidationError('CVV should be of 3 or 4 digit')
