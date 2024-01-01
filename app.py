import os
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'
app.config['SECRET_KEY'] = "random string"


# # blueprint for auth routes in our app
# from .auth import auth as auth_blueprint
# app.register_blueprint(auth_blueprint)

#     # blueprint for non-auth parts of app
# from .main import main as main_blueprint
# app.register_blueprint(main_blueprint)


# these two lines added to mac os support
db_name = 'employee.db'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, db_name)

db = SQLAlchemy(app)

class employees(db.Model):
   id = db.Column('eid', db.Integer, primary_key = True, autoincrement = True)
   firstName = db.Column(db.String(100))
   lastName = db.Column(db.String(100))
   phone = db.Column(db.String(50))
   email = db.Column(db.String(200)) 
   department = db.Column(db.Integer())
   designation = db.Column(db.Integer())
   uid = db.Column(db.Integer())

def __init__(self, firstName, lastName, phone,email,department,designation,uid):
   self.firstName = firstName
   self.lastName = lastName
   self.phone = phone
   self.email = email
   self.department = department
   self.designation = designation
   self.uid = uid

#navigate to home page
@app.route('/')
def home():
   return render_template('home.html')

 #show all
@app.route('/show_all')
def show_all():
   return render_template('show_all.html', employees = employees.query.all() )

#get employee/ create a new employee
@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['firstName'] or not request.form['lastName'] or not request.form['email']:
         flash('Please enter all the fields', 'error')
      else:
         employee = employees( firstName= request.form['firstName'],
                             lastName=request.form['lastName'],
            phone =request.form['phone'], 
            email =request.form['email'] ,
            department =request.form['department'],
            designation =request.form['designation'])
         db.session.add(employee)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   
   return render_template('new.html')

# #update an employee
# @app.route('/update', methods = 'PUT')
# def new():
#    if request.method == 'PUT':
#       if not request.form['name'] or not request.form['city'] or not request.form['address']:
#          flash('Please enter all the fields', 'error')
#       else:
#          employee = employees( name= request.form['name'], city=request.form['city'],
#             address =request.form['address'], pin =request.form['pin'])        
#          db.session.add(employee)
#          db.session.commit()
#          #flash('Record was successfully added')
#          return redirect(url_for('show_all'))
#    flash('Record was successfully added')
#    return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
   
if __name__ == "__main__":
   port = int(os.environ.get('PORT', 5000))
   app.run(debug=True, host='0.0.0.0', port=port)