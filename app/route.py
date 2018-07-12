from flask import flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app import app, db
from app.form import Login
from app.models import User

@app.route('/', methods = ['GET'])
@app.route('/home', methods = ['GET'])
def home():
    return "Hello World!"


@app.route('/<string:user>', methods=['GET','POST'])
def user_profile(user):
    '''
        This functions take in user from url bar and outputs on the page
        
        :param user: takes in user's name from url
    '''
    return render_template('user.html', title = User, user = user)


@app.route('/login', methods=['GET','POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = Login()
    user_data = User.query.filter_by(username = form.username.data).first()
    if form.validate_on_submit():
        if user is None or not user.check_password(form.password.data):
            flash("Invalid Username or Passowrd")
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for('home'))
  
    return render_template('login.html', title = Login, form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/signup', methods=['POST'])
def regesiter