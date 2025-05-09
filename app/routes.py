from flask import Blueprint, render_template, redirect, url_for, request, flash
from .forms import RegisterForm, LoginForm, ExpenseForm
from .models import User, Expense
from . import db
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return 'Expense Tracker is running!'

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('User created. Please log in.')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = ExpenseForm()
    if form.validate_on_submit():
        new_expense = Expense(
            name=form.name.data,
            amount=form.amount.data,
            category=form.category.data,
            date=form.date.data,
            user_id=current_user.id
        )
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added successfully.')
        return redirect(url_for('main.dashboard'))
    
    category = request.args.get('category')
    date = request.args.get('date')

    query = Expense.query.filter_by(user_id=current_user.id)
    if category:
        query = query.filter_by(category=category)
    if date:
        query = query.filter(Expense.date == date)

    expenses = query.order_by(Expense.date.desc()).all()

    return render_template('dashboard.html', form=form, expenses=expenses)

@main.route('/delete_expense/<int:expense_id>', methods=['POST'])
@login_required
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)

    if expense.user_id != current_user.id:
        flash("You don't have permission to delete this expense.")
        return redirect(url_for('main.dashboard'))

    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully.')
    return redirect(url_for('main.dashboard'))

@main.route('/edit_expense/<int:expense_id>', methods=['GET', 'POST'])
@login_required
def edit_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    if expense.user_id != current_user.id:
        flash("You don't have permission to edit this expense.")
        return redirect(url_for('main.dashboard'))

    form = ExpenseForm(obj=expense)
    if form.validate_on_submit():
        expense.name = form.name.data
        expense.amount = form.amount.data
        expense.date = form.date.data
        expense.category = form.category.data
        db.session.commit()
        flash('Expense updated.')
        return redirect(url_for('main.dashboard'))

    return render_template('edit_expense.html', form=form)