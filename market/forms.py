from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,Email,EqualTo,DataRequired,ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! please try different username')
    def validate_email(self,email_to_check):
        email=User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exists! please try different Email Address')
    username=StringField(label='User Name',validators=[Length(min=2,max=60),DataRequired()])
    email=StringField(label='Email Address',validators=[Email(),DataRequired()])
    pass1=PasswordField(label='Password',validators=[Length(min=6),DataRequired()])
    pass2=PasswordField(label='Confirm Password',validators=[EqualTo('pass1'),DataRequired()])
    submit=SubmitField(label='Create Account')
class LoginForm(FlaskForm):
    username=StringField(label='User Name',validators=[DataRequired()])
    
    password=PasswordField(label='Password',validators=[DataRequired()])
    submit=SubmitField(label='sign in')
class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')
class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')