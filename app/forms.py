from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, DateField, SelectField
from wtforms.validators import InputRequired, Length, DataRequired

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4, max=150)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class ExpenseForm(FlaskForm):
    name = StringField('Expense Name', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Leisure', 'Leisure'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Add Expense')