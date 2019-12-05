from flask import render_template, redirect, url_for, flash
from website import app
from website.forms import RegistrationForm, LoginForm
from website.models import Users, Posts

posts = [
    {
        'author': 'Rodrigo Brochado',
        'title': 'ACONCHEGO',
        'content': 'First post content',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'Bob dog',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)
