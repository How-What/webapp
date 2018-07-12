from flask import flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app import app, db
from app.form import Login, Register
from app.models import User

@app.route('/', methods = ['GET'])
@app.route('/home', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def home():
    return render_template('index.html', title = 'Home - Generic')


@app.route('/<string:user>', methods=['GET','POST'])
def user_profile(user):
    '''
        This functions take in user from url bar and outputs on the page
        
        :param user: takes in user's name from url
    '''
    return render_template('user.html', title = "user", user = user)


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
    '''
        logs the user out then takes back to home page
    '''
    logout_user()
    return redirect(url_for('home'))


@app.route('/sign-up', methods=['GET','POST'])
@app.route('/register', methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = Register()
    if form.validate_on_submit():
        user = User(username = form.username.data,email =  form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You are now registered!")
        return redirect(url_for('login'))
    
    return render_template('register.html', title = "Signup - Generic website", form = form)