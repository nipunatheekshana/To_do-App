import app as backend_app
from flask import Flask, render_template,jsonify,request,redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv
from user import User
import dbms

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

# Load user callback for Flask-Login
@login_manager.user_loader
def load_user(username):
    dbUser=dbms.get('users',['username','password'], f"username = '{username}'")
    if dbUser :
        return User(username)
    return None

# unauthorized_handler redirects to login page
@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        dbUser=dbms.get('users',['username','password'], f"username = '{username}'")
        if dbUser and bcrypt.check_password_hash(dbUser[0][1], password):
            user = User(username)
            login_user(user)  # Log the user in
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

@app.route('/register-page', methods=['GET', 'POST'])
def register_page():
    return  render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if not(dbms.ifExcist('users')):
        dbms.create_user_table()
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        dbUser=dbms.get('users',['username'], f"username = '{username}'")
   
        #validation
        if dbUser:
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))
        
        # save to database
        dbms.insert('users',{'username':username,'password': bcrypt.generate_password_hash(password).decode('utf-8')})

        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')  

@app.route('/')
@login_required
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return jsonify({"error": str(e)}), 500 

@app.route('/load-tasks', methods=['GET'])
@login_required
def load_tasks():
    try:    
        data= backend_app.load_tasks(current_user.userId)
        return {"tasks":data}
    except Exception as e: 
        return jsonify({"error": str(e)}), 500 
    
@app.route('/save-tasks', methods=['POST'])
@login_required
def saveTasks():
    try:    
        tasks = request.get_json() 
        backend_app.save_tasks(current_user.userId,tasks['tasks'])

        return {"success":True}
    except Exception as e:
        return jsonify({"error": str(e)}), 500 

if __name__ == '__main__':
    app.run(debug=True)