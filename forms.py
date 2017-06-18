from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class RegistrationForm(FlaskForm):
    email = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('password', validators=[validators.DataRequired(), validators.Length(min=1, message="Please choose a password of at least 8 characters")])
    password2 = PasswordField('password2', validators=[validators.DataRequired(), validators.EqualTo('password', message='Passwords must match')])
    submit = SubmitField('submit', [validators.DataRequired()])

class LoginForm(FlaskForm):
    email = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('password', validators=[validators.DataRequired(), validators.EqualTo('password', message='Password is required')])
    submit = SubmitField('submit',[validators.DataRequired()])

class CompanyForm(FlaskForm):
    company_name = StringField('Company Name', validators=[validators.InputRequired()])
    address1 = StringField('Address Line 1', validators=[validators.InputRequired()])
    address2 = StringField('Address Line 2', validators=[validators.Optional()])
    #Must allow for international phone numbers
    phone = IntegerField('Phone Number', validators=[validators.Optional()])
    fax = IntegerField('Fax Numbers', validators=[validators.Optional()])
    email = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
    submit = SubmitField('submit', [validators.DataRequired()])

class IndentForm(FlaskForm):
    buyer_name = StringField('Buyer Name', validators=[validators.InputRequired()])
    buyer_address1 = StringField('Address Line 1', validators=[validators.InputRequired()])
    buyer_address2 = StringField('Address Line 2', validators=[validators.InputRequired()])
    buyer_city = StringField('Buyer City', validators=[validators.InputRequired()])
    buyer_country = StringField('Buyer Country', validators=[validators.InputRequired()])
    seller_name = StringField('Seller Name', validators=[validators.InputRequired()])
    seller_address1 = StringField('Seller Address Line 1', validators=[validators.InputRequired()])
    seller_address2 = StringField('Seller Address Line 2', validators=[validators.InputRequired()])
    seller_city = StringField('Seller City', validators=[validators.InputRequired()])
    seller_country = StringField('Seller Country', validators=[validators.InputRequired()])
    product_name = StringField('Product Name', validators=[validators.InputRequired()])
    product_qty = IntegerField('Product Quantity', validators=[validators.InputRequired()])
    unit = StringField('Unit', validators=[validators.InputRequired()])
    price = IntegerField('Product Price', validators=[validators.InputRequired()])
    pkg = StringField('Packaging', validators=[validators.InputRequired()])
    origin = StringField('Product Origin', validators=[validators.InputRequired()])
    load = StringField('Buyer Name', validators=[validators.InputRequired()])
    payment_type = StringField('Payment Type', validators=[validators.InputRequired()])
    shipment_port = StringField('Port of Shipment', validators=[validators.InputRequired()])
    bank_detail = StringField('Bank Routing Detail', validators=[validators.InputRequired()])
    days_at_port = StringField('Days at Port', validators=[validators.InputRequired()])
    insurance_by = StringField('Insurance Provided By', validators=[validators.InputRequired()])
    submit = SubmitField('submit', [validators.DataRequired()])
