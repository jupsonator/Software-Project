# Expense Tracker App

A full-featured web-based personal finance tracker built with Flask. Users can register, log in, and manage expenses through a clean dashboard featuring data visualization and flexible filtering options.

---

## Overview

This app helps users:

* Record and categorize personal expenses
* Visualize spending via dynamic pie charts
* Sort/filter transactions by category, date, or amount
* Manage entries with edit/delete features
* Stay organized with a simple, intuitive interface

---

## Tech Stack

**Backend**

* Flask
* Flask-Login (user session management)
* Flask-SQLAlchemy (ORM)
* Flask-WTF (form handling)

**Frontend**

* Jinja2 (templating)
* HTML/CSS
* Chart.js (pie chart for category breakdown)

**Data**

* SQLite (local dev DB via SQLAlchemy)
* Pandas / NumPy (for future data processing)

---

## Project Structure

```
project/
├── app/
│   ├── __init__.py          # App factory and config
│   ├── models.py            # User and Expense models
│   ├── forms.py             # Login, Register, Expense forms
│   ├── routes.py            # Main application routes
│   └── templates/           # HTML templates (Jinja2)
│       ├── dashboard.html
│       ├── edit_expense.html
│       ├── login.html
│       └── register.html
├── config.py                # App configuration
├── run.py                   # Entry point
├── requirements.txt         # Python dependencies
```

---

## Getting Started

### Prerequisites

* Python 3.8+
* Virtual environment (recommended)

### Installation

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

### ⚙️ Configuration

Create a `.env` file or use `config.py` to provide environment variables:

```env
SECRET_KEY=your-secret-key
SQLALCHEMY_DATABASE_URI=sqlite:///app.db
```

### Initialize Database

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

### Run the App

```bash
python run.py
```

Visit `http://localhost:5000/login` to start using the app.

---

## Features in Action

### Authentication

* Register and log in securely
* Session-based user tracking with Flask-Login

### Expense Management

* Add, update, and delete expenses
* Categorize by Food, Transport, Leisure, Other

### Dashboard

* Pie chart shows expense distribution by category using **Chart.js**
* Filter by category
* Sort by date or amount (ascending/descending)
* Total expense calculation

### Simple UI

Clean, readable HTML templates powered by Flask + Jinja2:

* `register.html`
* `login.html`
* `dashboard.html`
* `edit_expense.html`

---

## Potential Improvements

* CSV export for expense history
* Monthly/weekly budgeting tools
* Mobile-first responsive design
* Google OAuth login
* Notifications or reminders for recurring expenses

---

## Testing

Manual testing via browser sessions is recommended for now. Consider adding:

* Flask test client for unit/integration tests
* Selenium for end-to-end UI testing

---

## License

[MIT License](LICENSE)

---

