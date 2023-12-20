import os
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'
app.config['SECRET_KEY'] = "random string"

# these two lines added to mac os support
db_name = 'employee.db'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, db_name)

db = SQLAlchemy(app)

class employees(db.Model):
   id = db.Column('employee_id', db.Integer, primary_key = True, autoincrement = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   address = db.Column(db.String(200)) 
   pin = db.Column(db.String(10))

def __init__(self, name, city, address,pin):
   self.name = name
   self.city = city
   self.address = address
   self.pin = pin

@app.route('/', methods = ['GET'])
def show_all():
   return render_template('show_all.html', employees = employees.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['address']:
         flash('Please enter all the fields', 'error')
      else:
         employee = employees( name= request.form['name'], city=request.form['city'],
            address =request.form['address'], pin =request.form['pin'])        
         db.session.add(employee)
         db.session.commit()
         #flash('Record was successfully added')
         return redirect(url_for('show_all'))
   flash('Record was successfully added')
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)