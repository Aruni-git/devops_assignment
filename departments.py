from flask import request, jsonify, Blueprint
from flask import Flask, request, flash, url_for, redirect, render_template
from model import department
from .. import db
from datetime import datetime, timedelta

dep = Blueprint('departments', __name__, url_prefix='')

#view all departments
@dep.route('/departments', methods=['GET'])
def viewDepartments():
   return render_template('departments.html', department = department.query.all() )
