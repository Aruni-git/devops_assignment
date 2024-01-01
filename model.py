#Author name: Aruni
#Purpose: Create each tables with its attributes in the database


from .. import db, ma
from datetime import datetime
#from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
#from flask_dance.consumer import oauth_authorized, oauth_error


#departments table
class department(db.Model):
   id = db.Column('departmentId', db.Integer, primary_key = True, autoincrement = True)
   department = db.Column(db.String(100))
   description = db.Column(db.String(100))


def __repr__(self) -> str:
        return self.department
    
class DepartmentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("department","description")

# for a single instance of department
department_schema = DepartmentSchema()
# for many instances of Attendance
department_schema = DepartmentSchema(many=True)




# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(256), unique=True)
#     # ... other columns as needed

# class OAuth(db.Model, OAuthConsumerMixin):
#     user_id = db.Column(db.Integer, db.ForeignKey(User.id))
#     user = db.relationship(User)
    
  