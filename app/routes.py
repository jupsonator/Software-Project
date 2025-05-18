from flask import Blueprint, render_template, redirect, url_for, request, flash
from .forms import RegisterForm, LoginForm, ExpenseForm
from .models import User, Expense
from . import db
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from collections import defaultdict

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

   
    category_filter = request.args.get('category')
    sort_by = request.args.get('sort_by')

    expenses_query = Expense.query.filter_by(user_id=current_user.id)

    if category_filter:
        expenses_query = expenses_query.filter_by(category=category_filter)

    if sort_by == 'date_asc':
        expenses_query = expenses_query.order_by(Expense.date.asc())
    elif sort_by == 'date_desc':
        expenses_query = expenses_query.order_by(Expense.date.desc())
    elif sort_by == 'amount_asc':
        expenses_query = expenses_query.order_by(Expense.amount.asc())
    elif sort_by == 'amount_desc':
        expenses_query = expenses_query.order_by(Expense.amount.desc())
    else:
        expenses_query = expenses_query.order_by(Expense.date.desc())  # default

    expenses = expenses_query.all()

    category_data = defaultdict(float)
    total_amount = 0

    for exp in expenses:
        category_data[exp.category] += exp.amount
        total_amount += exp.amount

    categories = list(category_data.keys())
    category_totals = list(category_data.values())

    return render_template(
        'dashboard.html',
        form=form,
        expenses=expenses,
        total_amount=total_amount,
        categories=categories,
        category_totals=category_totals
    )

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

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.login'))