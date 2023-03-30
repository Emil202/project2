from app import app
from flask import render_template,request,redirect,flash,url_for
from models import Contact,User,Image
from forms import ContactForm, RegisterForm,LoginForm
from datetime import datetime   
from werkzeug.security import check_password_hash
from flask_login import login_user,logout_user,login_required
from flask_security import current_user



@app.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        post_data = request.form
        form = RegisterForm(data=post_data)
        if form.validate_on_submit():
            user = User(full_name = form.full_name.data, email = form.email.data , password = form.password.data)
            user.save()
            return redirect('/login')
    return render_template('register.html', form = form)


@app.route('/login', methods= ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        post_data = request.data
        form =LoginForm(data = post_data)
        if form.validate_on_submit():
            user = User.query.filter_by(email = form.email.data).first()
            if user and check_password_hash(user.password,form.password.data):
                login_user(user)
               
                
                return redirect('/shop')
            else:
                
                flash('Wrong email or password')
    return render_template('login.html', form =form)


@app.route('/contact', methods = ['GET','POST'])

def contact():
    form = ContactForm()

    if  request.method == 'POST':
        print('post')
        print(request.form)
        form = ContactForm(request.form)
        if form.validate_on_submit():
            print('post')   
            contact = Contact(
                full_name = form.full_name.data,
                email = form.email.data,
                message = form.message.data
            )
            contact.save()
    return render_template('contact.html', form = form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route('/home')
def home():
    return render_template('index.html')