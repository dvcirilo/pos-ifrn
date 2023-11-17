from flask import Flask, render_template, request, flash, redirect, url_for
import users

app = Flask(__name__)

user_api = users.Users()

@app.route('/')
def index():
    return render_template('index.html', users=user_api.list())

@app.route('/user/<int:user_id>')
def user(user_id):
    return render_template('user.html', user_data=user_api.read(user_id))

@app.route('/user/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        if not request.form['user_name']:
            flash('O nome é obrigatório!')
        else:
            user_data=user_api.create(request.form)
            return render_template('user.html', user_data=user_data)
    return render_template('create.html')


