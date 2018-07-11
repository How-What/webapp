from flask import render_template
from app import app
from app.form import Login

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
    return render_template('user.html', user= user, form = Login())