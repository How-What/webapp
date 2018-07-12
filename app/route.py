from flask import render_template, redirect, url_for
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

    form = Login()
    user_data = User(username = form.username.data, password_hash = form.password.data)
  
    if form.validate_on_submit():
        db.session.add(user_data)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('user.html', user= user, form = Login())
