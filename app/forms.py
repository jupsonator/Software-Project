from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, DateField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=150)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class ExpenseForm(FlaskForm):
    name = StringField('Expense Name', validators=[InputRequired()])
    amount = FloatField('Amount', validators=[InputRequired()])
    date = DateField('Date', format='%Y-%m-%d')
    submit = SubmitField('Add Expense')