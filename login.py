# Author: Aruni
#Purpose: For authentication


from . import app, db
from flask import jsonify, request
from flask import Blueprint
from .models.model import Course, courses_schema

#course route
cs = Blueprint('course', __name__, url_prefix='/api/course')


@cs.route("/")
def course():
    return jsonify({"Welcome": "Course Page"})