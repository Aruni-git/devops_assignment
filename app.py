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

#employees table
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

#departments table
class department(db.Model):
   id = db.Column('departmentId', db.Integer, primary_key = True, autoincrement = True)
   department = db.Column(db.String(100))

def __init__(self, department):
   self.department = department
   
#navigate to home page
@app.route('/')
def home():
   return render_template('dashboard.html')



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
      return render_template('employees.html')

   
   return render_template('employees.html')

# Create New
@app.route('/addemployee', methods=['GET', 'POST'])
def addEmployee():
    if request.method == 'POST':
        date = request.form['date']
        title = request.form['blog_title']
        post = request.form['blog_main']
        post_entry = models.BlogPost(date = date, title = title, post = post)
        db.session.add(post_entry)
        db.session.commit()
        return redirect(url_for('database'))
    else:
        return render_template('entry.html')

@app.route('/database', methods=['GET', 'POST'])        
def database():
    query = []
    for i in session.query(models.BlogPost):
        query.append((i.title, i.post, i.date))
    return render_template('database.html', query = query)
 
 
  #show all
@app.route('/show_all')
def show_all():
   return render_template('employees.html', employees = employees.query.all() )

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

 #view all departments
@app.route('/departments')
def viewDepartments():
   return render_template('departments.html', department = department.query.all() )

#create new department
@app.route('/newD', methods = ['GET', 'POST'])
def createDepartment():
   if request.method == 'POST':
      if not request.form['department']:
         flash('Please enter all the fields', 'error')
      else:
         employee = employees( department= request.form['department'],
                            )
         db.session.add(department)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('departments'))
   
   return render_template('departments.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)